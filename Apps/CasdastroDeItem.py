# We will load the UI file created in the previous part using the PyQt6 module.
import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QLabel, QPushButton, QComboBox, QTextEdit, QLineEdit, QMessageBox, QCompleter
import sys
# to import the UI file, we use the uic module from PyQt6.
from PyQt6 import uic
import MySQLdb as mdb

# we will do a class to call the UI file.
class cadastro_de_item_UI(QWidget):
    def __init__(self):
        super().__init__()
        # be attention to the path of the UI file. This most be the real path of the file.
        uic.loadUi("Apps\CadastroDeItens.ui", self)
        
        # get the itens of the apps
        self.lineEdit_cod_item = self.findChild(QLineEdit, "lineEdit_cod_item")
        self.lineEdit_nome_do_item = self.findChild(QLineEdit, "lineEdit_nome_do_item")
        self.lineEdit_descricao_do_item = self.findChild(QLineEdit, "lineEdit_descricao_do_item")
        self.lineEdit_cod_barras_item = self.findChild(QLineEdit, "lineEdit_cod_barras_item")
        self.comboBox_fornecedor_item = self.findChild(QComboBox, "comboBox_fornecedor_item")
        self.comboBox_un_medida_item = self.findChild(QComboBox, "comboBox_un_medida_item")
        self.lineEdit_qtde_atual_item = self.findChild(QLineEdit, "lineEdit_qtde_atual_item")
        self.lineEdit_est_max_item = self.findChild(QLineEdit, "lineEdit_est_max_item")
        self.lineEdit_est_min_item = self.findChild(QLineEdit, "lineEdit_est_min_item")
        self.lineEdit_ponto_ressup = self.findChild(QLineEdit, "lineEdit_ponto_ressup")
        self.lineEdit_valor_medio_item = self.findChild(QLineEdit, "lineEdit_valor_medio_item")
        self.lineEdit_setor_maior_saida_item = self.findChild(QLineEdit, "lineEdit_setor_maior_saida_item")
        self.comboBox_categoria_do_item = self.findChild(QComboBox, "comboBox_categoria_do_item")
        self.comboBox_rotatividade = self.findChild(QComboBox, "comboBox_rotatividade")
        self.textEdit_info_extra = self.findChild(QTextEdit, "textEdit_info_extra")
        self.pushButton_cadastrar = self.findChild(QPushButton, "pushButton_cadastrar")
        self.pushButton_limpar_tela = self.findChild(QPushButton, "pushButton_limpar_tela")
        self.pushButton_sair = self.findChild(QPushButton, "pushButton_sair")
        self.label_feedback = self.findChild(QLabel, "label_feedback")
        
        #actions of the buttons
        self.pushButton_limpar_tela.clicked.connect(self.limpar_tela)
        self.pushButton_cadastrar.clicked.connect(self.cadastrar_item)
        
        #comboBox Itens
        #categorias
        self.comboBox_categoria_do_item.insertItem(1, "Mouse")
        self.comboBox_categoria_do_item.insertItem(2, "Teclado")
        
        #fornecedores
        self.comboBox_fornecedor_item.insertItem(1, "Kabum")
        self.comboBox_fornecedor_item.insertItem(2, "Magalu")
        self.comboBox_fornecedor_item.insertItem(3, "Mercado Livre")
        
        #rotatividade
        self.comboBox_rotatividade.insertItem(1, "Nula")
        self.comboBox_rotatividade.insertItem(2, "Baixa")
        self.comboBox_rotatividade.insertItem(3, "Média")
        self.comboBox_rotatividade.insertItem(4, "Alta")
        self.comboBox_rotatividade.insertItem(5, "Urgente")
        
        #un de medida
        self.comboBox_un_medida_item.insertItem(1, "UN")
        self.comboBox_un_medida_item.insertItem(2, "M")
        self.comboBox_un_medida_item.insertItem(3, "CM")
        self.comboBox_un_medida_item.insertItem(4, "PR")
        self.comboBox_un_medida_item.insertItem(5, "DZ")
        self.comboBox_un_medida_item.insertItem(6, "MM")
        
        #closing the window
        self.pushButton_sair.clicked.connect(self.close)
        
    
    def limpar_tela(self):
        self.lineEdit_cod_item.clear()
        self.lineEdit_cod_barras_item.clear()
        self.lineEdit_descricao_do_item.clear()
        self.lineEdit_est_max_item.clear()
        self.lineEdit_est_min_item.clear()
        self.lineEdit_nome_do_item.clear()
        self.lineEdit_ponto_ressup.clear()
        self.lineEdit_qtde_atual_item.clear()
        self.lineEdit_setor_maior_saida_item.clear()
        self.lineEdit_valor_medio_item.clear()
        self.comboBox_categoria_do_item.setCurrentIndex(-1)
        self.comboBox_fornecedor_item.setCurrentIndex(-1)
        self.comboBox_rotatividade.setCurrentIndex(-1)
        self.comboBox_un_medida_item.setCurrentIndex(-1)
        self.textEdit_info_extra.clear()
        self.label_feedback.setText("CADASTRANDO ITENS...")
        
    def cadastrar_item(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Confirmação!")
        dialog.setText("Tem certeza que quer adicionar esse Item?")
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dialog.setIcon(QMessageBox.Icon.Question)
        
        response = dialog.exec()
        
        if response == QMessageBox.StandardButton.Yes:
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
                codItem = self.lineEdit_cod_item.text()
                nomeItem = self.lineEdit_nome_do_item.text()
                descItem = self.lineEdit_descricao_do_item.text()
                codbarrasItem = self.lineEdit_cod_barras_item.text()
                fornecedorItem = self.comboBox_fornecedor_item.currentText()
                unItem = self.comboBox_un_medida_item.currentText()
                qtdeatualItem = self.lineEdit_qtde_atual_item.text()
                estmaxItem = self.lineEdit_est_max_item.text()
                estminItem = self.lineEdit_est_min_item.text()
                pontoressupItem = self.lineEdit_ponto_ressup.text()
                valormedioItem = self.lineEdit_valor_medio_item.text()
                setorsaidaItem = self.lineEdit_setor_maior_saida_item.text()
                categoriaItem = self.comboBox_categoria_do_item.currentText()
                rotatividadeItem = self.comboBox_rotatividade.currentText()
                infoextraItem = self.textEdit_info_extra.toPlainText()
                # 15 itens data
                # the combobox and TextEdit use different ways to get the text
                
                
                #query to put the data in the database
                query = "INSERT INTO itens (codItem, nomeItem, descItem, codbarrasItem, fornecedorItem, unItem, qtdeatualItem, estmaxItem, estminItem, pontoressupItem, valormedioItem, setorsaidaItem, categoriaItem, rotatividadeItem, infoextraItem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (codItem, nomeItem, descItem, codbarrasItem, fornecedorItem, unItem, qtdeatualItem, estmaxItem, estminItem, pontoressupItem, valormedioItem, setorsaidaItem, categoriaItem, rotatividadeItem, infoextraItem) # this is the values to be inserted in the table.
                
                # executing the SQL command.
                mycursor.execute(query, values) # taking the values to be inserted and the SQL command.
                
                mydb.commit() # commiting the changes in the database.
                
                self.label_feedback.setText("Item: " + nomeItem + ", added successfully") # to give the feedback to the user.
            except mdb.Error as e:
                error_message = f"Error: {str(e)}"
                self.label_feedback.setText(error_message)
                print(error_message)
            except Exception as e:
                error_message = f"Unexpected error: {str(e)}"
                self.label_feedback.setText(error_message)
                print(error_message)
        else:
            self.label_feedback.setText("Item não inserido!")
                


# I use this part of code to teste, when I put to open with another windows, dont is necessary
'''
app = QApplication(sys.argv)
window = cadastro_de_item_UI()
window.show()
app.exec()'''