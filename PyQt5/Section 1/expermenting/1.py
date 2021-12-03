from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineFullScreenRequest
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QProgressBar, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from warnings import warn
from sys import argv, exit as sys_exit

warn("This is a test warning")

class Windows(QWidget):
    def init(self):
        self.setWindowTitle('Web Engine View')
        self.setGeometry(300, 300, 750, 500)
        self.setWindowIcon(QIcon('python.png'))
        # self.load(QUrl(''))
        self.webUrl = QLineEdit(self)
        self.webUrl.setPlaceholderText('Enter URL:')
        self.webUrl.move(15, 10)
        self.webUrl.resize(700, 30)
        self.webUrl.returnPressed.connect(self.load)
        self.webView = QWebEngineView(self)
        self.webView.move(15, 50)
        self.webView.resize(700, 400)
        self.show()
    
    def load(self):
        
        self.url = QUrl(self.webUrl.text())
        self.webView.setAcceptDrops(True)
        self.webView.setAttribute(Qt.WA_AcceptTouchEvents, True)
        try:
            self.webView.load(self.url)
            self.webView.show()
        except Exception as e:
            print('ERROR:', e, sep='\n')

def main():
    app = QApplication(argv)
    win = Windows()
    win.init()
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()