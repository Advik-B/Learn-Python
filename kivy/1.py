import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class UI(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.add_widget(Label(text='First Name:'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        self.add_widget(Label(text='Last Name:'))
        self.lname = TextInput(multiline=False)
        self.add_widget(self.lname)
        
        self.sumbit = Button(text='Submit', font_size=40)
        self.add_widget(self.sumbit)

class MainUI(App):
    
    def build(self):
        return UI()

def main():
    UI = MainUI()
    UI.run()

if __name__ == '__main__':
    main()
