# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\\guiPages\\emailPopUp.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from main import resource_path

class Ui_emailPopUp(object):
    def setupUi(self, emailPopUp):
        emailPopUp.setObjectName("emailPopUp")
        emailPopUp.resize(400, 250)
        emailPopUp.setStyleSheet("background-color: rgb(196, 236, 236);")
        self.emailPopUp_2 = QtWidgets.QFrame(emailPopUp)
        self.emailPopUp_2.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.emailPopUp_2.setMaximumSize(QtCore.QSize(500, 600))
        self.emailPopUp_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emailPopUp_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emailPopUp_2.setObjectName("emailPopUp_2")
        self.logoButton = QtWidgets.QPushButton(self.emailPopUp_2, clicked=lambda: self.logoButtonClicked())
        self.logoButton.setGeometry(QtCore.QRect(165, 40, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setUnderline(False)
        self.logoButton.setFont(font)
        self.logoButton.setStyleSheet("background-color: rgb(244, 249, 250);\n"
"border: none;\n"
"color: black;")
        self.logoButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("./images/icon_blueBackground.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoButton.setIcon(icon)
        self.logoButton.setIconSize(QtCore.QSize(90, 90))
        self.logoButton.setObjectName("logoButton")
        self.frame = QtWidgets.QFrame(self.emailPopUp_2)
        self.frame.setGeometry(QtCore.QRect(0, 119, 400, 60))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(210, 15, 150, 30))
        self.textEdit.setStyleSheet("font: 13pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(40, 15, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 700 20pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.emailPopUp_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 190, 100, 30))
        self.pushButton.setStyleSheet("background-color: rgb(77, 206, 175);\n"
"font: 18pt \"Arial\";\n"
"border: none;")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(emailPopUp)
        QtCore.QMetaObject.connectSlotsByName(emailPopUp)

    def retranslateUi(self, emailPopUp):
        _translate = QtCore.QCoreApplication.translate
        emailPopUp.setWindowTitle(_translate("emailPopUp", "Form"))
        self.textEdit.setHtml(_translate("emailPopUp", "<!DOCTYPE HTML PUBLIC \"-\\\\W3C\\\\DTD HTML 4.0\\\\EN\" \"http:\\\\www.w3.org\\TR\\REC-html40\\strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" \\><meta charset=\"utf-8\" \\><style type=\"text\\css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"<\\style><\\head><body style=\" font-family:\'Arial\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br \\><\\p><\\body><\\html>"))
        self.label.setText(_translate("emailPopUp", "Email:"))
        self.pushButton.setText(_translate("emailPopUp", "Send"))

    def pushButtonClicked(self, downloadPopUp):
        downloadPopUp.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    emailPopUp = QtWidgets.QWidget()
    ui = Ui_emailPopUp()
    ui.setupUi(emailPopUp)
    emailPopUp.show()
    sys.exit(app.exec_())