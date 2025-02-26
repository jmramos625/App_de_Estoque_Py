# We will load the UI file created in the previous part using the PyQt6 module.
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QPushButton, QLabel
import sys
# to import the UI file, we use the uic module from PyQt6.
from PyQt6 import uic
#import the MySQL connector module to connect to the database.
import mysql.connector as mc
import traceback

#maybe this can work too
import MySQLdb as mdb

# we will do a class to call the UI file.
class create_user_UI(QWidget):
    def __init__(self):
        super().__init__()
        # be attention to the path of the UI file. This most be the real path of the file.
        uic.loadUi("Apps\create_login.ui", self)
        
        # now we will get the objects from the UI file.
        self.lineEdit_username = self.findChild(QLineEdit, "lineEdit_username")
        self.lineEdit_password = self.findChild(QLineEdit, "lineEdit_password")
        self.pushButton_adduser = self.findChild(QPushButton, "pushButton_adduser")
        self.pushButton_viewpass = self.findChild(QPushButton, "pushButton_viewpass")
        self.label_result = self.findChild(QLabel, "label_result")
        self.pushButton_connectDB = self.findChild(QPushButton, "pushButton_connectDB")
        
        # now we will set the events to the buttons.
        self.pushButton_adduser.clicked.connect(self.insert_data) # this is the event to the button to add the user.
        self.pushButton_connectDB.clicked.connect(self.connect_db) # this is the event to the button to connect to the database.

     
     
    def connect_db(self):   
        try:
            '''mydb = mc.connect(
                host = "br1158.hostgator.com.br",
                user = "hgroot72_DomJhon",
                password = "PdV36f1!Y~1Z",
                database = "hgroot72_base_teste",
                port=3306
        )'''
            #give the host, user, password, and database name to connect to the database.
            mydb = mdb.connect('br1158.hostgator.com.br', 
                               'hgroot72_DomJhon', 
                               'PdV36f1!Y~1Z', 
                               'hgroot72_base_teste')
        

            print("Connected to MySQL database!")
            cursor = mydb.cursor()
            cursor.execute("SELECT VERSION()")
            version = cursor.fetchone()
            print(f"MySQL Server Version: {version}")
            self.label_result.setText("DataBase connected successfully")
            cursor.close()
                
        except mdb.Error as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            self.label_result.setText(error_message)
            traceback.print_exc()
            
           
    def insert_data(self):
        try:
            mydb = mdb.connect(
                host = "br1158.hostgator.com.br",
                user = "hgroot72_DomJhon",
                password = "PdV36f1!Y~1Z",
                database = "hgroot72_base_teste",
                port=3306
            )
        
            # creating the cursor to execute the SQL commands.
            mycursor = mydb.cursor()
             
            # setting the SQL command to insert the data in the table.
            user = self.lineEdit_username.text()
            passwd = self.lineEdit_password.text()
            
            query = "INSERT INTO users_pass (username, password) VALUES (%s, %s)"
            values = (user, passwd) # this is the values to be inserted in the table.
            
            # executing the SQL command.
            mycursor.execute(query, values) # taking the values to be inserted and the SQL command.
            
            mydb.commit() # commiting the changes in the database.
            
            self.label_result.setText("User " + user + " added successfully") # to give the feedback to the user.
        except mdb.Error as e:
            error_message = f"Error: {str(e)}"
            self.label_result.setText(error_message)
            print(error_message)
            traceback.print_exc()
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"
            self.label_result.setText(error_message)
            print(error_message)
            traceback.print_exc()
 

app = QApplication(sys.argv)
window = create_user_UI()
window.show()
sys.exit(app.exec())