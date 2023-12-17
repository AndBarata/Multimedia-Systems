# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../guiPages/endingwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EndingWindow(object):
    stars = 0 # display variable
    def setupUi(self, EndingWindow, initialWindow):
        EndingWindow.setObjectName("EndingWindow")
        EndingWindow.resize(600, 400)
        EndingWindow.setStyleSheet("background-color: rgb(244, 249, 250);")
        self.EndingWindow_frame = QtWidgets.QFrame(EndingWindow)
        self.EndingWindow_frame.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.EndingWindow_frame.setStyleSheet("background-color: rgb(244, 249, 250);")
        self.EndingWindow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.EndingWindow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.EndingWindow_frame.setObjectName("EndingWindow_frame")
        self.readyLable = QtWidgets.QLabel(self.EndingWindow_frame)
        self.readyLable.setGeometry(QtCore.QRect(200, 20, 200, 50))
        self.readyLable.setStyleSheet("font: 14pt \"Segoe UI\";")
        self.readyLable.setAlignment(QtCore.Qt.AlignCenter)
        self.readyLable.setObjectName("readyLable")
        self.feedback = QtWidgets.QLabel(self.EndingWindow_frame)
        self.feedback.setGeometry(QtCore.QRect(200, 240, 200, 50))
        self.feedback.setStyleSheet("font: 12pt \"Segoe UI\";")
        self.feedback.setAlignment(QtCore.Qt.AlignCenter)
        self.feedback.setObjectName("feedback")
        self.downloadButton = QtWidgets.QPushButton(self.EndingWindow_frame, clicked=lambda: self.downloadButtonClicked())
        self.downloadButton.setGeometry(QtCore.QRect(200, 60, 200, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("font: 13pt \"Arial\";\n"
"background-color: rgb(244, 249, 250);\n"
"border: none;\n"
"")
        self.downloadButton.setObjectName("downloadButton")
        self.emailButton = QtWidgets.QPushButton(self.EndingWindow_frame, clicked=lambda: self.emailButtonClicked())
        self.emailButton.setGeometry(QtCore.QRect(200, 90, 200, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        self.emailButton.setFont(font)
        self.emailButton.setStyleSheet("font: 13pt \"Arial\";\n"
"background-color: rgb(244, 249, 250);\n"
"border: none;\n"
"")
        self.emailButton.setObjectName("emailButton")
        self.frame = QtWidgets.QFrame(self.EndingWindow_frame)
        self.frame.setGeometry(QtCore.QRect(0, 280, 600, 50))
        self.frame.setStyleSheet("border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.star5 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.star5Clicked())
        self.star5.setGeometry(QtCore.QRect(380, 10, 30, 30))
        self.star5.setStyleSheet("border: none;\n"
"background-color: rgb(244, 249, 250);")
        self.star5.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.star5.setIcon(icon)
        self.star5.setIconSize(QtCore.QSize(30, 30))
        self.star5.setCheckable(False)
        self.star5.setObjectName("star5")
        self.star2 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.star2Clicked())
        self.star2.setGeometry(QtCore.QRect(230, 10, 30, 30))
        self.star2.setStyleSheet("border: none;\n"
"background-color: rgb(244, 249, 250);")
        self.star2.setText("")
        self.star2.setIcon(icon)
        self.star2.setIconSize(QtCore.QSize(30, 30))
        self.star2.setCheckable(False)
        self.star2.setObjectName("star2")
        self.star4 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.star4Clicked())
        self.star4.setGeometry(QtCore.QRect(330, 10, 30, 30))
        self.star4.setStyleSheet("border: none;\n"
"background-color: rgb(244, 249, 250);")
        self.star4.setText("")
        self.star4.setIcon(icon)
        self.star4.setIconSize(QtCore.QSize(30, 30))
        self.star4.setCheckable(False)
        self.star4.setObjectName("star4")
        self.star1 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.star1Clicked())
        self.star1.setGeometry(QtCore.QRect(180, 10, 30, 30))
        self.star1.setStyleSheet("border: none;\n"
"background-color: rgb(244, 249, 250);")
        self.star1.setText("")
        self.star1.setIcon(icon)
        self.star1.setIconSize(QtCore.QSize(30, 30))
        self.star1.setCheckable(False)
        self.star1.setObjectName("star1")
        self.star3 = QtWidgets.QPushButton(self.frame, clicked=lambda: self.star3Clicked())
        self.star3.setGeometry(QtCore.QRect(280, 10, 30, 30))
        self.star3.setStyleSheet("border: none;\n"
"background-color: rgb(244, 249, 250);")
        self.star3.setText("")
        self.star3.setIcon(icon)
        self.star3.setIconSize(QtCore.QSize(30, 30))
        self.star3.setCheckable(False)
        self.star3.setObjectName("star3")
        self.thanksLabel = QtWidgets.QLabel(self.EndingWindow_frame)
        self.thanksLabel.setGeometry(QtCore.QRect(175, 120, 250, 100))
        self.thanksLabel.setStyleSheet("font: 24pt \"Arial\";")
        self.thanksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.thanksLabel.setObjectName("thanksLabel")
        self.logoButton = QtWidgets.QPushButton(self.EndingWindow_frame, clicked=lambda: self.logoButtonPressed(EndingWindow, initialWindow))
        self.logoButton.setGeometry(QtCore.QRect(500, 10, 70, 70))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setUnderline(False)
        self.logoButton.setFont(font)
        self.logoButton.setStyleSheet("background-color: rgb(244, 249, 250);\n"
"border: none;\n"
"color: black;")
        self.logoButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../guiPages/../images/icon_whiteBackground.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoButton.setIcon(icon1)
        self.logoButton.setIconSize(QtCore.QSize(70, 70))
        self.logoButton.setObjectName("logoButton")

        self.retranslateUi(EndingWindow)
        QtCore.QMetaObject.connectSlotsByName(EndingWindow)

    def retranslateUi(self, EndingWindow):
        _translate = QtCore.QCoreApplication.translate
        EndingWindow.setWindowTitle(_translate("EndingWindow", "Form"))
        self.readyLable.setText(_translate("EndingWindow", "Your music sheet is ready!"))
        self.feedback.setText(_translate("EndingWindow", "We appreciate your feedback:"))
        self.downloadButton.setText(_translate("EndingWindow", "Download"))
        self.emailButton.setText(_translate("EndingWindow", "Send to email"))
        self.thanksLabel.setText(_translate("EndingWindow", "Thank you for using\n"
" PerfectPitch!"))

    # When export button is pressed - back to initial window
    def logoButtonPressed(self, EndingWindow, initialWindow):
        initialWindow.show()
        EndingWindow.hide()

    def star1Clicked(self):
        # Zero starts to one star
        if self.stars < 1:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starYellow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.stars = 1

        # One star to zero stars
        elif self.stars == 1:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.stars = 0
        
        # several stars to one star
        else :
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 1

    def star2Clicked(self):
        if self.stars < 2:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starYellow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.stars = 2

        elif self.stars == 2:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.stars = 0
        
        else :
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 2

    def star3Clicked(self):
        if self.stars < 3:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starYellow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.stars = 3

        elif self.stars == 3:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.stars = 0
        
        else :
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 3

    def star4Clicked(self):
        if self.stars < 4:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starYellow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.stars = 4

        elif self.stars == 4:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.stars = 0
        else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star5.setIcon(icon)
                self.stars = 4

    def star5Clicked(self):
        if self.stars < 5:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starYellow.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 5
        else:
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap("../guiPages/../images/starWhite.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.star1.setIcon(icon)
                self.star2.setIcon(icon)
                self.star3.setIcon(icon)
                self.star4.setIcon(icon)
                self.star5.setIcon(icon)
                self.stars = 0

    def emailButtonClicked(self):
        from emailPopUpController import Ui_emailPopUp
        self.emailPopUp = QtWidgets.QMainWindow()
        self.ui = Ui_emailPopUp()
        self.ui.setupUi(self.emailPopUp)
        self.emailPopUp.show()

    def downloadButtonClicked(self):
        from downloadPopUpController import Ui_downloadPopUp
        self.downloadPopUp = QtWidgets.QMainWindow()
        self.ui = Ui_downloadPopUp()
        self.ui.setupUi(self.downloadPopUp)
        self.downloadPopUp.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EndingWindow = QtWidgets.QWidget()
    ui = Ui_EndingWindow()
    ui.setupUi(EndingWindow)
    EndingWindow.show()
    sys.exit(app.exec_())
