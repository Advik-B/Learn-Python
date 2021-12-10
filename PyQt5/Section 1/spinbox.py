from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox, QPushButton
from PyQt5.QtGui import QFont
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.fon = QFont('Arial', 20)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(
            int(self.width() * .9),
            int(self.height() * .5),
            800,
            600,
            )
        self.setWindowTitle('PyQt5')
        self.spinbox = QSpinBox(self)
        self.spinbox.move(150, 150)
        self.spinbox.setFont(self.fon)
        self.spinbox.setRange(1, 100)
        self.spinbox.setPrefix('$')
        self.spinbox.setSuffix(' USD')
        self.spinbox.setSingleStep(5)
        self.spinbox.resize(200, 50)
        
        self.btn = QPushButton('Send', self)
        self.btn.move(150, 250)
        self.btn.clicked.connect(self.getvalue)
        self.btn.resize(200, 50)
        
        self.show()

    def getvalue(self):
        print(self.spinbox.value())
    
def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()