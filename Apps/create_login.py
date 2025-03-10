# Form implementation generated from reading ui file '.\create_login.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QPushButton, QLabel
import traceback
import sys
import mysql.connector as mc


class Ui_create_login_window(object):
    def setupUi(self, create_login_window):
        create_login_window.setObjectName("create_login_window")
        create_login_window.setEnabled(True)
        create_login_window.resize(810, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(create_login_window.sizePolicy().hasHeightForWidth())
        create_login_window.setSizePolicy(sizePolicy)
        create_login_window.setMinimumSize(QtCore.QSize(810, 320))
        create_login_window.setMaximumSize(QtCore.QSize(810, 320))
        font = QtGui.QFont()
        font.setPointSize(18)
        create_login_window.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../Images/login.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        create_login_window.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(create_login_window)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_username = QtWidgets.QLabel(parent=create_login_window)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(28)
        font.setBold(True)
        self.label_username.setFont(font)
        self.label_username.setObjectName("label_username")
        self.horizontalLayout.addWidget(self.label_username)
        self.lineEdit_username = QtWidgets.QLineEdit(parent=create_login_window)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout.addWidget(self.lineEdit_username)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_password = QtWidgets.QLabel(parent=create_login_window)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Variable Text Semibold")
        font.setPointSize(28)
        font.setBold(True)
        self.label_password.setFont(font)
        self.label_password.setObjectName("label_password")
        self.horizontalLayout_2.addWidget(self.label_password)
        self.lineEdit_password = QtWidgets.QLineEdit(parent=create_login_window)
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_2.addWidget(self.lineEdit_password)
        self.pushButton_viewpass = QtWidgets.QPushButton(parent=create_login_window)
        self.pushButton_viewpass.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\../Images/eye.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_viewpass.setIcon(icon1)
        self.pushButton_viewpass.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_viewpass.setObjectName("pushButton_viewpass")
        self.horizontalLayout_2.addWidget(self.pushButton_viewpass)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_adduser = QtWidgets.QPushButton(parent=create_login_window)
        self.pushButton_adduser.setObjectName("pushButton_adduser")
        
        self.pushButton_adduser.clicked.connect(self.insert_data)
        self.verticalLayout.addWidget(self.pushButton_adduser)
        self.pushButton_connectDB = QtWidgets.QPushButton(parent=create_login_window)
        self.pushButton_connectDB.setObjectName("pushButton_connectDB")
        
        self.pushButton_connectDB.clicked.connect(self.connect_db)
        self.verticalLayout.addWidget(self.pushButton_connectDB)
        self.label_result = QtWidgets.QLabel(parent=create_login_window)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(create_login_window)
        QtCore.QMetaObject.connectSlotsByName(create_login_window)

    def retranslateUi(self, create_login_window):
        _translate = QtCore.QCoreApplication.translate
        create_login_window.setWindowTitle(_translate("create_login_window", "CREATE LOGIN"))
        self.label_username.setText(_translate("create_login_window", "USERNAME:"))
        self.lineEdit_username.setPlaceholderText(_translate("create_login_window", "Enter your username"))
        self.label_password.setText(_translate("create_login_window", "PASSWORD:"))
        self.lineEdit_password.setPlaceholderText(_translate("create_login_window", "Enter your password"))
        self.pushButton_adduser.setText(_translate("create_login_window", "Add User"))
        self.pushButton_connectDB.setText(_translate("create_login_window", "Connect to Database"))
    
    def connect_db(self):   
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "DomJhon",
                password = "PdV36f1!Y~1Z",
                database = "app_estoque",
                port=3306
        )
        
            if mydb.is_connected():
                print("Connected to MySQL database!")
                cursor = mydb.cursor()
                cursor.execute("SELECT VERSION()")
                version = cursor.fetchone()
                print(f"MySQL Server Version: {version}")
                #self.label_result.setText("DataBase connected successfully")
                cursor.close()
                
        except mc.Error as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
            self.label_result.setText(error_message)
            traceback.print_exc()
    
    def insert_data(self):
        try:
            mydb = mc.connect(
                host = "localhost",
                user = "DomJhon",
                password = "PdV36f1!Y~1Z",
                database = "app_estoque",
                port=3306
            )
            
            if mydb.is_connected():
                print("Connected to MySQL database!")
                cursor = mydb.cursor()
                cursor.execute("SELECT VERSION()")
                version = cursor.fetchone()
                print(f"MySQL Server Version: {version}")
                cursor.close()
            
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
        except mc.Error as e:
            error_message = f"Error: {str(e)}"
            self.label_result.setText(error_message)
            print(error_message)
            traceback.print_exc()
        except Exception as e:
            error_message = f"Unexpected error: {str(e)}"
            self.label_result.setText(error_message)
            print(error_message)
            traceback.print_exc()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    create_login_window = QtWidgets.QWidget()
    ui = Ui_create_login_window()
    ui.setupUi(create_login_window)
    create_login_window.show()
    sys.exit(app.exec())
