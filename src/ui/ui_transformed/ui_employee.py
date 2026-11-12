# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextBrowser, QVBoxLayout,
    QWidget)

from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        if not EmployeeWindow.objectName():
            EmployeeWindow.setObjectName(u"EmployeeWindow")
        EmployeeWindow.resize(850, 520)
        self.mainLayout = QHBoxLayout(EmployeeWindow)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(EmployeeWindow)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(160, 0))
        self.sidebarFrame.setMaximumSize(QSize(160, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.btnCollapse = QPushButton(self.sidebarFrame)
        self.btnCollapse.setObjectName(u"btnCollapse")

        self.sidebarLayout.addWidget(self.btnCollapse)

        self.btnNavPackages = QPushButton(self.sidebarFrame)
        self.btnNavPackages.setObjectName(u"btnNavPackages")

        self.sidebarLayout.addWidget(self.btnNavPackages)

        self.btnNavAddPackage = QPushButton(self.sidebarFrame)
        self.btnNavAddPackage.setObjectName(u"btnNavAddPackage")

        self.sidebarLayout.addWidget(self.btnNavAddPackage)

        self.btnNavSettings = QPushButton(self.sidebarFrame)
        self.btnNavSettings.setObjectName(u"btnNavSettings")

        self.sidebarLayout.addWidget(self.btnNavSettings)

        self.vSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.vSpacer)

        self.btnLogout = QPushButton(self.sidebarFrame)
        self.btnLogout.setObjectName(u"btnLogout")

        self.sidebarLayout.addWidget(self.btnLogout)


        self.mainLayout.addWidget(self.sidebarFrame)

        self.stackedMain = QStackedWidget(EmployeeWindow)
        self.stackedMain.setObjectName(u"stackedMain")
        self.pagePackages = QWidget()
        self.pagePackages.setObjectName(u"pagePackages")
        self.vboxLayout = QVBoxLayout(self.pagePackages)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(20, 20, 20, 20)
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.editSearchPkg = QLineEdit(self.pagePackages)
        self.editSearchPkg.setObjectName(u"editSearchPkg")
        self.editSearchPkg.setMinimumSize(QSize(0, 36))

        self.hboxLayout.addWidget(self.editSearchPkg)

        self.btnFindPkg = QPushButton(self.pagePackages)
        self.btnFindPkg.setObjectName(u"btnFindPkg")
        self.btnFindPkg.setMinimumSize(QSize(80, 36))

        self.hboxLayout.addWidget(self.btnFindPkg)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.outerCard = QFrame(self.pagePackages)
        self.outerCard.setObjectName(u"outerCard")
        self.hboxLayout1 = QHBoxLayout(self.outerCard)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(20, 20, 20, 20)
        self.vboxLayout1 = QVBoxLayout()
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.lblBox = QLabel(self.outerCard)
        self.lblBox.setObjectName(u"lblBox")
        self.lblBox.setMinimumSize(QSize(210, 210))
        self.lblBox.setAlignment(Qt.AlignCenter)
        self.lblBox.setPixmap(QPixmap(str(ASSETS_DIR / "cube.png")))
        self.lblBox.setScaledContents(True)

        self.vboxLayout1.addWidget(self.lblBox)

        self.btnModeUpdateHistory = QPushButton(self.outerCard)
        self.btnModeUpdateHistory.setObjectName(u"btnModeUpdateHistory")

        self.vboxLayout1.addWidget(self.btnModeUpdateHistory)

        self.btnModeChangeData = QPushButton(self.outerCard)
        self.btnModeChangeData.setObjectName(u"btnModeChangeData")

        self.vboxLayout1.addWidget(self.btnModeChangeData)


        self.hboxLayout1.addLayout(self.vboxLayout1)

        self.stackedPackageDetails = QStackedWidget(self.outerCard)
        self.stackedPackageDetails.setObjectName(u"stackedPackageDetails")
        self.subViewDetails = QWidget()
        self.subViewDetails.setObjectName(u"subViewDetails")
        self.vboxLayout2 = QVBoxLayout(self.subViewDetails)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.lblDetails = QLabel(self.subViewDetails)
        self.lblDetails.setObjectName(u"lblDetails")

        self.vboxLayout2.addWidget(self.lblDetails)

        self.historyFrame = QFrame(self.subViewDetails)
        self.historyFrame.setObjectName(u"historyFrame")
        self.vboxLayout3 = QVBoxLayout(self.historyFrame)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.lblHTitle = QLabel(self.historyFrame)
        self.lblHTitle.setObjectName(u"lblHTitle")
        self.lblHTitle.setAlignment(Qt.AlignCenter)

        self.vboxLayout3.addWidget(self.lblHTitle)

        self.txtHistory = QTextBrowser(self.historyFrame)
        self.txtHistory.setObjectName(u"txtHistory")

        self.vboxLayout3.addWidget(self.txtHistory)


        self.vboxLayout2.addWidget(self.historyFrame)

        self.stackedPackageDetails.addWidget(self.subViewDetails)
        self.subUpdateHistory = QWidget()
        self.subUpdateHistory.setObjectName(u"subUpdateHistory")
        self.vboxLayout4 = QVBoxLayout(self.subUpdateHistory)
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.innerRightCard = QFrame(self.subUpdateHistory)
        self.innerRightCard.setObjectName(u"innerRightCard")
        self.vboxLayout5 = QVBoxLayout(self.innerRightCard)
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.vboxLayout5.setContentsMargins(20, 20, 20, 20)
        self.lblUpdHistoryFields = QLabel(self.innerRightCard)
        self.lblUpdHistoryFields.setObjectName(u"lblUpdHistoryFields")

        self.vboxLayout5.addWidget(self.lblUpdHistoryFields)

        self.vSp1 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout5.addItem(self.vSp1)

        self.btnSubmitHistory = QPushButton(self.innerRightCard)
        self.btnSubmitHistory.setObjectName(u"btnSubmitHistory")

        self.vboxLayout5.addWidget(self.btnSubmitHistory)


        self.vboxLayout4.addWidget(self.innerRightCard)

        self.stackedPackageDetails.addWidget(self.subUpdateHistory)
        self.subChangeData = QWidget()
        self.subChangeData.setObjectName(u"subChangeData")
        self.vboxLayout6 = QVBoxLayout(self.subChangeData)
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.innerRightCard1 = QFrame(self.subChangeData)
        self.innerRightCard1.setObjectName(u"innerRightCard1")
        self.vboxLayout7 = QVBoxLayout(self.innerRightCard1)
        self.vboxLayout7.setObjectName(u"vboxLayout7")
        self.vboxLayout7.setContentsMargins(20, 20, 20, 20)
        self.lblChgDataFields = QLabel(self.innerRightCard1)
        self.lblChgDataFields.setObjectName(u"lblChgDataFields")

        self.vboxLayout7.addWidget(self.lblChgDataFields)

        self.vSp2 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout7.addItem(self.vSp2)

        self.btnSubmitData = QPushButton(self.innerRightCard1)
        self.btnSubmitData.setObjectName(u"btnSubmitData")

        self.vboxLayout7.addWidget(self.btnSubmitData)


        self.vboxLayout6.addWidget(self.innerRightCard1)

        self.stackedPackageDetails.addWidget(self.subChangeData)

        self.hboxLayout1.addWidget(self.stackedPackageDetails)


        self.vboxLayout.addWidget(self.outerCard)

        self.stackedMain.addWidget(self.pagePackages)
        self.pageAddPackage = QWidget()
        self.pageAddPackage.setObjectName(u"pageAddPackage")
        self.vboxLayout8 = QVBoxLayout(self.pageAddPackage)
        self.vboxLayout8.setObjectName(u"vboxLayout8")
        self.vboxLayout8.setContentsMargins(25, 25, 25, 25)
        self.outerCard1 = QFrame(self.pageAddPackage)
        self.outerCard1.setObjectName(u"outerCard1")
        self.hboxLayout2 = QHBoxLayout(self.outerCard1)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.hboxLayout2.setContentsMargins(25, 25, 25, 25)
        self.vboxLayout9 = QVBoxLayout()
        self.vboxLayout9.setObjectName(u"vboxLayout9")
        self.lblAddBox = QLabel(self.outerCard1)
        self.lblAddBox.setObjectName(u"lblAddBox")
        self.lblAddBox.setMinimumSize(QSize(180, 180))
        self.lblAddBox.setAlignment(Qt.AlignCenter)
        self.lblAddBox.setPixmap(QPixmap(str(ASSETS_DIR / "cube.png")))
        self.lblAddBox.setScaledContents(True)

        self.vboxLayout9.addWidget(self.lblAddBox)

        self.btnAddPackage = QPushButton(self.outerCard1)
        self.btnAddPackage.setObjectName(u"btnAddPackage")

        self.vboxLayout9.addWidget(self.btnAddPackage)

        self.vSp3 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout9.addItem(self.vSp3)


        self.hboxLayout2.addLayout(self.vboxLayout9)

        self.stackedAddPackage = QStackedWidget(self.outerCard1)
        self.stackedAddPackage.setObjectName(u"stackedAddPackage")
        self.subAddForm = QWidget()
        self.subAddForm.setObjectName(u"subAddForm")
        self.vboxLayout10 = QVBoxLayout(self.subAddForm)
        self.vboxLayout10.setObjectName(u"vboxLayout10")
        self.innerRightCard2 = QFrame(self.subAddForm)
        self.innerRightCard2.setObjectName(u"innerRightCard2")
        self.vboxLayout11 = QVBoxLayout(self.innerRightCard2)
        self.vboxLayout11.setObjectName(u"vboxLayout11")
        self.vboxLayout11.setContentsMargins(20, 20, 20, 20)
        self.lblAddFields = QLabel(self.innerRightCard2)
        self.lblAddFields.setObjectName(u"lblAddFields")

        self.vboxLayout11.addWidget(self.lblAddFields)

        self.vSp4 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout11.addItem(self.vSp4)


        self.vboxLayout10.addWidget(self.innerRightCard2)

        self.stackedAddPackage.addWidget(self.subAddForm)
        self.subAddSuccess = QWidget()
        self.subAddSuccess.setObjectName(u"subAddSuccess")
        self.vboxLayout12 = QVBoxLayout(self.subAddSuccess)
        self.vboxLayout12.setObjectName(u"vboxLayout12")
        self.innerRightCard3 = QFrame(self.subAddSuccess)
        self.innerRightCard3.setObjectName(u"innerRightCard3")
        self.vboxLayout13 = QVBoxLayout(self.innerRightCard3)
        self.vboxLayout13.setObjectName(u"vboxLayout13")
        self.vSp5 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout13.addItem(self.vSp5)

        self.lblSuccessMsg = QLabel(self.innerRightCard3)
        self.lblSuccessMsg.setObjectName(u"lblSuccessMsg")
        self.lblSuccessMsg.setAlignment(Qt.AlignCenter)

        self.vboxLayout13.addWidget(self.lblSuccessMsg)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.hSp1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout3.addItem(self.hSp1)

        self.btnAddOk = QPushButton(self.innerRightCard3)
        self.btnAddOk.setObjectName(u"btnAddOk")
        self.btnAddOk.setMinimumSize(QSize(90, 36))

        self.hboxLayout3.addWidget(self.btnAddOk)

        self.hSp2 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout3.addItem(self.hSp2)


        self.vboxLayout13.addLayout(self.hboxLayout3)

        self.vSp6 = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout13.addItem(self.vSp6)


        self.vboxLayout12.addWidget(self.innerRightCard3)

        self.stackedAddPackage.addWidget(self.subAddSuccess)

        self.hboxLayout2.addWidget(self.stackedAddPackage)


        self.vboxLayout8.addWidget(self.outerCard1)

        self.stackedMain.addWidget(self.pageAddPackage)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.vboxLayout14 = QVBoxLayout(self.pageSettings)
        self.vboxLayout14.setObjectName(u"vboxLayout14")
        self.vboxLayout14.setContentsMargins(25, 25, 25, 25)
        self.settingsBox = QFrame(self.pageSettings)
        self.settingsBox.setObjectName(u"settingsBox")
        self.vboxLayout15 = QVBoxLayout(self.settingsBox)
        self.vboxLayout15.setObjectName(u"vboxLayout15")
        self.vboxLayout15.setContentsMargins(15, 15, 15, 15)
        self.lblSetTitle = QLabel(self.settingsBox)
        self.lblSetTitle.setObjectName(u"lblSetTitle")
        self.lblSetTitle.setMinimumSize(QSize(0, 36))
        self.lblSetTitle.setAlignment(Qt.AlignCenter)

        self.vboxLayout15.addWidget(self.lblSetTitle)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.editSetName = QLineEdit(self.settingsBox)
        self.editSetName.setObjectName(u"editSetName")

        self.gridLayout.addWidget(self.editSetName, 0, 0, 1, 1)

        self.editSetSecondName = QLineEdit(self.settingsBox)
        self.editSetSecondName.setObjectName(u"editSetSecondName")

        self.gridLayout.addWidget(self.editSetSecondName, 0, 1, 1, 1)

        self.editSetUsername = QLineEdit(self.settingsBox)
        self.editSetUsername.setObjectName(u"editSetUsername")

        self.gridLayout.addWidget(self.editSetUsername, 1, 0, 1, 1)

        self.editSetEmail = QLineEdit(self.settingsBox)
        self.editSetEmail.setObjectName(u"editSetEmail")

        self.gridLayout.addWidget(self.editSetEmail, 1, 1, 1, 1)


        self.vboxLayout15.addLayout(self.gridLayout)

        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.editSetPassword = QLineEdit(self.settingsBox)
        self.editSetPassword.setObjectName(u"editSetPassword")

        self.hboxLayout4.addWidget(self.editSetPassword)

        self.btnUpdateAccount = QPushButton(self.settingsBox)
        self.btnUpdateAccount.setObjectName(u"btnUpdateAccount")
        self.btnUpdateAccount.setMinimumSize(QSize(220, 34))

        self.hboxLayout4.addWidget(self.btnUpdateAccount)


        self.vboxLayout15.addLayout(self.hboxLayout4)

        self.btnChangeTheme = QPushButton(self.settingsBox)
        self.btnChangeTheme.setObjectName(u"btnChangeTheme")
        self.btnChangeTheme.setMinimumSize(QSize(0, 36))

        self.vboxLayout15.addWidget(self.btnChangeTheme)

        self.lblLang = QLabel(self.settingsBox)
        self.lblLang.setObjectName(u"lblLang")
        self.lblLang.setMinimumSize(QSize(0, 36))
        self.lblLang.setAlignment(Qt.AlignCenter)

        self.vboxLayout15.addWidget(self.lblLang)

        self.hboxLayout5 = QHBoxLayout()
        self.hboxLayout5.setObjectName(u"hboxLayout5")
        self.editLang = QLineEdit(self.settingsBox)
        self.editLang.setObjectName(u"editLang")
        self.editLang.setReadOnly(True)

        self.hboxLayout5.addWidget(self.editLang)

        self.btnLangDrop = QPushButton(self.settingsBox)
        self.btnLangDrop.setObjectName(u"btnLangDrop")
        self.btnLangDrop.setMaximumSize(QSize(60, 34))

        self.hboxLayout5.addWidget(self.btnLangDrop)


        self.vboxLayout15.addLayout(self.hboxLayout5)

        self.vSpSet = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout15.addItem(self.vSpSet)


        self.vboxLayout14.addWidget(self.settingsBox)

        self.stackedMain.addWidget(self.pageSettings)

        self.mainLayout.addWidget(self.stackedMain)


        self.retranslateUi(EmployeeWindow)

        QMetaObject.connectSlotsByName(EmployeeWindow)
    # setupUi

    def retranslateUi(self, EmployeeWindow):
        EmployeeWindow.setWindowTitle(QCoreApplication.translate("EmployeeWindow", u"Employee Panel", None))
        EmployeeWindow.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QWidget { background: white; color: black; font-family: Arial; font-size: 14px; } QLineEdit { border: 1px solid black; padding: 6px; } QPushButton { border: 1px solid black; background: white; padding: 8px; text-align: left; } QPushButton:hover { background-color: #f2f2f2; } QPushButton:pressed { background-color: #e6e6e6; } QFrame#sidebarFrame { border-right: 1px solid black; } QFrame#outerCard, QFrame#innerRightCard, QFrame#historyFrame, QFrame#settingsBox { border: 1px solid black; }", None))
        self.btnCollapse.setText(QCoreApplication.translate("EmployeeWindow", u"\u2630  collapse", None))
        self.btnNavPackages.setText(QCoreApplication.translate("EmployeeWindow", u"\u25a1  packages", None))
        self.btnNavPackages.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { background: #f5c28b; } QPushButton:hover { background: #f0b06a; }", None))
        self.btnNavAddPackage.setText(QCoreApplication.translate("EmployeeWindow", u"\u25a1  add package", None))
        self.btnNavSettings.setText(QCoreApplication.translate("EmployeeWindow", u"\u25cb  settings", None))
        self.btnLogout.setText(QCoreApplication.translate("EmployeeWindow", u"log out", None))
        self.btnLogout.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"border: none; font-style: italic; text-align: center;", None))
        self.editSearchPkg.setText(QCoreApplication.translate("EmployeeWindow", u"123456", None))
        self.btnFindPkg.setText(QCoreApplication.translate("EmployeeWindow", u"FIND", None))
        self.btnFindPkg.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"font-weight: bold; text-align: center;", None))
        self.lblBox.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"border: none;", None))
        self.btnModeUpdateHistory.setText(QCoreApplication.translate("EmployeeWindow", u"update history", None))
        self.btnModeUpdateHistory.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"text-align: center; font-size: 16px;", None))
        self.btnModeChangeData.setText(QCoreApplication.translate("EmployeeWindow", u"change data", None))
        self.btnModeChangeData.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"text-align: center; font-size: 16px;", None))
        self.lblDetails.setText(QCoreApplication.translate("EmployeeWindow", u"id: <...>\n"
"\n"
"creation date: ...\n"
"sender: ...\n"
"recipient: ...\n"
"address: ...\n"
"current status: ...", None))
        self.lblHTitle.setText(QCoreApplication.translate("EmployeeWindow", u"history", None))
        self.lblHTitle.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"font-weight: bold;", None))
        self.txtHistory.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"border: none;", None))
        self.txtHistory.setPlainText(QCoreApplication.translate("EmployeeWindow", u"date update: ...\n"
"location type: ...\n"
"adress: ...\n"
"status: ...\n"
"\n"
"date update: ...\n"
"location type: ...", None))
        self.lblUpdHistoryFields.setText(QCoreApplication.translate("EmployeeWindow", u"ID: <...>\n"
"\n"
"\n"
"date: <auto>\n"
"location type: ...\n"
"adress: ...\n"
"status: ...", None))
        self.btnSubmitHistory.setText(QCoreApplication.translate("EmployeeWindow", u"update", None))
        self.btnSubmitHistory.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { font-weight: bold; text-align: center; font-size: 16px; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.lblChgDataFields.setText(QCoreApplication.translate("EmployeeWindow", u"ID: <...>\n"
"\n"
"creation date: ...\n"
"sender: ...\n"
"recipient: ...\n"
"address: ...", None))
        self.btnSubmitData.setText(QCoreApplication.translate("EmployeeWindow", u"update", None))
        self.btnSubmitData.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { font-weight: bold; text-align: center; font-size: 16px; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.lblAddBox.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"border: none;", None))
        self.btnAddPackage.setText(QCoreApplication.translate("EmployeeWindow", u"ADD", None))
        self.btnAddPackage.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { font-weight: bold; text-align: center; font-size: 16px; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.lblAddFields.setText(QCoreApplication.translate("EmployeeWindow", u"ID: <auto>\n"
"date create: <auto>\n"
"status: <auto>\n"
"\n"
"\n"
"Package number: ...\n"
"Sender: ...\n"
"Recipient: ...\n"
"Address: ...", None))
        self.lblAddFields.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"font-size: 16px;", None))
        self.lblSuccessMsg.setText(QCoreApplication.translate("EmployeeWindow", u"The <ID> package has been successfully added", None))
        self.lblSuccessMsg.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"font-size: 16px; font-style: italic;", None))
        self.btnAddOk.setText(QCoreApplication.translate("EmployeeWindow", u"OK", None))
        self.btnAddOk.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { font-weight: bold; text-align: center; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.lblSetTitle.setText(QCoreApplication.translate("EmployeeWindow", u"Change account data", None))
        self.lblSetTitle.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"background: #efefef; border: 1px solid black; font-size: 16px;", None))
        self.editSetName.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Name: ...", None))
        self.editSetSecondName.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Second name: ...", None))
        self.editSetUsername.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Username: ...", None))
        self.editSetEmail.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Email: ...", None))
        self.editSetPassword.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"New password:", None))
        self.btnUpdateAccount.setText(QCoreApplication.translate("EmployeeWindow", u"UPDATE", None))
        self.btnUpdateAccount.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { font-weight: bold; text-align: center; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.btnChangeTheme.setText(QCoreApplication.translate("EmployeeWindow", u"Change theme \u21c4", None))
        self.btnChangeTheme.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { background: #efefef; border: 1px solid black; text-align: center; font-size: 16px; } QPushButton:hover { background: #e0e0e0; } QPushButton:pressed { background: #d0d0d0; }", None))
        self.lblLang.setText(QCoreApplication.translate("EmployeeWindow", u"Change language", None))
        self.lblLang.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"background: #efefef; border: 1px solid black; font-size: 16px;", None))
        self.editLang.setText(QCoreApplication.translate("EmployeeWindow", u"Language: EN", None))
        self.btnLangDrop.setText(QCoreApplication.translate("EmployeeWindow", u"\u21e9", None))
        self.btnLangDrop.setStyleSheet(QCoreApplication.translate("EmployeeWindow", u"QPushButton { text-align: center; font-size: 18px; }", None))
    # retranslateUi

