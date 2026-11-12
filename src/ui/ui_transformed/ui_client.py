# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'client.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextBrowser, QVBoxLayout, QWidget)

from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"

class Ui_ClientWindow(object):
    def setupUi(self, ClientWindow):
        if not ClientWindow.objectName():
            ClientWindow.setObjectName(u"ClientWindow")
        ClientWindow.resize(850, 520)
        self.mainLayout = QHBoxLayout(ClientWindow)
        self.mainLayout.setSpacing(0)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebarFrame = QFrame(ClientWindow)
        self.sidebarFrame.setObjectName(u"sidebarFrame")
        self.sidebarFrame.setMinimumSize(QSize(160, 0))
        self.sidebarFrame.setMaximumSize(QSize(160, 16777215))
        self.sidebarLayout = QVBoxLayout(self.sidebarFrame)
        self.sidebarLayout.setObjectName(u"sidebarLayout")
        self.btnCollapse = QPushButton(self.sidebarFrame)
        self.btnCollapse.setObjectName(u"btnCollapse")

        self.sidebarLayout.addWidget(self.btnCollapse)

        self.btnNavFind = QPushButton(self.sidebarFrame)
        self.btnNavFind.setObjectName(u"btnNavFind")

        self.sidebarLayout.addWidget(self.btnNavFind)

        self.btnNavMy = QPushButton(self.sidebarFrame)
        self.btnNavMy.setObjectName(u"btnNavMy")

        self.sidebarLayout.addWidget(self.btnNavMy)

        self.btnNavSettings = QPushButton(self.sidebarFrame)
        self.btnNavSettings.setObjectName(u"btnNavSettings")

        self.sidebarLayout.addWidget(self.btnNavSettings)

        self.vSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebarLayout.addItem(self.vSpacer)

        self.btnLogout = QPushButton(self.sidebarFrame)
        self.btnLogout.setObjectName(u"btnLogout")

        self.sidebarLayout.addWidget(self.btnLogout)


        self.mainLayout.addWidget(self.sidebarFrame)

        self.stackedMain = QStackedWidget(ClientWindow)
        self.stackedMain.setObjectName(u"stackedMain")
        self.pageFind = QWidget()
        self.pageFind.setObjectName(u"pageFind")
        self.findLayout = QVBoxLayout(self.pageFind)
        self.findLayout.setObjectName(u"findLayout")
        self.findLayout.setContentsMargins(20, 20, 20, 20)
        self.searchBarLayout = QHBoxLayout()
        self.searchBarLayout.setObjectName(u"searchBarLayout")
        self.editSearchNumber = QLineEdit(self.pageFind)
        self.editSearchNumber.setObjectName(u"editSearchNumber")
        self.editSearchNumber.setMinimumSize(QSize(0, 36))

        self.searchBarLayout.addWidget(self.editSearchNumber)

        self.btnFind = QPushButton(self.pageFind)
        self.btnFind.setObjectName(u"btnFind")
        self.btnFind.setMinimumSize(QSize(80, 36))

        self.searchBarLayout.addWidget(self.btnFind)


        self.findLayout.addLayout(self.searchBarLayout)

        self.stackedFindResult = QStackedWidget(self.pageFind)
        self.stackedFindResult.setObjectName(u"stackedFindResult")
        self.subPageEmpty = QWidget()
        self.subPageEmpty.setObjectName(u"subPageEmpty")
        self.vboxLayout = QVBoxLayout(self.subPageEmpty)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.boxFrame = QFrame(self.subPageEmpty)
        self.boxFrame.setObjectName(u"boxFrame")

        self.vboxLayout.addWidget(self.boxFrame)

        self.stackedFindResult.addWidget(self.subPageEmpty)
        self.subPageNotFound = QWidget()
        self.subPageNotFound.setObjectName(u"subPageNotFound")
        self.vboxLayout1 = QVBoxLayout(self.subPageNotFound)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.boxFrame1 = QFrame(self.subPageNotFound)
        self.boxFrame1.setObjectName(u"boxFrame1")
        self.vboxLayout2 = QVBoxLayout(self.boxFrame1)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.lblNotFound = QLabel(self.boxFrame1)
        self.lblNotFound.setObjectName(u"lblNotFound")
        self.lblNotFound.setAlignment(Qt.AlignCenter)

        self.vboxLayout2.addWidget(self.lblNotFound)


        self.vboxLayout1.addWidget(self.boxFrame1)

        self.stackedFindResult.addWidget(self.subPageNotFound)
        self.subPageFound = QWidget()
        self.subPageFound.setObjectName(u"subPageFound")
        self.vboxLayout3 = QVBoxLayout(self.subPageFound)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.boxFrame2 = QFrame(self.subPageFound)
        self.boxFrame2.setObjectName(u"boxFrame2")
        self.hboxLayout = QHBoxLayout(self.boxFrame2)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.hboxLayout.setContentsMargins(25, 25, 25, 25)
        self.vboxLayout4 = QVBoxLayout()
        self.vboxLayout4.setObjectName(u"vboxLayout4")
        self.lblBoxIcon = QLabel(self.boxFrame2)
        self.lblBoxIcon.setObjectName(u"lblBoxIcon")
        self.lblBoxIcon.setMinimumSize(QSize(220, 220))
        self.lblBoxIcon.setAlignment(Qt.AlignCenter)
        self.lblBoxIcon.setPixmap(QPixmap(str(ASSETS_DIR / "cube.png")))
        self.lblBoxIcon.setScaledContents(True)

        self.vboxLayout4.addWidget(self.lblBoxIcon)

        self.btnToTrack = QPushButton(self.boxFrame2)
        self.btnToTrack.setObjectName(u"btnToTrack")

        self.vboxLayout4.addWidget(self.btnToTrack)


        self.hboxLayout.addLayout(self.vboxLayout4)

        self.vboxLayout5 = QVBoxLayout()
        self.vboxLayout5.setObjectName(u"vboxLayout5")
        self.lblPackageInfo = QLabel(self.boxFrame2)
        self.lblPackageInfo.setObjectName(u"lblPackageInfo")

        self.vboxLayout5.addWidget(self.lblPackageInfo)

        self.historyFrame = QFrame(self.boxFrame2)
        self.historyFrame.setObjectName(u"historyFrame")
        self.vboxLayout6 = QVBoxLayout(self.historyFrame)
        self.vboxLayout6.setObjectName(u"vboxLayout6")
        self.lblHistHeader = QLabel(self.historyFrame)
        self.lblHistHeader.setObjectName(u"lblHistHeader")
        self.lblHistHeader.setAlignment(Qt.AlignCenter)

        self.vboxLayout6.addWidget(self.lblHistHeader)

        self.txtHistory = QTextBrowser(self.historyFrame)
        self.txtHistory.setObjectName(u"txtHistory")

        self.vboxLayout6.addWidget(self.txtHistory)


        self.vboxLayout5.addWidget(self.historyFrame)


        self.hboxLayout.addLayout(self.vboxLayout5)


        self.vboxLayout3.addWidget(self.boxFrame2)

        self.stackedFindResult.addWidget(self.subPageFound)

        self.findLayout.addWidget(self.stackedFindResult)

        self.stackedMain.addWidget(self.pageFind)
        self.pageMyPackages = QWidget()
        self.pageMyPackages.setObjectName(u"pageMyPackages")
        self.vboxLayout7 = QVBoxLayout(self.pageMyPackages)
        self.vboxLayout7.setObjectName(u"vboxLayout7")
        self.vboxLayout7.setContentsMargins(25, 25, 25, 25)
        self.listMyPackages = QListWidget(self.pageMyPackages)
        icon = QIcon()
        icon.addFile(str(ASSETS_DIR / "cube.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u"", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        __qlistwidgetitem = QListWidgetItem(self.listMyPackages)
        __qlistwidgetitem.setIcon(icon)
        __qlistwidgetitem1 = QListWidgetItem(self.listMyPackages)
        __qlistwidgetitem1.setIcon(icon)
        __qlistwidgetitem2 = QListWidgetItem(self.listMyPackages)
        __qlistwidgetitem2.setIcon(icon)
        self.listMyPackages.setObjectName(u"listMyPackages")
        self.listMyPackages.setIconSize(QSize(42, 42))

        self.vboxLayout7.addWidget(self.listMyPackages)

        self.stackedMain.addWidget(self.pageMyPackages)
        self.pageSettings = QWidget()
        self.pageSettings.setObjectName(u"pageSettings")
        self.vboxLayout8 = QVBoxLayout(self.pageSettings)
        self.vboxLayout8.setObjectName(u"vboxLayout8")
        self.vboxLayout8.setContentsMargins(25, 25, 25, 25)
        self.settingsBox = QFrame(self.pageSettings)
        self.settingsBox.setObjectName(u"settingsBox")
        self.vboxLayout9 = QVBoxLayout(self.settingsBox)
        self.vboxLayout9.setObjectName(u"vboxLayout9")
        self.vboxLayout9.setContentsMargins(15, 15, 15, 15)
        self.lblSetTitle = QLabel(self.settingsBox)
        self.lblSetTitle.setObjectName(u"lblSetTitle")
        self.lblSetTitle.setMinimumSize(QSize(0, 36))
        self.lblSetTitle.setAlignment(Qt.AlignCenter)

        self.vboxLayout9.addWidget(self.lblSetTitle)

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


        self.vboxLayout9.addLayout(self.gridLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.editSetPassword = QLineEdit(self.settingsBox)
        self.editSetPassword.setObjectName(u"editSetPassword")

        self.hboxLayout1.addWidget(self.editSetPassword)

        self.btnUpdateAccount = QPushButton(self.settingsBox)
        self.btnUpdateAccount.setObjectName(u"btnUpdateAccount")
        self.btnUpdateAccount.setMinimumSize(QSize(220, 34))

        self.hboxLayout1.addWidget(self.btnUpdateAccount)


        self.vboxLayout9.addLayout(self.hboxLayout1)

        self.btnChangeTheme = QPushButton(self.settingsBox)
        self.btnChangeTheme.setObjectName(u"btnChangeTheme")
        self.btnChangeTheme.setMinimumSize(QSize(0, 36))

        self.vboxLayout9.addWidget(self.btnChangeTheme)

        self.lblLang = QLabel(self.settingsBox)
        self.lblLang.setObjectName(u"lblLang")
        self.lblLang.setMinimumSize(QSize(0, 36))
        self.lblLang.setAlignment(Qt.AlignCenter)

        self.vboxLayout9.addWidget(self.lblLang)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.editLang = QLineEdit(self.settingsBox)
        self.editLang.setObjectName(u"editLang")
        self.editLang.setReadOnly(True)

        self.hboxLayout2.addWidget(self.editLang)

        self.btnLangDrop = QPushButton(self.settingsBox)
        self.btnLangDrop.setObjectName(u"btnLangDrop")
        self.btnLangDrop.setMaximumSize(QSize(60, 34))

        self.hboxLayout2.addWidget(self.btnLangDrop)


        self.vboxLayout9.addLayout(self.hboxLayout2)

        self.vSpSet = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vboxLayout9.addItem(self.vSpSet)


        self.vboxLayout8.addWidget(self.settingsBox)

        self.stackedMain.addWidget(self.pageSettings)

        self.mainLayout.addWidget(self.stackedMain)


        self.retranslateUi(ClientWindow)

        QMetaObject.connectSlotsByName(ClientWindow)
    # setupUi

    def retranslateUi(self, ClientWindow):
        ClientWindow.setWindowTitle(QCoreApplication.translate("ClientWindow", u"Client Panel", None))
        ClientWindow.setStyleSheet(QCoreApplication.translate("ClientWindow", u"QWidget { background: white; color: black; font-family: Arial; font-size: 14px; } QLineEdit { border: 1px solid black; padding: 6px; } QPushButton { border: 1px solid black; background: white; padding: 8px; text-align: left; } QPushButton:hover { background-color: #f2f2f2; } QPushButton:pressed { background-color: #e6e6e6; } QFrame#sidebarFrame { border-right: 1px solid black; } QFrame#boxFrame, QFrame#historyFrame, QFrame#settingsBox { border: 1px solid black; }", None))
        self.btnCollapse.setText(QCoreApplication.translate("ClientWindow", u"\u2630  collapse", None))
        self.btnNavFind.setText(QCoreApplication.translate("ClientWindow", u"\u25a1  find package", None))
        self.btnNavFind.setStyleSheet(QCoreApplication.translate("ClientWindow", u"QPushButton { background: #f5c28b; } QPushButton:hover { background: #f0b06a; }", None))
        self.btnNavMy.setText(QCoreApplication.translate("ClientWindow", u"\u25a1  my package", None))
        self.btnNavSettings.setText(QCoreApplication.translate("ClientWindow", u"\u25cb  settings", None))
        self.btnLogout.setText(QCoreApplication.translate("ClientWindow", u"log out", None))
        self.btnLogout.setStyleSheet(QCoreApplication.translate("ClientWindow", u"border: none; font-style: italic; text-align: center;", None))
        self.editSearchNumber.setText(QCoreApplication.translate("ClientWindow", u"123456", None))
        self.btnFind.setText(QCoreApplication.translate("ClientWindow", u"FIND", None))
        self.btnFind.setStyleSheet(QCoreApplication.translate("ClientWindow", u"font-weight: bold; text-align: center;", None))
        self.lblNotFound.setText(QCoreApplication.translate("ClientWindow", u"NOT FOUND", None))
        self.lblNotFound.setStyleSheet(QCoreApplication.translate("ClientWindow", u"font-size: 28px; font-style: italic;", None))
        self.lblBoxIcon.setStyleSheet(QCoreApplication.translate("ClientWindow", u"border: none;", None))
        self.btnToTrack.setText(QCoreApplication.translate("ClientWindow", u"to track", None))
        self.btnToTrack.setStyleSheet(QCoreApplication.translate("ClientWindow", u"text-align: center; font-size: 16px;", None))
        self.lblPackageInfo.setText(QCoreApplication.translate("ClientWindow", u"id: ...\n"
"\n"
"creation date: ...\n"
"sender: ...\n"
"current status: ...", None))
        self.lblHistHeader.setText(QCoreApplication.translate("ClientWindow", u"history", None))
        self.lblHistHeader.setStyleSheet(QCoreApplication.translate("ClientWindow", u"font-weight: bold;", None))
        self.txtHistory.setStyleSheet(QCoreApplication.translate("ClientWindow", u"border: none;", None))
        self.txtHistory.setPlainText(QCoreApplication.translate("ClientWindow", u"date update: ...\n"
"location type: ...\n"
"adress: ...\n"
"status: ...\n"
"\n"
"date update: ...\n"
"location type: ...", None))

        __sortingEnabled = self.listMyPackages.isSortingEnabled()
        self.listMyPackages.setSortingEnabled(False)
        ___qlistwidgetitem = self.listMyPackages.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ClientWindow", u"   ID ...\n"
"       create date ...", None))
        ___qlistwidgetitem1 = self.listMyPackages.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("ClientWindow", u"   ID ...\n"
"       create date ...", None))
        ___qlistwidgetitem2 = self.listMyPackages.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("ClientWindow", u"   ID ...\n"
"       create date ...", None))
        self.listMyPackages.setSortingEnabled(__sortingEnabled)

        self.listMyPackages.setStyleSheet(QCoreApplication.translate("ClientWindow", u"QListWidget { border: 1px solid black; padding: 15px; font-size: 16px; } QListWidget::item { padding: 12px; }", None))
        self.lblSetTitle.setText(QCoreApplication.translate("ClientWindow", u"Change account data", None))
        self.lblSetTitle.setStyleSheet(QCoreApplication.translate("ClientWindow", u"background: #efefef; border: 1px solid black; font-size: 16px;", None))
        self.editSetName.setPlaceholderText(QCoreApplication.translate("ClientWindow", u"Name: ...", None))
        self.editSetSecondName.setPlaceholderText(QCoreApplication.translate("ClientWindow", u"Second name: ...", None))
        self.editSetUsername.setPlaceholderText(QCoreApplication.translate("ClientWindow", u"Username: ...", None))
        self.editSetEmail.setPlaceholderText(QCoreApplication.translate("ClientWindow", u"Email: ...", None))
        self.editSetPassword.setPlaceholderText(QCoreApplication.translate("ClientWindow", u"New password:", None))
        self.btnUpdateAccount.setText(QCoreApplication.translate("ClientWindow", u"UPDATE", None))
        self.btnUpdateAccount.setStyleSheet(QCoreApplication.translate("ClientWindow", u"QPushButton { font-weight: bold; text-align: center; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.btnChangeTheme.setText(QCoreApplication.translate("ClientWindow", u"Change theme \u21c4", None))
        self.btnChangeTheme.setStyleSheet(QCoreApplication.translate("ClientWindow", u"QPushButton { background: #efefef; border: 1px solid black; text-align: center; font-size: 16px; } QPushButton:hover { background: #e0e0e0; } QPushButton:pressed { background: #d0d0d0; }", None))
        self.lblLang.setText(QCoreApplication.translate("ClientWindow", u"Change language", None))
        self.lblLang.setStyleSheet(QCoreApplication.translate("ClientWindow", u"background: #efefef; border: 1px solid black; font-size: 16px;", None))
        self.editLang.setText(QCoreApplication.translate("ClientWindow", u"Language: EN", None))
        self.btnLangDrop.setText(QCoreApplication.translate("ClientWindow", u"\u21e9", None))
        self.btnLangDrop.setStyleSheet(QCoreApplication.translate("ClientWindow", u"QPushButton { text-align: center; font-size: 18px; }", None))
    # retranslateUi

