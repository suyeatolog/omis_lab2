# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(600, 620)
        self.mainLayout = QHBoxLayout(RegisterWindow)
        self.mainLayout.setObjectName(u"mainLayout")
        self.mainLayout.setContentsMargins(30, 30, 30, 30)
        self.formLayout = QVBoxLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.l1 = QLabel(RegisterWindow)
        self.l1.setObjectName(u"l1")
        self.l1.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.l1)

        self.editUsername = QLineEdit(RegisterWindow)
        self.editUsername.setObjectName(u"editUsername")

        self.formLayout.addWidget(self.editUsername)

        self.l2 = QLabel(RegisterWindow)
        self.l2.setObjectName(u"l2")
        self.l2.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.l2)

        self.editEmail = QLineEdit(RegisterWindow)
        self.editEmail.setObjectName(u"editEmail")

        self.formLayout.addWidget(self.editEmail)

        self.l3 = QLabel(RegisterWindow)
        self.l3.setObjectName(u"l3")
        self.l3.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.l3)

        self.editName = QLineEdit(RegisterWindow)
        self.editName.setObjectName(u"editName")

        self.formLayout.addWidget(self.editName)

        self.l4 = QLabel(RegisterWindow)
        self.l4.setObjectName(u"l4")
        self.l4.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.l4)

        self.editSecondName = QLineEdit(RegisterWindow)
        self.editSecondName.setObjectName(u"editSecondName")

        self.formLayout.addWidget(self.editSecondName)

        self.l5 = QLabel(RegisterWindow)
        self.l5.setObjectName(u"l5")
        self.l5.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.l5)

        self.editPassword = QLineEdit(RegisterWindow)
        self.editPassword.setObjectName(u"editPassword")

        self.formLayout.addWidget(self.editPassword)

        self.l6 = QLabel(RegisterWindow)
        self.l6.setObjectName(u"l6")
        self.l6.setAlignment(Qt.AlignCenter)

        self.formLayout.addWidget(self.l6)

        self.editPasswordAgain = QLineEdit(RegisterWindow)
        self.editPasswordAgain.setObjectName(u"editPasswordAgain")

        self.formLayout.addWidget(self.editPasswordAgain)

        self.bottomLayout = QHBoxLayout()
        self.bottomLayout.setObjectName(u"bottomLayout")
        self.chkRemember = QCheckBox(RegisterWindow)
        self.chkRemember.setObjectName(u"chkRemember")

        self.bottomLayout.addWidget(self.chkRemember)

        self.hSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.bottomLayout.addItem(self.hSpacer)

        self.btnRegister = QPushButton(RegisterWindow)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setMinimumSize(QSize(120, 45))

        self.bottomLayout.addWidget(self.btnRegister)


        self.formLayout.addLayout(self.bottomLayout)


        self.mainLayout.addLayout(self.formLayout)

        self.switchLayout = QVBoxLayout()
        self.switchLayout.setSpacing(0)
        self.switchLayout.setObjectName(u"switchLayout")
        self.btnGoReg = QPushButton(RegisterWindow)
        self.btnGoReg.setObjectName(u"btnGoReg")
        self.btnGoReg.setMaximumSize(QSize(40, 80))

        self.switchLayout.addWidget(self.btnGoReg)

        self.btnGoLog = QPushButton(RegisterWindow)
        self.btnGoLog.setObjectName(u"btnGoLog")
        self.btnGoLog.setMaximumSize(QSize(40, 80))

        self.switchLayout.addWidget(self.btnGoLog)

        self.vSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.switchLayout.addItem(self.vSpacer)


        self.mainLayout.addLayout(self.switchLayout)


        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"Registration", None))
        RegisterWindow.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"QWidget { background: white; color: black; font-family: Arial; font-size: 14px; } QLineEdit { border: 1px solid black; padding: 6px; font-family: monospace; font-size: 15px; } QPushButton { border: 1px solid black; background: white; padding: 8px; font-weight: bold; } QPushButton:hover { background-color: #f2f2f2; } QPushButton:pressed { background-color: #e6e6e6; }", None))
        self.l1.setText(QCoreApplication.translate("RegisterWindow", u"username", None))
        self.l1.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"font-size: 18px; font-family: monospace;", None))
        self.editUsername.setText(QCoreApplication.translate("RegisterWindow", u"degus_admin", None))
        self.l2.setText(QCoreApplication.translate("RegisterWindow", u"email", None))
        self.l2.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"font-size: 18px; font-family: monospace;", None))
        self.editEmail.setText(QCoreApplication.translate("RegisterWindow", u"degus@gmail.com", None))
        self.l3.setText(QCoreApplication.translate("RegisterWindow", u"name", None))
        self.l3.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"font-size: 18px; font-family: monospace;", None))
        self.editName.setText(QCoreApplication.translate("RegisterWindow", u"de", None))
        self.l4.setText(QCoreApplication.translate("RegisterWindow", u"second name", None))
        self.l4.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"font-size: 18px; font-family: monospace;", None))
        self.editSecondName.setText(QCoreApplication.translate("RegisterWindow", u"gus", None))
        self.l5.setText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.l5.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"font-size: 18px; font-family: monospace;", None))
        self.editPassword.setText(QCoreApplication.translate("RegisterWindow", u"*******", None))
        self.l6.setText(QCoreApplication.translate("RegisterWindow", u"Password again", None))
        self.l6.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"font-size: 18px; font-family: monospace;", None))
        self.editPasswordAgain.setText(QCoreApplication.translate("RegisterWindow", u"*******", None))
        self.chkRemember.setText(QCoreApplication.translate("RegisterWindow", u"Remember me", None))
        self.btnRegister.setText(QCoreApplication.translate("RegisterWindow", u"Regisration", None))
        self.btnRegister.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"QPushButton { font-weight: bold; } QPushButton:hover { background-color: #fce0c5; }", None))
        self.btnGoReg.setText(QCoreApplication.translate("RegisterWindow", u"R\n"
"E\n"
"G", None))
        self.btnGoReg.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"QPushButton { background: black; color: white; border: 1px solid black; } QPushButton:hover { background: #333333; }", None))
        self.btnGoLog.setText(QCoreApplication.translate("RegisterWindow", u"L\n"
"O\n"
"G", None))
        self.btnGoLog.setStyleSheet(QCoreApplication.translate("RegisterWindow", u"QPushButton { background: white; color: black; border: 1px solid black; } QPushButton:hover { background: #f2f2f2; }", None))
    # retranslateUi

