# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(600, 400)
        self.mainLayout = QHBoxLayout(LoginWindow)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(50, 50, 50, 50)
        self.formLayout = QVBoxLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lblUser = QLabel(LoginWindow)
        self.lblUser.setObjectName(u"lblUser")
        self.lblUser.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.lblUser)

        self.editUsername = QLineEdit(LoginWindow)
        self.editUsername.setObjectName(u"editUsername")

        self.formLayout.addWidget(self.editUsername)

        self.lblPass = QLabel(LoginWindow)
        self.lblPass.setObjectName(u"lblPass")
        self.lblPass.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.lblPass)

        self.editPassword = QLineEdit(LoginWindow)
        self.editPassword.setObjectName(u"editPassword")

        self.formLayout.addWidget(self.editPassword)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.chkRemember = QCheckBox(LoginWindow)
        self.chkRemember.setObjectName(u"chkRemember")

        self.bottomLayout.addWidget(self.chkRemember)

        self.hSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottomLayout.addItem(self.hSpacer)

        self.btnLogin = QPushButton(LoginWindow)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setMinimumSize(QSize(120, 50))

        self.bottomLayout.addWidget(self.btnLogin)


        self.formLayout.addLayout(self.bottomLayout)


        self.mainLayout.addLayout(self.formLayout)

        self.switchLayout = QVBoxLayout()
        self.switchLayout.setSpacing(0)
        self.switchLayout.setObjectName(u"switchLayout")
        self.btnGoReg = QPushButton(LoginWindow)
        self.btnGoReg.setObjectName(u"btnGoReg")
        self.btnGoReg.setMaximumSize(QSize(40, 80))

        self.switchLayout.addWidget(self.btnGoReg)

        self.btnGoLog = QPushButton(LoginWindow)
        self.btnGoLog.setObjectName(u"btnGoLog")
        self.btnGoLog.setMaximumSize(QSize(40, 80))

        self.switchLayout.addWidget(self.btnGoLog)


        self.mainLayout.addLayout(self.switchLayout)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        LoginWindow.setStyleSheet(QCoreApplication.translate("LoginWindow", u"QWidget { background: white; color: black; font-family: Arial; font-size: 14px; } QLineEdit { border: 1px solid black; padding: 6px; font-family: monospace; font-size: 16px; } QPushButton { border: 1px solid black; background: white; padding: 8px; font-weight: bold; } QPushButton:hover { background-color: #f2f2f2; } QPushButton:pressed { background-color: #e6e6e6; }", None))
        self.lblUser.setText(QCoreApplication.translate("LoginWindow", u"username", None))
        self.lblUser.setStyleSheet(QCoreApplication.translate("LoginWindow", u"font-size: 20px; font-family: monospace;", None))
        self.editUsername.setText(QCoreApplication.translate("LoginWindow", u"degus_admin", None))
        self.lblPass.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.lblPass.setStyleSheet(QCoreApplication.translate("LoginWindow", u"font-size: 20px; font-family: monospace;", None))
        self.editPassword.setText(QCoreApplication.translate("LoginWindow", u"*******", None))
        self.chkRemember.setText(QCoreApplication.translate("LoginWindow", u"Remember me", None))
        self.btnLogin.setText(QCoreApplication.translate("LoginWindow", u"LOG IN", None))
        self.btnLogin.setStyleSheet(QCoreApplication.translate("LoginWindow", u"QPushButton { font-weight: bold; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.btnGoReg.setText(QCoreApplication.translate("LoginWindow", u"R\n"
"E\n"
"G", None))
        self.btnGoReg.setStyleSheet(QCoreApplication.translate("LoginWindow", u"QPushButton { background: white; color: black; border: 1px solid black; } QPushButton:hover { background: #f2f2f2; }", None))
        self.btnGoLog.setText(QCoreApplication.translate("LoginWindow", u"L\n"
"O\n"
"G", None))
        self.btnGoLog.setStyleSheet(QCoreApplication.translate("LoginWindow", u"QPushButton { background: black; color: white; border: 1px solid black; } QPushButton:hover { background: #333333; }", None))
    # retranslateUi

