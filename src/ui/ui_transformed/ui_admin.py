# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
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
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        if not AdminWindow.objectName():
            AdminWindow.setObjectName(u"AdminWindow")
        AdminWindow.resize(850, 520)
        self.mainLayout = QHBoxLayout(AdminWindow)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(AdminWindow)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(160, 0))
        self.sidebarFrame.setMaximumSize(QSize(160, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.btnCollapse = QPushButton(self.sidebarFrame)
        self.btnCollapse.setObjectName(u"btnCollapse")

        self.sidebarLayout.addWidget(self.btnCollapse)

        self.btnNavUsers = QPushButton(self.sidebarFrame)
        self.btnNavUsers.setObjectName(u"btnNavUsers")

        self.sidebarLayout.addWidget(self.btnNavUsers)

        self.btnNavSettings = QPushButton(self.sidebarFrame)
        self.btnNavSettings.setObjectName(u"btnNavSettings")

        self.sidebarLayout.addWidget(self.btnNavSettings)

        self.vSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.vSpacer)

        self.btnLogout = QPushButton(self.sidebarFrame)
        self.btnLogout.setObjectName(u"btnLogout")

        self.sidebarLayout.addWidget(self.btnLogout)


        self.mainLayout.addWidget(self.sidebarFrame)

        self.stackedMain = QStackedWidget(AdminWindow)
        self.stackedMain.setObjectName(u"stackedMain")
        self.pageUsers = QWidget()
        self.pageUsers.setObjectName(u"pageUsers")
        self.vboxLayout = QVBoxLayout(self.pageUsers)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(20, 20, 20, 20)
        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.editSearchUser = QLineEdit(self.pageUsers)
        self.editSearchUser.setObjectName(u"editSearchUser")
        self.editSearchUser.setMinimumSize(QSize(0, 36))

        self.hboxLayout.addWidget(self.editSearchUser)

        self.btnFindUser = QPushButton(self.pageUsers)
        self.btnFindUser.setObjectName(u"btnFindUser")
        self.btnFindUser.setMinimumSize(QSize(80, 36))

        self.hboxLayout.addWidget(self.btnFindUser)


        self.vboxLayout.addLayout(self.hboxLayout)

        self.stackedUserResult = QStackedWidget(self.pageUsers)
        self.stackedUserResult.setObjectName(u"stackedUserResult")
        self.subNoUser = QWidget()
        self.subNoUser.setObjectName(u"subNoUser")
        self.vboxLayout1 = QVBoxLayout(self.subNoUser)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.userCard = QFrame(self.subNoUser)
        self.userCard.setObjectName(u"userCard")
        self.vboxLayout2 = QVBoxLayout(self.userCard)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.lblNoUser = QLabel(self.userCard)
        self.lblNoUser.setObjectName(u"lblNoUser")
        self.lblNoUser.setAlignment(Qt.AlignCenter)

        self.vboxLayout2.addWidget(self.lblNoUser)


        self.vboxLayout1.addWidget(self.userCard)

        self.stackedUserResult.addWidget(self.subNoUser)
        self.subUserFound = QWidget()
        self.subUserFound.setObjectName(u"subUserFound")
        self.vboxLayout3 = QVBoxLayout(self.subUserFound)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.userCard1 = QFrame(self.subUserFound)
        self.userCard1.setObjectName(u"userCard1")
        self.hboxLayout1 = QHBoxLayout(self.userCard1)
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.hboxLayout1.setContentsMargins(25, 25, 25, 25)
        self.lblAvatar = QLabel(self.userCard1)
        self.lblAvatar.setObjectName(u"lblAvatar")
        self.lblAvatar.setMinimumSize(QSize(200, 260))
        self.lblAvatar.setAlignment(Qt.AlignCenter)
        self.lblAvatar.setPixmap(QPixmap(str(ASSETS_DIR / "stickman.png")))
        self.lblAvatar.setScaledContents(True)

        self.hboxLayout1.addWidget(self.lblAvatar)

        self.vboxLayout4 = QVBoxLayout()
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.lblUserInfo = QLabel(self.userCard1)
        self.lblUserInfo.setObjectName(u"lblUserInfo")

        self.vboxLayout4.addWidget(self.lblUserInfo)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.btnRoleAdmin = QPushButton(self.userCard1)
        self.btnRoleAdmin.setObjectName(u"btnRoleAdmin")

        self.hboxLayout2.addWidget(self.btnRoleAdmin)

        self.btnRoleClient = QPushButton(self.userCard1)
        self.btnRoleClient.setObjectName(u"btnRoleClient")

        self.hboxLayout2.addWidget(self.btnRoleClient)

        self.btnRoleEmployee = QPushButton(self.userCard1)
        self.btnRoleEmployee.setObjectName(u"btnRoleEmployee")

        self.hboxLayout2.addWidget(self.btnRoleEmployee)


        self.vboxLayout4.addLayout(self.hboxLayout2)


        self.hboxLayout1.addLayout(self.vboxLayout4)


        self.vboxLayout3.addWidget(self.userCard1)

        self.stackedUserResult.addWidget(self.subUserFound)

        self.vboxLayout.addWidget(self.stackedUserResult)

        self.stackedMain.addWidget(self.pageUsers)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.vboxLayout5 = QVBoxLayout(self.pageSettings)
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.vboxLayout5.setContentsMargins(25, 25, 25, 25)
        self.settingsBox = QFrame(self.pageSettings)
        self.settingsBox.setObjectName(u"settingsBox")
        self.vboxLayout6 = QVBoxLayout(self.settingsBox)
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.vboxLayout6.setContentsMargins(15, 15, 15, 15)
        self.lblSetTitle = QLabel(self.settingsBox)
        self.lblSetTitle.setObjectName(u"lblSetTitle")
        self.lblSetTitle.setMinimumSize(QSize(0, 36))
        self.lblSetTitle.setAlignment(Qt.AlignCenter)

        self.vboxLayout6.addWidget(self.lblSetTitle)

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


        self.vboxLayout6.addLayout(self.gridLayout)

        self.hboxLayout3 = QHBoxLayout()
        self.hboxLayout3.setObjectName(u"hboxLayout3")
        self.editSetPassword = QLineEdit(self.settingsBox)
        self.editSetPassword.setObjectName(u"editSetPassword")

        self.hboxLayout3.addWidget(self.editSetPassword)

        self.btnUpdateAccount = QPushButton(self.settingsBox)
        self.btnUpdateAccount.setObjectName(u"btnUpdateAccount")
        self.btnUpdateAccount.setMinimumSize(QSize(220, 34))

        self.hboxLayout3.addWidget(self.btnUpdateAccount)


        self.vboxLayout6.addLayout(self.hboxLayout3)

        self.btnChangeTheme = QPushButton(self.settingsBox)
        self.btnChangeTheme.setObjectName(u"btnChangeTheme")
        self.btnChangeTheme.setMinimumSize(QSize(0, 36))

        self.vboxLayout6.addWidget(self.btnChangeTheme)

        self.lblLang = QLabel(self.settingsBox)
        self.lblLang.setObjectName(u"lblLang")
        self.lblLang.setMinimumSize(QSize(0, 36))
        self.lblLang.setAlignment(Qt.AlignCenter)

        self.vboxLayout6.addWidget(self.lblLang)

        self.hboxLayout4 = QHBoxLayout()
        self.hboxLayout4.setObjectName(u"hboxLayout4")
        self.editLang = QLineEdit(self.settingsBox)
        self.editLang.setObjectName(u"editLang")
        self.editLang.setReadOnly(True)

        self.hboxLayout4.addWidget(self.editLang)

        self.btnLangDrop = QPushButton(self.settingsBox)
        self.btnLangDrop.setObjectName(u"btnLangDrop")
        self.btnLangDrop.setMaximumSize(QSize(60, 34))

        self.hboxLayout4.addWidget(self.btnLangDrop)


        self.vboxLayout6.addLayout(self.hboxLayout4)

        self.vSpSet = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout6.addItem(self.vSpSet)


        self.vboxLayout5.addWidget(self.settingsBox)

        self.stackedMain.addWidget(self.pageSettings)

        self.mainLayout.addWidget(self.stackedMain)


        self.retranslateUi(AdminWindow)

        QMetaObject.connectSlotsByName(AdminWindow)
    # setupUi

    def retranslateUi(self, AdminWindow):
        AdminWindow.setWindowTitle(QCoreApplication.translate("AdminWindow", u"Admin Panel", None))
        AdminWindow.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QWidget { background: white; color: black; font-family: Arial; font-size: 14px; } QLineEdit { border: 1px solid black; padding: 6px; } QPushButton { border: 1px solid black; background: white; padding: 8px; text-align: left; } QPushButton:hover { background-color: #f2f2f2; } QPushButton:pressed { background-color: #e6e6e6; } QFrame#sidebarFrame { border-right: 1px solid black; } QFrame#userCard, QFrame#settingsBox { border: 1px solid black; }", None))
        self.btnCollapse.setText(QCoreApplication.translate("AdminWindow", u"\u2630  collapse", None))
        self.btnNavUsers.setText(QCoreApplication.translate("AdminWindow", u"\u25a1  users", None))
        self.btnNavUsers.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { background: #f5c28b; } QPushButton:hover { background: #f0b06a; }", None))
        self.btnNavSettings.setText(QCoreApplication.translate("AdminWindow", u"\u25cb  settings", None))
        self.btnLogout.setText(QCoreApplication.translate("AdminWindow", u"log out", None))
        self.btnLogout.setStyleSheet(QCoreApplication.translate("AdminWindow", u"border: none; font-style: italic; text-align: center;", None))
        self.editSearchUser.setText(QCoreApplication.translate("AdminWindow", u"123456", None))
        self.btnFindUser.setText(QCoreApplication.translate("AdminWindow", u"FIND", None))
        self.btnFindUser.setStyleSheet(QCoreApplication.translate("AdminWindow", u"font-weight: bold; text-align: center;", None))
        self.lblNoUser.setText(QCoreApplication.translate("AdminWindow", u"NO USER", None))
        self.lblNoUser.setStyleSheet(QCoreApplication.translate("AdminWindow", u"font-size: 24px; font-weight: bold;", None))
        self.lblAvatar.setStyleSheet(QCoreApplication.translate("AdminWindow", u"border: none;", None))
        self.lblUserInfo.setText(QCoreApplication.translate("AdminWindow", u"id: <...>\n"
"\n"
"username: <...>\n"
"name: <...>\n"
"second name: <...>\n"
"email: <...>", None))
        self.lblUserInfo.setStyleSheet(QCoreApplication.translate("AdminWindow", u"font-size: 16px;", None))
        self.btnRoleAdmin.setText(QCoreApplication.translate("AdminWindow", u"admin", None))
        self.btnRoleAdmin.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { font-weight: bold; text-align: center; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.btnRoleClient.setText(QCoreApplication.translate("AdminWindow", u"client", None))
        self.btnRoleClient.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { background: #b8d4f2; font-weight: bold; text-align: center; } QPushButton:hover { background: #a3c6eb; }", None))
        self.btnRoleEmployee.setText(QCoreApplication.translate("AdminWindow", u"employee", None))
        self.btnRoleEmployee.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { font-weight: bold; text-align: center; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.lblSetTitle.setText(QCoreApplication.translate("AdminWindow", u"Change account data", None))
        self.lblSetTitle.setStyleSheet(QCoreApplication.translate("AdminWindow", u"background: #efefef; border: 1px solid black; font-size: 16px;", None))
        self.editSetName.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Name: ...", None))
        self.editSetSecondName.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Second name: ...", None))
        self.editSetUsername.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Username: ...", None))
        self.editSetEmail.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"Email: ...", None))
        self.editSetPassword.setPlaceholderText(QCoreApplication.translate("AdminWindow", u"New password:", None))
        self.btnUpdateAccount.setText(QCoreApplication.translate("AdminWindow", u"UPDATE", None))
        self.btnUpdateAccount.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { font-weight: bold; text-align: center; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.btnChangeTheme.setText(QCoreApplication.translate("AdminWindow", u"Change theme \u21c4", None))
        self.btnChangeTheme.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { background: #efefef; border: 1px solid black; text-align: center; font-size: 16px; } QPushButton:hover { background: #e0e0e0; } QPushButton:pressed { background: #d0d0d0; }", None))
        self.lblLang.setText(QCoreApplication.translate("AdminWindow", u"Change language", None))
        self.lblLang.setStyleSheet(QCoreApplication.translate("AdminWindow", u"background: #efefef; border: 1px solid black; font-size: 16px;", None))
        self.editLang.setText(QCoreApplication.translate("AdminWindow", u"Language: EN", None))
        self.btnLangDrop.setText(QCoreApplication.translate("AdminWindow", u"\u21e9", None))
        self.btnLangDrop.setStyleSheet(QCoreApplication.translate("AdminWindow", u"QPushButton { text-align: center; font-size: 18px; }", None))
    # retranslateUi

