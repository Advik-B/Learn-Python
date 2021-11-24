import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using labels")
        self.setGeometry(50, 50, 350, 350)
        self.UI()
        

    def UI(self):
        text1 = QLabel("This is a label", self)
        text2 = QLabel("This is another label", self)
        text1.move(100, 50)
        text2.move(200, 50)
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()