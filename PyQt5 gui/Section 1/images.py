import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Images")
        self.setGeometry(50, 50, 350, 350)
        self.UI()
        

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("python.png"))
        self.show()
        
def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()