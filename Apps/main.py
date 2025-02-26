from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
# I created a new funcion to show the current time
from nowDateInfo import now_time as nt
import sys
import requests

app = QApplication(sys.argv)
window = QMainWindow()
# showing the current time in the status bar
window.statusBar().showMessage(nt())

# to show the window, we call the show() method.
window.show()

# we can exit the application by calling the exit() method of the QApplication instance, and execute the application.
sys.exit(app.exec()) # can teste too with sys.exit(app.exec_())

