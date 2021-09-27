import PySimpleGUI as sg

layout = [

    [sg.Text('This is only pysimplegui')],
    [sg.Button('Ok')]
]

window = sg.Window('Demo' , layout)

while True:
    event , values = window.read()
    
    if event == 'Ok' or event == sg.WIN_CLOSED:
        break

window.close()