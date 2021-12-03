from Qcalculator import QUseless_Calculator
from PyQt5.QtWidgets import QApplication, QWidget # Import the QApplication and QWidget classes
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(
            int(self.width() * .9),
            int(self.height() * .5),
            int(self.width() * 2 * .8),
            int(self.height() * 2 * .7),
            )
        self.setWindowTitle('PyQt5')
        self.calc = QUseless_Calculator(self)
        self.calc.move(0, 0)
        self.show()

def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()