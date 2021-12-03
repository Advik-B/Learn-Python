import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using LineEdit")
        self.setGeometry(650, 150, 550, 550)
        self.UI()
  

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.setPlaceholderText("Enter your name")
        self.nameTextBox.move(120, 50)
        self.passTextBox = QLineEdit(self)
        self.passTextBox.setPlaceholderText("Enter your password")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120, 100)
        self.submitButton = QPushButton("Save", self)
        self.submitButton.move(165, 150)
        self.submitButton.clicked.connect(self.save)
        self.show()
    
    def save(self):
        print('Name:',self.nameTextBox.text())
        print('Password:',self.passTextBox.text())
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()