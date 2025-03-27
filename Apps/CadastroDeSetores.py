from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLineEdit, QTextEdit, QPushButton, QLabel, QMessageBox
import sys
# to import the UI file, we use the uic module from PyQt6.
from PyQt6 import uic
import MySQLdb as mdb

# we will do a class to call the UI file.
class cadastro_de_setores_UI(QWidget):
    def __init__(self):
        super().__init__()
        # be attention to the path of the UI file. This most be the real path of the file.
        uic.loadUi("Apps\CadastroDeSetores.ui", self)
        
        #get the objects from the UI file.
        self.lineEdit_cod_setores = self.findChild(QLineEdit, "lineEdit_cod_setores")
        self.lineEdit_desc_setores = self.findChild(QLineEdit, "lineEdit_desc_setores")
        self.lineEdit_responsavel_setores = self.findChild(QLineEdit, "lineEdit_responsavel_setores")
        
        self.textEdit_localizacao_setores = self.findChild(QTextEdit, "textEdit_localizacao_setores")
        self.textEdit_obs_setores = self.findChild(QTextEdit, "textEdit_obs_setores")
        
        self.pushButton_cadastrar_setores = self.findChild(QPushButton, "pushButton_cadastrar_setores")
        self.pushButton_limpar_tela_setores = self.findChild(QPushButton, "pushButton_limpar_tela_setores")
        self.pushButton_sair_setores = self.findChild(QPushButton, "pushButton_sair_setores")
        
        self.label_feedback_setores = self.findChild(QLabel, "label_feedback_setores")
        
        #buttons actions
        self.pushButton_cadastrar_setores.clicked.connect(self.cadastrar_setores)
        self.pushButton_limpar_tela_setores.clicked.connect(self.limpar_tela)
        self.pushButton_sair_setores.clicked.connect(self.close)
        
        
        
        
    
    def cadastrar_setores(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Confirmação!")
        dialog.setText("Tem certeza que quer adicionar esse Setor?")
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dialog.setIcon(QMessageBox.Icon.Question)
        
        response = dialog.exec()
        
        if response == QMessageBox.StandardButton.Yes:
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
                
                #getting the values from the fields
                cod_setor = self.lineEdit_cod_setores.text()
                desc_setor = self.lineEdit_desc_setores.text()
                responsavel_setor = self.lineEdit_responsavel_setores.text()
                localizacao_setor = self.textEdit_localizacao_setores.toPlainText()
                obs_setor = self.textEdit_obs_setores.toPlainText()
                
                #setting the SQL command to insert the data in the table.
                query = "INSERT INTO setores (nomeSetores, descSetores, responSetores, localSetores, obsSetores) VALUES (%s, %s, %s, %s, %s)"
                values = (cod_setor, desc_setor, responsavel_setor, localizacao_setor, obs_setor)
                
                # executing the SQL command.
                mycursor.execute(query, values)
                
                mydb.commit() # commiting the changes in the database.
                
                self.limpar_tela() # Create this after
                self.label_feedback_setores.setText("Setor: " + cod_setor + ", adicionado com sucesso!") # to give the feedback to the user
            except mdb.Error as e:
                error_message = f"Error: {str(e)}"
                self.label_feedback_setores.setText(error_message)
                print(error_message)
            except Exception as e:
                error_message = f"Unexpected error: {str(e)}"
                self.label_feedback_setores.setText(error_message)
                print(error_message)
        else:
            self.label_feedback.setText("Item não inserido!")
    
    def limpar_tela(self):
        self.lineEdit_cod_setores.clear()
        self.lineEdit_desc_setores.clear()
        self.lineEdit_responsavel_setores.clear()
        self.textEdit_localizacao_setores.clear()
        self.textEdit_obs_setores.clear()
        self.label_feedback_setores.clear()
        self.label_feedback_setores.setText("CADASTRANDO SETORES...")