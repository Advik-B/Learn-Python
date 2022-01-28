from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QSpinBox, QComboBox, QPlainTextEdit, QListWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QIcon, QImage
from PyQt5.QtCore import QSize
import sys
import json

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        loadUi('employes_app.ui', self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Employes App')
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon('assets/default.png'))
        self.profile_pic = self.findChild(QPushButton, 'profile_pic')
        self.name = self.findChild(QLineEdit, 'name_tbox')
        self.surname = self.findChild(QLineEdit, 'surname_tbox')
        self.age = self.findChild(QSpinBox, 'age')
        self.gender = self.findChild(QComboBox, 'gender_cbox')
        self.phone0 = self.findChild(QComboBox, 'phone_number_prefix')
        self.phone1 = self.findChild(QLineEdit, 'phone1')
        self.email = self.findChild(QLineEdit, 'email')
        self.address = self.findChild(QPlainTextEdit, 'addr_tbox')
        self.notes = self.findChild(QPlainTextEdit, 'notes')
        self.items = self.findChild(QListWidget, 'items')
        self.profile_pic.setStyleSheet('border: 0px;')
        self.profile_pic.clicked.connect(self.change_profile)
        self.getdata()
        self.show()

    def getdata(self):
        with open('employes.json', 'r') as file:
            data: list = json.load(file)
        for dat in data:
            self.items.addItem(dat['name'])
        def _show_data():
            # self.show_data(
            name = self.items.currentItem().text()
            for dat in data:
                if dat['name'] == name:
                    obj = dat
                    break
            self.show_data(

                name=obj.get('name'),
                address=obj.get('address'),
                age=obj.get('age'),
                email=obj.get('email'),
                notes=obj.get('notes'),
                phone0=obj.get('phone0'),
                phone1=obj.get('phone1'),
                profile_pic=obj.get('avatar'),
                surname=obj.get('surname'),
                gender=obj.get('gender')
            )
            print(name)
        with open('phonenumbers.txt', 'r') as f:
            for item in f:
                self.phone0.addItem(item)
            # )
        self.items.currentItemChanged.connect(_show_data)

    def show_data(
        self,
        profile_pic,
        name,
        surname,
        age,
        phone0,
        phone1,
        email,
        address,
        notes,
        gender,
            ):
        self.profile_pic.setIcon(QIcon(profile_pic))
        self.profile_pic.setIconSize(QIcon(profile_pic).actualSize(QSize(200, 200)))
        self.name.setText(name)
        self.surname.setText(str(surname))
        self.age.setValue(age)
        self.phone0.setCurrentText(phone0)
        self.phone1.setText(phone1)
        self.email.setText(email)

        if gender == 'male':
            self.gender.setCurrentIndex(0)
        elif gender == 'female':
            self.gender.setCurrentIndex(1)
        elif gender == 'other':
            self.gender.setCurrentIndex(2)
        self.address.setPlainText(address)
        self.notes.setPlainText(notes)
    def change_profile(self):
        if self.items.currentItem() is not None:
            file = QFileDialog.getOpenFileName(self, 'Open file', './assets/', 'Image files (*.png *.jpg *.bmp)')
            if file != ('', ''): # IF NOT EMPTY
                self.profile_pic.setIcon(QIcon(file[0]))
                self.profile_pic.setIconSize(QIcon(file[0]).actualSize(QSize(200, 200)))



def main():
    global main_ui, window
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
