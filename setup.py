from cx_Freeze import *
setup(name="test",
      version="0.1",
      description="test",
      executables=[Executable("main.py")])