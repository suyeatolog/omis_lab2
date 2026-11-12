from typing import List, Optional

from PySide6.QtWidgets import QPushButton, QWidget

from ..models.models import HistoryRecord, Package
from ..services.services import (
    PackageService,
    SearchService,
    TrackingService,
    UserService,
)
from ..ui.ui_transformed.ui_admin import Ui_AdminWindow
from ..ui.ui_transformed.ui_client import Ui_ClientWindow
from ..ui.ui_transformed.ui_employee import Ui_EmployeeWindow
from ..ui.ui_transformed.ui_login import Ui_LoginWindow
from ..ui.ui_transformed.ui_register import Ui_RegisterWindow

ACTIVE_NAV_STYLE = "background: #f5c28b;"
INACTIVE_NAV_STYLE = "background: white;"


def highlight_button(active_btn: Optional[QPushButton], buttons: List[QPushButton], center: bool = False):
    align = "text-align: center;" if center else ""
    for btn in buttons:
        if btn == active_btn:
            btn.setStyleSheet(f"{ACTIVE_NAV_STYLE} {align}")
        else:
            btn.setStyleSheet(f"{INACTIVE_NAV_STYLE} {align}")


class LoginView(QWidget):
    def __init__(self, router: "SystemInterface"):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.router = router
        self.ui.btnGoReg.clicked.connect(self.router.show_register)
        self.ui.btnLogin.clicked.connect(self.on_login)

    def on_login(self):
        username = self.ui.editUsername.text().strip().lower()
        password = self.ui.editPassword.text()
        self.router.login(username, password)


class RegisterView(QWidget):
    def __init__(self, router: "SystemInterface"):
        super().__init__()
        self.ui = Ui_RegisterWindow()
        self.ui.setupUi(self)
        self.router = router
        self.ui.btnGoLog.clicked.connect(self.router.show_login)
        self.ui.btnRegister.clicked.connect(self.router.show_login)


class ClientView(QWidget):
    def __init__(self, router: "SystemInterface"):
        super().__init__()
        self.ui = Ui_ClientWindow()
        self.ui.setupUi(self)
        self.router = router
        self.collapsed = False
        self.nav_buttons = [self.ui.btnNavFind, self.ui.btnNavMy, self.ui.btnNavSettings]

        self.ui.stackedFindResult.setCurrentIndex(0)
        self.ui.btnNavFind.clicked.connect(lambda: self.switch_tab(0, self.ui.btnNavFind))
        self.ui.btnNavMy.clicked.connect(lambda: self.switch_tab(1, self.ui.btnNavMy))
        self.ui.btnNavSettings.clicked.connect(lambda: self.switch_tab(2, self.ui.btnNavSettings))
        self.ui.btnCollapse.clicked.connect(self.toggle_collapse)
        self.ui.btnLogout.clicked.connect(self.router.show_login)
        self.ui.btnFind.clicked.connect(self.on_find)
        self.ui.listMyPackages.itemClicked.connect(self.on_select_my_package)

    def switch_tab(self, index: int, btn: QPushButton):
        self.ui.stackedMain.setCurrentIndex(index)
        highlight_button(btn, self.nav_buttons)

    def toggle_collapse(self):
        self.collapsed = not self.collapsed
        width = 55 if self.collapsed else 160
        self.ui.sidebarFrame.setMinimumWidth(width)
        self.ui.sidebarFrame.setMaximumWidth(width)
        self.ui.btnLogout.setVisible(not self.collapsed)
        for btn, full, short in [
            (self.ui.btnCollapse, "☰  collapse", "☰"),
            (self.ui.btnNavFind, "□  find package", "□"),
            (self.ui.btnNavMy, "□  my package", "□"),
            (self.ui.btnNavSettings, "○  settings", "○"),
        ]:
            btn.setText(short if self.collapsed else full)

    def on_find(self):
        num = self.ui.editSearchNumber.text().strip()
        self.router.find_package(num)
        if not num or num == "0":
            self.ui.stackedFindResult.setCurrentIndex(1)
        else:
            self.ui.stackedFindResult.setCurrentIndex(2)

    def on_select_my_package(self):
        self.switch_tab(0, self.ui.btnNavFind)
        self.ui.stackedFindResult.setCurrentIndex(2)


class EmployeeView(QWidget):
    def __init__(self, router: "SystemInterface"):
        super().__init__()
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self)
        self.router = router
        self.collapsed = False
        self.nav_buttons = [self.ui.btnNavPackages, self.ui.btnNavAddPackage, self.ui.btnNavSettings]
        self.mode_buttons = [self.ui.btnModeUpdateHistory, self.ui.btnModeChangeData]

        self.ui.btnNavPackages.clicked.connect(self.open_packages_tab)
        self.ui.btnNavAddPackage.clicked.connect(self.open_add_package_tab)
        self.ui.btnNavSettings.clicked.connect(lambda: self.switch_tab(2, self.ui.btnNavSettings))
        self.ui.btnCollapse.clicked.connect(self.toggle_collapse)
        self.ui.btnLogout.clicked.connect(self.router.show_login)

        self.ui.btnFindPkg.clicked.connect(self.show_package_overview)
        self.ui.btnModeUpdateHistory.clicked.connect(self.show_update_history_mode)
        self.ui.btnModeChangeData.clicked.connect(self.show_change_data_mode)
        self.ui.btnSubmitHistory.clicked.connect(self.on_submit_history)
        self.ui.btnSubmitData.clicked.connect(self.on_submit_data)

        self.ui.btnAddPackage.clicked.connect(self.on_add_package)
        self.ui.btnAddOk.clicked.connect(self.open_add_package_tab)

    def switch_tab(self, index: int, btn: QPushButton):
        self.ui.stackedMain.setCurrentIndex(index)
        highlight_button(btn, self.nav_buttons)

    def toggle_collapse(self):
        self.collapsed = not self.collapsed
        width = 55 if self.collapsed else 160
        self.ui.sidebarFrame.setMinimumWidth(width)
        self.ui.sidebarFrame.setMaximumWidth(width)
        self.ui.btnLogout.setVisible(not self.collapsed)
        for btn, full, short in [
            (self.ui.btnCollapse, "☰  collapse", "☰"),
            (self.ui.btnNavPackages, "□  packages", "□"),
            (self.ui.btnNavAddPackage, "□  add package", "□"),
            (self.ui.btnNavSettings, "○  settings", "○"),
        ]:
            btn.setText(short if self.collapsed else full)

    def open_packages_tab(self):
        self.switch_tab(0, self.ui.btnNavPackages)
        self.show_package_overview()

    def show_package_overview(self):
        self.ui.stackedPackageDetails.setCurrentIndex(0)
        highlight_button(None, self.mode_buttons, center=True)

    def show_update_history_mode(self):
        self.ui.stackedPackageDetails.setCurrentIndex(1)
        highlight_button(self.ui.btnModeUpdateHistory, self.mode_buttons, center=True)

    def show_change_data_mode(self):
        self.ui.stackedPackageDetails.setCurrentIndex(2)
        highlight_button(self.ui.btnModeChangeData, self.mode_buttons, center=True)

    def on_submit_history(self):
        self.router.update_package_state()
        self.show_package_overview()

    def on_submit_data(self):
        self.show_package_overview()

    def open_add_package_tab(self):
        self.switch_tab(1, self.ui.btnNavAddPackage)
        self.ui.stackedAddPackage.setCurrentIndex(0)

    def on_add_package(self):
        self.router.register_package()
        self.ui.stackedAddPackage.setCurrentIndex(1)


class AdminView(QWidget):
    def __init__(self, router: "SystemInterface"):
        super().__init__()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self)
        self.router = router
        self.collapsed = False
        self.nav_buttons = [self.ui.btnNavUsers, self.ui.btnNavSettings]
        self.role_buttons = [self.ui.btnRoleAdmin, self.ui.btnRoleClient, self.ui.btnRoleEmployee]

        self.ui.stackedUserResult.setCurrentIndex(0)
        self.ui.btnNavUsers.clicked.connect(self.open_users_tab)
        self.ui.btnNavSettings.clicked.connect(lambda: self.switch_tab(1, self.ui.btnNavSettings))
        self.ui.btnCollapse.clicked.connect(self.toggle_collapse)
        self.ui.btnLogout.clicked.connect(self.router.show_login)
        self.ui.btnFindUser.clicked.connect(self.on_find_user)

        for btn in self.role_buttons:
            btn.clicked.connect(lambda checked=False, b=btn: self.select_role(b))

    def switch_tab(self, index: int, btn: QPushButton):
        self.ui.stackedMain.setCurrentIndex(index)
        highlight_button(btn, self.nav_buttons)

    def open_users_tab(self):
        self.switch_tab(0, self.ui.btnNavUsers)
        self.ui.stackedUserResult.setCurrentIndex(0)

    def toggle_collapse(self):
        self.collapsed = not self.collapsed
        width = 55 if self.collapsed else 160
        self.ui.sidebarFrame.setMinimumWidth(width)
        self.ui.sidebarFrame.setMaximumWidth(width)
        self.ui.btnLogout.setVisible(not self.collapsed)
        for btn, full, short in [
            (self.ui.btnCollapse, "☰  collapse", "☰"),
            (self.ui.btnNavUsers, "□  users", "□"),
            (self.ui.btnNavSettings, "○  settings", "○"),
        ]:
            btn.setText(short if self.collapsed else full)

    def on_find_user(self):
        uid = self.ui.editSearchUser.text().strip()
        self.router.manage_users()
        if not uid or uid == "0":
            self.ui.stackedUserResult.setCurrentIndex(0)
        else:
            self.ui.stackedUserResult.setCurrentIndex(1)

    def select_role(self, selected_btn: QPushButton):
        for btn in self.role_buttons:
            if btn == selected_btn:
                btn.setStyleSheet("background: #b8d4f2; font-weight: bold; text-align: center;")
            else:
                btn.setStyleSheet("background: white; font-weight: bold; text-align: center;")


class SystemInterface:
    def __init__(
        self,
        search_service: SearchService,
        package_service: PackageService,
        tracking_service: TrackingService,
        user_service: UserService,
    ):
        self.search_service = search_service
        self.package_service = package_service
        self.tracking_service = tracking_service
        self.user_service = user_service
        self.current_window: Optional[QWidget] = None

    def login(self, login_str: str, password: str) -> bool:
        if "admin" in login_str:
            self._switch_window(AdminView(self))
        elif "emp" in login_str:
            self._switch_window(EmployeeView(self))
        else:
            self._switch_window(ClientView(self))
        return True

    def register_package(self, *args, **kwargs) -> None:
        pass

    def update_package_state(self, *args, **kwargs) -> None:
        pass

    def find_package(self, tracking_number: str) -> Optional[Package]:
        return self.search_service.find_by_number(tracking_number)

    def show_history(self, tracking_number: str) -> List[HistoryRecord]:
        return []

    def manage_users(self) -> None:
        pass

    def _switch_window(self, new_window: QWidget) -> None:
        if self.current_window is not None:
            self.current_window.close()
        self.current_window = new_window
        self.current_window.show()

    def show_login(self) -> None:
        self._switch_window(LoginView(self))

    def show_register(self) -> None:
        self._switch_window(RegisterView(self))