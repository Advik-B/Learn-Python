from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit,  QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QFont
from sys import argv, exit as sys_exit

global font
font = QFont('Ubuntu Mono', 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(650, 150, 600, 700)
        self.setWindowTitle('Message Box')
        self.setWindowIcon(QIcon('python.png'))
        self.bnt = QPushButton('Show Message Box', self)
        self.bnt.move(50, 50)
        self.bnt.resize(200, 50)
        self.bnt.setFont(font)
        self.bnt.clicked.connect(self.message_box)
        self.show()
    
    def message_box(self):
        # mbox = QMessageBox.question(self, '!!! Warning !!!', 'Are you shure you want to exit', QMessageBox.Yes | QMessageBox.No , QMessageBox.No)
        # if mbox == QMessageBox.Yes:
        #     sys_exit()
        mbox = QMessageBox.information(self, '!!! Information !!!', 'This is a information message')
        mbox = QMessageBox.warning(self, '!!! Warning !!!', 'This is a warning message')
        mbox = QMessageBox.critical(self, '!!! Critical !!!', 'This is a critical message')
        mbox = QMessageBox.about(self, '!!! About !!!', 'This is a about message')
        mbox = QMessageBox.aboutQt(self, '!!! About Qt !!!')

def main():
    app = QApplication(argv)
    window = Window()
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()