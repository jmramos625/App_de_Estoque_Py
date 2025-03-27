# We will load the UI file created in the previous part using the PyQt6 module.
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QPushButton, QLabel
from PyQt6.QtGui import QMovie, QIcon, QPixmap
from PyQt6.QtCore import QTime, QTimer, QDateTime
import sys
# to import the UI file, we use the uic module from PyQt6.
from PyQt6 import uic
from dotenv import set_key

#importing another window
from CasdastroDeItem import cadastro_de_item_UI #import the item registration
from CadastroDeSetores import cadastro_de_setores_UI #import the sectors registration
from CadastroDeFornecedores import cadastro_de_fornecedores_UI #import the suppliers registration

# we will do a class to call the UI file.
class main_windows_UI(QMainWindow):
    def __init__(self):
        super().__init__()
        # be attention to the path of the UI file. This most be the real path of the file.
        uic.loadUi("Apps\main_window.ui", self)
        
        
        # now we will get the objects from the UI file.
        self.pushButton_cadastro_de_itens_menu = self.findChild(QPushButton, "pushButton_cadastro_de_itens_menu")
        self.pushButton_cadastro_setores = self.findChild(QPushButton, "pushButton_cadastro_setores")
        self.pushButton_cadastro_fornecedores = self.findChild(QPushButton, "pushButton_cadastro_fornecedores")
        self.pushButton_cadastro_categorias = self.findChild(QPushButton, "pushButton_cadastro_categorias")
        self.pushButton_cadastro_un_medida = self.findChild(QPushButton, "pushButton_cadastro_un_medida")
        self.pushButton_cadastro_usuarios = self.findChild(QPushButton, "pushButton_cadastro_usuarios")
        
        self.label_horario = self.findChild(QLabel, "label_horario")
        
        #setting gif animation
        self.add_item_gif = QMovie("Images\\add_item2.gif")
        self.add_item_gif.frameChanged.connect(self.update_add_item_icon)
        self.add_item_gif.start()
        
        self.add_sectors_gif = QMovie("Images\\add_sectors.gif")
        self.add_sectors_gif.frameChanged.connect(self.update_add_sectors_icon)
        self.add_sectors_gif.start()
        
        self.add_fornecedor_gif = QMovie("Images\\add_fornecedor.gif")
        self.add_fornecedor_gif.frameChanged.connect(self.update_add_fornecedor_gif)
        self.add_fornecedor_gif.start()
        
        self.add_categorias_gif = QMovie("Images\\add_categories.gif")
        self.add_categorias_gif.frameChanged.connect(self.update_add_categories_icon)
        self.add_categorias_gif.start()
        
        self.add_un_medidas_gif = QMovie("Images\\add_un_medidas.gif")
        self.add_un_medidas_gif.frameChanged.connect(self.update_add_un_medidas_icon)
        self.add_un_medidas_gif.start()
        
        self.add_users_gif = QMovie("Images\\add_user.gif")
        self.add_users_gif.frameChanged.connect(self.update_add_users_icon)
        self.add_users_gif.start()
        
        #opening the window with the button
        self.pushButton_cadastro_de_itens_menu.clicked.connect(self.open_cadastro_de_item)
        self.pushButton_cadastro_setores.clicked.connect(self.open_cadastro_de_setores)
        self.pushButton_cadastro_fornecedores.clicked.connect(self.open_cadastro_de_fornecedores)
                
        #setting the timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1)
    
    
    #buttons and your functions
    def open_cadastro_de_item(self):
        self.cadastro_de_item_ui = cadastro_de_item_UI()
        self.cadastro_de_item_ui.show()
        
    def open_cadastro_de_setores(self):
        self.cadastro_de_setores_ui = cadastro_de_setores_UI()
        self.cadastro_de_setores_ui.show()
        
    def open_cadastro_de_fornecedores(self):
        self.cadastro_de_fornecedores_ui = cadastro_de_fornecedores_UI()
        self.cadastro_de_fornecedores_ui.show()
        
    #hours funcion
    def update_time(self):
        current_time = QDateTime.currentDateTime()
        time_text = current_time.toString('hh:mm:ss')
        day_of_week = current_time.toString('dddd')
        self.label_horario.setText(f'{day_of_week}, {time_text}')
    
    
    #functions about the gif
    def update_add_item_icon(self):
        self.pushButton_cadastro_de_itens_menu.setIcon(QIcon(QPixmap.fromImage(self.add_item_gif.currentImage())))
    
    def update_add_sectors_icon(self):
        self.pushButton_cadastro_setores.setIcon(QIcon(QPixmap.fromImage(self.add_sectors_gif.currentImage())))
        
    def update_add_fornecedor_gif(self):
        self.pushButton_cadastro_fornecedores.setIcon(QIcon(QPixmap.fromImage(self.add_fornecedor_gif.currentImage())))
    
    def update_add_categories_icon(self):
        self.pushButton_cadastro_categorias.setIcon(QIcon(QPixmap.fromImage(self.add_categorias_gif.currentImage())))

    def update_add_un_medidas_icon(self):
        self.pushButton_cadastro_un_medida.setIcon(QIcon(QPixmap.fromImage(self.add_un_medidas_gif.currentImage())))
    
    def update_add_users_icon(self):
        self.pushButton_cadastro_usuarios.setIcon(QIcon(QPixmap.fromImage(self.add_users_gif.currentImage())))
    
    

        

app = QApplication(sys.argv)
window = main_windows_UI()
window.show()
app.exec()