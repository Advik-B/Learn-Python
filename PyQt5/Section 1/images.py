import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Images")
        self.setGeometry(50, 50, 1050, 550)
        self.setWindowIcon(QIcon("python.png"))
        self.UI()
        

    def UI(self):
        self.image = QLabel(self)
        img = QPixmap("python.png")
        self.image.setPixmap(img)
        self.image.move(0, 0)
        self.remove_image_btn = QPushButton("Remove Image", self)
        self.remove_image_btn.clicked.connect(self.remove_image)
        self.remove_image_btn.move(100, 100)
        self.show_image_btn = QPushButton("Show Image", self)
        self.show_image_btn.clicked.connect(self.show_image)
        self.show_image_btn.move(200, 100)
        self.show()
    
    def remove_image(self):
        self.image.close()
    
    def show_image(self):
        self.image.show()

def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()