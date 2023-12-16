from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PerfectPitch


if __name__ == '__main__':
    global perfectPitch
    perfectPitch = PerfectPitch(sys.argv)
    sys.exit(perfectPitch.exec_())
    