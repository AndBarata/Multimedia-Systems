# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../guiPages/initialWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initialWindow(object):
    def setupUi(self, initialWindow):
        initialWindow.setObjectName("initialWindow")
        initialWindow.resize(600, 400)
        initialWindow.setStyleSheet("background-color: rgb(244, 249, 250);")
        self.centralwidget = QtWidgets.QWidget(initialWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.initialwindow_frame = QtWidgets.QFrame(self.centralwidget)
        self.initialwindow_frame.setGeometry(QtCore.QRect(0, 0, 600, 400))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setUnderline(True)
        self.initialwindow_frame.setFont(font)
        self.initialwindow_frame.setStyleSheet("background-color: rgb(244, 249, 250);")
        self.initialwindow_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.initialwindow_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.initialwindow_frame.setObjectName("initialwindow_frame")
        self.logo = QtWidgets.QLabel(self.initialwindow_frame)
        self.logo.setGeometry(QtCore.QRect(200, 50, 201, 200))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("../guiPages/../images/icon_whiteBackground.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.startButton = QtWidgets.QPushButton(self.initialwindow_frame, clicked=lambda: self.startButtonClicked(initialWindow))
        self.startButton.setGeometry(QtCore.QRect(200, 250, 200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("font: 20pt \"Segoe UI\";\n"
"background-color: rgb(28, 206, 176);")
        self.startButton.setObjectName("startButton")
        self.aboutButton = QtWidgets.QPushButton(self.initialwindow_frame, clicked=lambda: self.aboutButtonClicked())
        self.aboutButton.setGeometry(QtCore.QRect(450, 360, 141, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setUnderline(True)
        self.aboutButton.setFont(font)
        self.aboutButton.setStyleSheet("background-color: rgb(244, 249, 250);\n"
                                    "border: none;\n"
                                    "color: black;")
        self.aboutButton.setObjectName("aboutButton")
        initialWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(initialWindow)
        QtCore.QMetaObject.connectSlotsByName(initialWindow)

    def retranslateUi(self, initialWindow):
        _translate = QtCore.QCoreApplication.translate
        initialWindow.setWindowTitle(_translate("initialWindow", "MainWindow"))
        self.startButton.setText(_translate("initialWindow", "START"))
        self.aboutButton.setText(_translate("initialWindow", "About PerfectPitch"))


    def startButtonClicked(self, initialWindow):
        from mainWindowController import Ui_mainWindow

        self.mainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.mainWindow, initialWindow)
        self.mainWindow.show()
        initialWindow.hide()


    def aboutButtonClicked(self):
        from aboutPerfectPitchController import Ui_aboutPerfectPitch

        self.aboutPerfectPitch = QtWidgets.QWidget()
        self.ui = Ui_aboutPerfectPitch()
        self.ui.setupUi(self.aboutPerfectPitch)
        self.aboutPerfectPitch.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initialWindow = QtWidgets.QMainWindow()
    ui = Ui_initialWindow()
    ui.setupUi(initialWindow)
    initialWindow.show()
    sys.exit(app.exec_())