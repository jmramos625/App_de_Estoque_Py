from PyQt6 import QtCore, QtGui, QtWidgets
# its needed to use and import the mysql.connector module to connect to the database.
import mysql.connector as mc


'''def create_database(self):
    try:
        mydb = mc.connect(
            host = "localhost"
            user = "root"
            password = "%1XY8Oi1ePfb"
            
            cursor = mydb.cursor()
            dbname = self.lineEdit.text()
            cursor.execute("CREATE DATABASE " + dbname)
            self.label_result.setText("Database " + dbname + " created successfully")
        )
    except mc.Error as e:
        self.label_result.setText("Error: " + str(e))'''
        
'''def db_connect(self):
    try:
        mydb = mc.connect(
            host = "localhost"
            user = "root"
            password = "%1XY8Oi1ePfb"
            database = "NAME OF THE DATABASE CREATED"
        )
        
        self.label_result.setText("Connected to the database")
    except mc.Error as e:        
        self.label_result.setText("Error: " + str(e))'''

'''
# setting the connection to the database in the button click event.
self.pushButton.clicked.connect(self.create_database)

# this is the code to create the table in the database.
CREATE TABLE `app_estoque`.`users_pass` (
  `idusers` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  `password` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`idusers`))
COMMENT = 'This is the first DB create to alocate the primary users of my apps';
'''