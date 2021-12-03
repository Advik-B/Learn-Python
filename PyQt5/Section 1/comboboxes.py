from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QPushButton
from sys import argv, exit as sys_exit

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(900, 150, 600, 700)
        self.setWindowTitle('ComboBoxes')
        self.combo_box = QComboBox(self)
        self.combo_box.move(150, 100)
        self.button = QPushButton('Save', self)
        self.button.clicked.connect(self.save_selection)
        self.combo_box.addItems(
            [
                # List of programming languages
                'Python',
                'JavaScript',
                'Java',
                'C++',
                'C#',
                'PHP',
                'Objective-C',
                'Swift',
                'Ruby',
                'Go',
                'R',
                'Assembly',
                'TypeScript',
                'C', 
                'CoffeeScript',
                'Scala',
                'Haskell',
                'Dart',
                'Rust',
                'Julia',
                'F#', 
                'Fortran', 
                'Kotlin',
                'D', 
                'Vala', 
                'Lua', 
                'Erlang', 
                'Perl', 
                'Haskell', 
                'Dart', 
                'Rust', 
                'Julia', 
                'F#', 
                'Fortran', 
                'Kotlin', 
                'D',
                'Vala',
            ]
        ) 

        self.combo_box.resize(100, 25)
        self.button.move(150, 150)
        self.show()
    
    def save_selection(self):
        print(self.combo_box.currentText())
        
def main():
    app = QApplication(argv)
    window = Window()
    sys_exit(app.exec_())

if __name__ == '__main__':
    main()