import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["sys", 'PyQt5', 'json'], "excludes": ["tkinter"]}

base = "Win32GUI" if sys.platform == "win32" else None
setup(
    name = "guifoo",
    version = "0.1",
    description = "My GUI application!",
    options = {"build_exe": build_exe_options},
    files = ["employes_app.ui", "assets/", "phonenumbers.txt", 'employes.json'],
    executables = [Executable("employes_app.py", base=base)]
)
