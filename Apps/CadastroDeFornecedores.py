from itertools import count
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QComboBox, QPushButton, QLabel
import sys
# to import the UI file, we use the uic module from PyQt6.
from PyQt6 import uic
import MySQLdb as mdb

# we will do a class to call the UI file.
class cadastro_de_fornecedores_UI(QWidget):
    def __init__(self):
        super().__init__()
        # be attention to the path of the UI file. This most be the real path of the file.
        uic.loadUi("Apps\CadastroDeFornecedores.ui", self)
        
        #getting the objects from the UI file.
        self.lineEdit_razao_social = self.findChild(QLineEdit, "lineEdit_razao_social")
        self.lineEdit_nome_fantasia = self.findChild(QLineEdit, "lineEdit_nome_fantasia")
        self.lineEdit_cnpj_fornecedor = self.findChild(QLineEdit, "lineEdit_cnpj_fornecedor")
        self.lineEdit_im_fornecedor = self.findChild(QLineEdit, "lineEdit_im_fornecedor")
        self.lineEdit_ie_fornecedor = self.findChild(QLineEdit, "lineEdit_ie_fornecedor")
        self.lineEdit_end_completo_fornecedor = self.findChild(QLineEdit, "lineEdit_end_completo_fornecedor")
        self.lineEdit_cnpj_fornecedor = self.findChild(QLineEdit, "lineEdit_cnpj_fornecedor")
        self.lineEdit_telefone1_fornecedor = self.findChild(QLineEdit, "lineEdit_telefone1_fornecedor")
        self.lineEdit_telefone2_fornecedor = self.findChild(QLineEdit, "lineEdit_telefone2_fornecedor")
        self.lineEdit_email_fornecedor = self.findChild(QLineEdit, "lineEdit_email_fornecedor")
        self.lineEdit_site_fornecedor = self.findChild(QLineEdit, "lineEdit_site_fornecedor")
        
        self.comboBox_estado_fornecedor = self.findChild(QComboBox, "comboBox_estado_fornecedor")
        self.comboBox_pais_fornecedor = self.findChild(QComboBox, "comboBox_pais_fornecedor")
        
        
        self.pushButton_cadastrar_fornecedor = self.findChild(QPushButton, "pushButton_cadastrar_fornecedor")
        self.pushButton_limpar_tela_fornecedor = self.findChild(QPushButton, "pushButton_limpar_tela_fornecedor")
        self.pushButton_sair_fornecedor = self.findChild(QPushButton, "pushButton_sair_fornecedor")
        
        self.pushButton_cadastrar_contato_fornecedor = self.findChild(QPushButton, "pushButton_cadastrar_contato_fornecedor")
        self.pushButton_cadastrar_dados_bancarios_fornecedor = self.findChild(QPushButton, "pushButton_cadastrar_dados_bancarios_fornecedor")
        
        self.label_feedback_fornecedor = self.findChild(QLabel, "label_feedback_fornecedor")
        
        # Populate the country combo box
        self.country_combo_box()
        
        # Connect the country combo box signal to the state combo box update method
        self.comboBox_pais_fornecedor.currentIndexChanged.connect(self.state_combo_box)
        
        # Populate the state combo box based on the initial country selection
        self.state_combo_box()
        
        
        #closing the window
        self.pushButton_sair_fornecedor.clicked.connect(self.close)
        
        
      
    def country_combo_box(self):
        #countries
        try:
        #give the host, user, password, and database name to connect to the database.
            mydb = mdb.connect(
                    host = "br1158.hostgator.com.br",
                    user = "hgroot72_DomJhon",
                    password = "PdV36f1!Y~1Z",
                    database = "hgroot72_base_teste",
                    port=3306
                )

            mycursor = mydb.cursor()
            mycursor.execute("SELECT nomePais FROM paises")
            countries = mycursor.fetchall()
            for country in countries:
                self.comboBox_pais_fornecedor.addItem(country[0])
            
            mycursor.close()
            mydb.close()

        except mdb.Error as e:
            error_message = f"Error: {str(e)}"
            print(error_message)  
    
    def state_combo_box(self):
        #states
        
        # Clear the current items in the state combo box
        self.comboBox_estado_fornecedor.clear()
        try:
        #give the host, user, password, and database name to connect to the database.
            mydb = mdb.connect(
                    host = "br1158.hostgator.com.br",
                    user = "hgroot72_DomJhon",
                    password = "PdV36f1!Y~1Z",
                    database = "hgroot72_base_teste",
                    port=3306
                )
            mycursor = mydb.cursor()
            selected_country = self.comboBox_pais_fornecedor.currentText()
            mycursor.execute(f"SELECT nomeEstado FROM estados_mundo WHERE nomePaisEstado = '{selected_country}'")
            states = mycursor.fetchall()
            for state in states:
                self.comboBox_estado_fornecedor.addItem(state[0])
            mycursor.close()
            mydb.close()
        except mdb.Error as e:
            error_message = f"Error: {str(e)}"
            print(error_message)
    
    