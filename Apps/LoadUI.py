# We will load the UI file created in the previous part using the PyQt6 module.
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog
import sys
# to import the UI file, we use the uic module from PyQt6.
from PyQt6 import uic

# we will do a class to call the UI file.
class UI(QWidget):
    def __init__(self):
        super().__init__()
        # be attention to the path of the UI file. This most be the real path of the file.
        uic.loadUi("XXXXXXXXX", self)
        

app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()