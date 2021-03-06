from PyQt5.QtWidgets import QApplication, QWidget
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
            600
            )
        self.setWindowTitle('PyQt5')
        self.show()

def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()