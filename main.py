import sys

from PySide6.QtWidgets import QApplication

from src.interface.interface import SystemInterface
from src.services.services import (
    PackageService,
    SearchService,
    TrackingService,
    UserService,
)


class AppAssembler:
    def assemble(self) -> SystemInterface:
        search_service = SearchService()
        package_service = PackageService()
        tracking_service = TrackingService()
        user_service = UserService()

        return SystemInterface(
            search_service=search_service,
            package_service=package_service,
            tracking_service=tracking_service,
            user_service=user_service,
        )


class MainProgram:
    @staticmethod
    def main(assembler: AppAssembler) -> None:
        app = QApplication(sys.argv)
        system_interface = assembler.assemble()
        system_interface.show_login()
        sys.exit(app.exec())


if __name__ == "__main__":
    assembler = AppAssembler()
    MainProgram.main(assembler)