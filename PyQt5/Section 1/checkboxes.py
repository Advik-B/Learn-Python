from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon

from sys import argv, exit as sys_exit

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.username = 'Advik', 'advik.b@gmail.com', 'advik', ''
        self.password = 'hackerman', ''
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Checkboxes")
        # Make the window not resizable
        self.setGeometry(900, 150, 600, 200)
        self.setFixedSize(600, 200)
        self.setWindowIcon(QIcon("python.png"))
        self.name_textbox = QLineEdit(self)
        self.name_textbox.setPlaceholderText("Enter your username or email")
        self.password_textbox = QLineEdit(self)
        self.password_textbox.setPlaceholderText("Enter your password")
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.remember_me_checkbox = QCheckBox("Remember me", self)
        self.remember_me_checkbox.setChecked(False)
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.login)
        
        self.name_textbox.resize(550, 30)
        self.name_textbox.move(20, 20)
        self.password_textbox.resize(550, 30)
        self.password_textbox.move(20, 60)
        self.remember_me_checkbox.resize(550, 30)
        self.remember_me_checkbox.move(20, 100)
        self.login_button.resize(550, 30)
        self.login_button.move(20, 140)
        self.show()

    def login(self):
        username = self.name_textbox.text()
        password = self.password_textbox.text()
        remember_me = self.remember_me_checkbox.isChecked()
        if username in self.username and password in self.password:
            print("Login successful")
            print("Username:", username)
            print("Password:", password)
            print("Remember me:", remember_me)
            self.setWindowOpacity(.5)
            self.setWindowTitle("Login successful")
        else:
            print("Login failed")
            print("Username:", username)
            print("Password:", password)
            print("Remember me:", remember_me)

def main():
    app = QApplication(argv)
    window = LoginWindow()
    sys_exit(app.exec_())

if __name__ == "__main__":
    main()