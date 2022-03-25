import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Bipin Chauhan\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Bipin Chauhan\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="logo.ico")]


cx_Freeze.setup(
    name = "Magic Restaurent",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["logo.ico",'tcl86t.dll','tk86t.dll', 'images','database']}},
    version = "1.0",
    description = "Magic Restaurent",
    executables = executables
    )
