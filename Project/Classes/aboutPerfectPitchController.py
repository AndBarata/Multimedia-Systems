# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../guiPages/aboutPerfectPitch.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutPerfectPitch(object):
    def setupUi(self, aboutPerfectPitch):
        aboutPerfectPitch.setObjectName("aboutPerfectPitch")
        aboutPerfectPitch.resize(400, 250)
        aboutPerfectPitch.setStyleSheet("background-color: rgb(196, 236, 236);")
        self.aboutPerfectPitch_frame = QtWidgets.QFrame(aboutPerfectPitch)
        self.aboutPerfectPitch_frame.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.aboutPerfectPitch_frame.setMaximumSize(QtCore.QSize(500, 600))
        self.aboutPerfectPitch_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.aboutPerfectPitch_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.aboutPerfectPitch_frame.setObjectName("aboutPerfectPitch_frame")
        self.version = QtWidgets.QLabel(self.aboutPerfectPitch_frame)
        self.version.setGeometry(QtCore.QRect(170, 230, 49, 16))
        self.version.setAlignment(QtCore.Qt.AlignCenter)
        self.version.setObjectName("version")
        self.about = QtWidgets.QLabel(self.aboutPerfectPitch_frame)
        self.about.setGeometry(QtCore.QRect(100, 140, 200, 50))
        self.about.setAlignment(QtCore.Qt.AlignCenter)
        self.about.setObjectName("about")

        self.retranslateUi(aboutPerfectPitch)
        QtCore.QMetaObject.connectSlotsByName(aboutPerfectPitch)

    def retranslateUi(self, aboutPerfectPitch):
        _translate = QtCore.QCoreApplication.translate
        aboutPerfectPitch.setWindowTitle(_translate("aboutPerfectPitch", "Form"))
        self.version.setText(_translate("aboutPerfectPitch", "V 1.0"))
        self.about.setText(_translate("aboutPerfectPitch", "Tune your instrument and improve \n"
"your pitch by using PerfectPitch."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutPerfectPitch = QtWidgets.QWidget()
    ui = Ui_aboutPerfectPitch()
    ui.setupUi(aboutPerfectPitch)
    aboutPerfectPitch.show()
    sys.exit(app.exec_())

