from PyQt5.QtWidgets import QApplication, QWidget, QCalendarWidget, QPushButton, QLineEdit, QProgressBar
from PyQt5.QtGui import QFont
from sys import argv, exit as sys_exit
from TradingWithPython.main import get

class CustomProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setValue(0)
        with open("progress-bar.stylesheet.qml", "r") as f:
            self.setStyleSheet(f.read())
    
    def step(self, val):
        self.setValue(self.value() + val)
    
    def config(self,**kwargs):
        self.setMaximum(kwargs.get("maximum"))
   
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.fon = QFont('Ubuntu Mono', 20)
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
        self.text_edit.setReadOnly(True)
        self.text_edit.resize(800, 60)

        self.download_button = QPushButton('Download', self)
        self.download_button.move(0, 400)
        self.download_button.resize(800, 60)
        self.download_button.setFont(self.fon)
        self.download_button.clicked.connect(self.download_button_clicked)
        
        self.progress_bar = CustomProgressBar(self)
        self.progress_bar.move(0, 500)
        self.progress_bar.resize(800, 30)
        print(self.progress_bar.maximum())
        print(self.progress_bar.value())
        self.progress_bar.config(maximum=100)

        self.show()

    def show_date(self):
        self.progress_bar.step(1)
        print(self.calendar.selectedDate().toString())
        self.text_edit.setDisabled(False)
        self.text_edit.setText(self.calendar.selectedDate().toString())
        self.text_edit.setReadOnly(True)
    
    def download_button_clicked(self):
        dat = self.calendar.selectedDate()
        
        month = dat.month()
        year = dat.year()
        day = dat.day()
        
        get(date=day, month=month, year=year)
        

def main():
    app = QApplication(argv)
    gui = Window()
    app.setActiveWindow(gui)
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()