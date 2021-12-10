from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton, QLineEdit
from PyQt5.QtGui import QFont
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.fon = QFont('Times', 20)
        self.init_ui()

    def init_ui(self):
        self.setGeometry(
            int(self.width() * .9),
            int(self.height() * .5),
            800,
            600
            )   
        self.setWindowTitle('PyQt5')
        self.calendar = QCalendarWidget(self)
        self.calendar.resize(800, 300)
        self.calendar.setGridVisible(True)
        self.calendar.move(0, 0)
        self.calendar.selectionChanged.connect(self.show_date)
        
        self.text_edit = QLineEdit(self)
        self.text_edit.move(0, 300)
        self.text_edit.setText(self.calendar.selectedDate().toString())
        self.text_edit.setFont(self.fon)
        self.text_edit.resize(800, 60)
        
        self.show()

    def show_date(self):
        print(self.calendar.selectedDate().toString())
        self.text_edit.setText(self.calendar.selectedDate().toString())
    
def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()