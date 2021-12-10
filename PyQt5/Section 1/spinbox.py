from PyQt5.QtWidgets import QApplication, QWidget, QSpinBox
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
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
        self.show()

def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()