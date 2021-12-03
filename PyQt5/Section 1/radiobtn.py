from PyQt5.QtWidgets import QApplication, QRadioButton, QWidget, QPushButton, QLineEdit
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(900, 150, 600, 700)
        self.setWindowTitle('Radio Button')
        self.name = QLineEdit(self)
        self.name.setPlaceholderText('Enter your name')
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText('Enter your surname')
        self.male = QRadioButton('Male', self)
        self.female = QRadioButton('Female', self)
        self.other = QRadioButton('Other', self)
        self.submit_btn = QPushButton('Submit', self)
        self.name.move(25, 10)
        self.name.resize(550, 30)
        
        self.surname.move(25, 50)
        self.surname.resize(550, 30)
        
        self.male.move(25, 100)
        self.female.move(25 + 80, 100)
        self.other.move(25 + 80 + 80, 100)
        self.submit_btn.move(25, 140)
        self.submit_btn.resize(550, 30)
        self.show()


def main():
    app = QApplication(argv)
    window = Window()
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()