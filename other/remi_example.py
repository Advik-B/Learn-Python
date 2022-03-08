import remi.gui as gui
from remi import start, App

class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def main(self):
        container = gui.VBox(width=300, height=300, style={'margin':'0px auto', 'text-align':'center'})
        
        abv = gui.Button('Button', width=100, height=30)
        abv.style['margin'] = '10px'
        
        textBox = gui.TextInput(width=100, height=30)
        
        container.append(textBox)        
        container.append(abv)

        return container

# starts the web server
start(MyApp, port=80, debug=True)