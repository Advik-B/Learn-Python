from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtGui import QFont
from sys import argv, exit as sys_exit
from random import choice

class QUseless_Calculator(QWidget):

    def __init__(self, parent=None):
        
        if parent:
            super().__init__(parent)
        else:
            super().__init__()
        self.init_ui()

    def key_press(self, event):
        self.main_text_box.insert(str(event))
    
    def divide_(self):
        self.main_text_box.insert('/')
    
    def divide_1(self):
        self.main_text_box.insert('//')
        
    def point_(self):
        self.main_text_box.insert('.')
    
    def remainder_(self):
        self.main_text_box.insert('%')
    
    def multiply_(self):
        self.main_text_box.insert('*')
    
    def multiply_2_(self):
        self.main_text_box.insert('**')
    
    def add_(self):
        self.main_text_box.insert('+')
    
    def subtract_(self):
        self.main_text_box.insert('-')

    def opening_bracket_(self):
        self.main_text_box.insert('(')
    
    def closing_bracket_(self):
        self.main_text_box.insert(')')
    
    def point_(self):
        self.main_text_box.insert('.')

    def clear_(self):
        self.main_text_box.clear()

    def eval_(self):
        try:
            
            expression = self.main_text_box.text().split('\n')[0]
            if expression.startswith('0'):
                expression = expression[1:]
            elif expression.startswith('#'):
                return
            
            self.main_text_box.clear()
            self.main_text_box.insert(str(eval(expression)))
        
        except Exception as e:
            e_ = QMessageBox(icon=QMessageBox.Critical, text=f'Fatal Error:\n{e}', parent=self)
            e_.setWindowTitle('Error')
            if str(e) != 'unexpected EOF while parsing (<string>, line 0)':
                e_.exec_()
            self.main_text_box.insert(expression)

    def init_ui(self):
        self.setGeometry(
            int(self.width() * .9),
            int(self.height() * .5),
            850,
            400,
            )
        self.setWindowTitle('Useless Calculator')
        
        self.number_font = QFont('Ubuntu Mono', 20)
        self.text_font = QFont('Ubuntu Mono', 15)
        
        self.clear_button = QPushButton('C', self)
        self.clear_button.clicked.connect(self.clear_)
        
        self.btn7 = QPushButton('7', self)
        self.btn7.value = 7
        
        self.btn8 = QPushButton('8', self)
        self.btn8.value = 8
        
        self.btn9 = QPushButton('9', self)
        self.btn9.value = 9
        
        self.btn4 = QPushButton('4', self)
        self.btn4.value = 4
        
        self.btn5 = QPushButton('5', self)
        self.btn5.value = 5
        
        self.btn6 = QPushButton('6', self)
        self.btn6.value = 6
        
        self.btn1 = QPushButton('1', self)
        self.btn1.value = 1
        
        self.btn2 = QPushButton('2', self)
        self.btn2.value = 2
        
        self.btn3 = QPushButton('3', self)
        self.btn3.value = 3
        
        self.btn0 = QPushButton('0', self)
        self.btn0.value = 0
        
        
        self.main_text_box = QLineEdit(self)
        self.main_text_box.setFont(self.text_font)
        self.main_text_box.setPlaceholderText('Enter a number')
        
        self.clear_button.setFont(self.number_font)
        
        buttons = [
            self.btn7,
            self.btn8,
            self.btn9,
            self.btn4,
            self.btn5,
            self.btn6,
            self.btn1,
            self.btn2,
            self.btn3,
            self.btn0,
            ]
        
        for button in buttons:
            button.setFont(self.number_font)
            button.clicked.connect(lambda: self.change(button.value))
        
        self.divide = QPushButton('/', self)
        self.divide.clicked.connect(self.divide_)
        
        self.divide_2 = QPushButton('//', self)
        self.divide_2.clicked.connect(self.divide_1)
        
        self.remainder = QPushButton('%', self)
        self.remainder.clicked.connect(self.remainder_)
        
        self.multiply = QPushButton('✕', self)
        self.multiply.clicked.connect(self.multiply_)
        
        self.multiply_2 = QPushButton('^', self)
        self.multiply_2.clicked.connect(self.multiply_2_)
        
        self.subtract = QPushButton('—', self)
        self.subtract.clicked.connect(self.subtract_)
        
        self.add = QPushButton('+', self)
        self.add.clicked.connect(self.add_)
        
        self.point = QPushButton('.', self)
        self.point.clicked.connect(self.point_)
        
        self.equal = QPushButton('=', self)
        self.equal.clicked.connect(self.eval_)
        
        self.open_bracket = QPushButton('(', self)
        self.open_bracket.clicked.connect(self.opening_bracket_)
        
        self.close_bracket = QPushButton(')', self)
        self.close_bracket.clicked.connect(self.closing_bracket_)
        
        self.equal.setFont(self.number_font)

        self.main_text_box.returnPressed.connect(self.eval_)
        
        functions = [
            self.divide,
            self.divide_2,
            self.multiply,
            self.multiply_2,
            self.remainder,
            self.subtract,
            self.add,
            self.point,
            self.open_bracket,
            self.close_bracket,
            ]
        
        for function in functions:
            function.setFont(self.number_font)
        
        # Number Input
        self.main_text_box.move(100, 40)
        self.main_text_box.resize(650, 40)
        
        # Row 1
        self.btn7.move(100, 100)
        self.btn8.move(200, 100)
        self.btn9.move(300, 100)
        # Row 2
        self.btn4.move(100, 160)
        self.btn5.move(200, 160)
        self.btn6.move(300, 160)
        # Row 3
        self.btn1.move(100, 220)
        self.btn2.move(200, 220)
        self.btn3.move(300, 220)
        # Row 4
        self.btn0.move(200, 280)

        # Function buttons
        self.divide.move(450, 100)
        self.divide_2.move(550, 100)
        self.remainder.move(650, 100)
        
        self.open_bracket.move(450, 280)
        self.close_bracket.move(550, 280)
        
        self.multiply.move(450, 160)
        self.multiply_2.move(550, 160)
        self.clear_button.move(650, 160)
        
        self.add.move(450, 220)
        self.subtract.move(550, 220)
        self.point.move(100, 280)
        
        self.equal.move(300, 280)

        self.main_text_box.setFocus()
        self.show()

    def change(self, val):
        self.key_press(val)
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0, 9] # Just to trigger people who have OCD 😏
        for i in range(len(numbers)):
            if i == 10:
                i = 0
            self.btn = getattr(self, 'btn' + str(i))
            vl = str(choice(numbers))
            self.btn.setText(vl)
            self.btn.value = vl
            numbers.remove(int(self.btn.text()))


if __name__ == '__main__':
    app = QApplication(argv)
    ex = QUseless_Calculator()
    sys_exit(app.exec_())