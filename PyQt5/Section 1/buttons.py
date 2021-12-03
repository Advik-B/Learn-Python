import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Buttons")
        self.setGeometry(100, 100, 300, 300)
        self.UI()

    def UI(self):
        self.label = QLabel(self)
        self.label.setText("Hello World")
        self.label.move(100, 100)
        self.button = QPushButton("Click Me", self)
        self.button.move(100, 150)
        self.button.clicked.connect(self.button_clicked)
        # self.setStyleSheet('background-color:white;')
        self.show()
    
    def button_clicked(self):
        self.str1 = "Button Clicked"
        self.label.resize(150, len(self.str1))
        self.label.setText(self.str1)

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()