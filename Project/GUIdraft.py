import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QBoxLayout, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont



class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        super().__init__()
        self.setWindowTitle("Initial menu")
        self.setWindowIcon(QIcon("images/PerfectPitch_icon.png")) # Icon
        self.setGeometry(100, 100, 500, 500) # Position and Size x, y, width, height

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()
        button = QPushButton('&default', clicked=self.sayHello)
        self.output = QTextEdit()

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)

    def sayHello(self):
        self.output.setText("Hello {0}".format(self.inputField.text()))
    

app = QApplication(sys.argv)
app.setStyleSheet('''
    QWidget {
        font-size: 25px;
    }

    QPushButton {
        font-size: 25px;
    }
''')
window = MyApp()
window.show()
sys.exit(app.exec())