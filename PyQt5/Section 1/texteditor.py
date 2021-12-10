from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
from PyQt5.QtGui import QTextCursor, QFont
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.ubuntu_font = QFont('Ubuntu Mono', 12)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(
            int(self.width() * .9),
            int(self.height() * .5),
            800,
            600
            )
        self.setWindowTitle('PyQt5')
        self.text_edit = QTextEdit(self)
        self.text_edit.move(100, 80)
        self.text_edit.setFont(self.ubuntu_font)
        self.text_edit.setAcceptRichText(True)
        self.text_edit.resize(600, 400)
        
        
        self.send_button = QPushButton(self)
        self.send_button.setText('Send')
        self.send_button.move(610, 500)
        self.send_button.clicked.connect(self.send_button_clicked)
        
        self.show()

    def send_button_clicked(self):
        print(self.text_edit.toPlainText())
    
def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()