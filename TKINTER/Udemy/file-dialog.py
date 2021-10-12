from tkinter import *
from tkinter import ttk, messagebox, filedialog, colorchooser
try:
    from ttkthemes import themed_tk
except ModuleNotFoundError:
    import os
    os.system('pip install ttkthemes')
    from ttkthemes import themed_tk

try:
    from halo import Halo
except ModuleNotFoundError:
    import os
    os.system('pip install halo')
    from halo import Halo
from threading import Thread
from time import sleep
root = themed_tk.ThemedTk()
root.title('Text Editor')
root.geometry('1000x890+500+150')
supported_files=[
            ('Text Supported Files', ('.txt', '.log', '.env', '.py', '.pyi', '.pyt', '.pyw', '.jav', '.java')),
            ]

def __change_theme():
    while True:
        try:
            a = t.get()
            root.set_theme(a)
            sleep(1)
        except RuntimeError:
            exit(0)
            
def look_for_themes():
    abc = Thread(target=__change_theme)
    abc.start()    
    

def openFile():
    def a():
        filedname = filedialog.askopenfilename(
        filetypes=supported_files,
        defaultextension='.txt')
        if filedname == None or filedname=='\n':
            return
        else:
            text_editor.delete(1.0, 'end')
            try:
                f= open(filedname)
                text_editor.insert(1.0, f.read())
                f.close()
                root.title('Editing: {}'.format(filedname.split("/")[-1]))
                lbl.config(text='Editing: {}'.format(filedname.split("/")[-1]))
            except FileNotFoundError:
                messagebox.showerror(title='Error', message='No File Chosen!')
        
    content = text_editor.get(1.0, 'end')
    if not content or content == None or content == '' or content =='\n':
        a()
    else:
        if messagebox.askyesno('Warning','All changes will be lost.\nDo you want to still continue?' ,icon='warning'):
            a()
        else: return

def saveFile():
    filename=filedialog.asksaveasfile(filetypes=supported_files ,confirmoverwrite=True, defaultextension='.txt')
    if filename ==None:
        return
    content =text_editor.get(1.0, 'end')
    filename.write(content)

def clear():
    lbl.config(text='')
    text_editor.delete(1.0, 'end')
    root.title('Text Editor')

def Change_Color():
    color = colorchooser.askcolor()
    text_editor.configure(fg=color[1])

lbl = Label(root, font='Vendara 15')
text_editor = Text(root,takefocus=True, width=70, height=35, font=['Ubuntu Mono', 10] ,wrap='word')
lbl.pack()
text_editor.pack()
openfile = ttk.Button(root, text='Open File', command=openFile, width=81)
savefile = ttk.Button(root, text='Save As', command=saveFile, width=81)
clear_all = ttk.Button(root, text='Clear All', command=clear, width=81)
change = ttk.Button(root, text='Change Color', command=Change_Color, width=81)
val = root.get_themes()
t = StringVar(root, value='vista')
change_theme = ttk.Combobox(root ,textvariable=t, values=val, state='readonly')
change_theme.pack()
openfile.pack()
savefile.pack()
clear_all.pack()
change.pack()
look_for_themes()

def start():
    spinner = Halo(text='App is running', placement='right', text_color='green' , color='cyan')
    spinner.animation
    t = Thread(target=lambda:spinner.start())
    t.start()
    root.mainloop()
    while True:
        if root.quit:
            spinner.stop()
            exit(0)

start()
