from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()

root.geometry('700x650')

def install(mode:str , path:str) -> None:
    """
    This function will install the server\
    on the specified path based on the mode given.\n
    The avalable modes are:\n
            `bukkit`\n
            `fabric`\n
            `forge`\n
            `magma`\n
            `mohist`\n
            `paper`\n
            `spigot`\n
            `vanilla`
        """

root.mainloop()