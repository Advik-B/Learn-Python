import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()
        

    def UI(self):
        self.text1 = QLabel("My text", self)
        self.enter_btn = QPushButton("Enter", self)
        self.exit_btn = QPushButton("Exit", self)
        self.text1.move(160, 50)
        self.enter_btn.move(100, 80)
        self.exit_btn.move(200, 80)
        self.enter_btn.clicked.connect(self.enter_func)
        self.exit_btn.clicked.connect(self.exit_func)
        self.show()
        
    def enter_func(self):
        self.text1.setText("enter")
        
    def exit_func(self):
        self.text1.setText("exit")
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()