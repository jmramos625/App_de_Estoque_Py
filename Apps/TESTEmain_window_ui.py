# Form implementation generated from reading ui file 'c:\Users\W10\OneDrive\Study\Python\PyQT\App de Estoque\Apps\main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 627)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1136, 627))
        MainWindow.setMaximumSize(QtCore.QSize(1136, 627))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_cadastro_de_itens_menu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cadastro_de_itens_menu.setMinimumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_de_itens_menu.setMaximumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_de_itens_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\W10\\OneDrive\\Study\\Python\\PyQT\\App de Estoque\\Apps\\../Images/add_item2.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cadastro_de_itens_menu.setIcon(icon)
        self.pushButton_cadastro_de_itens_menu.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_cadastro_de_itens_menu.setAutoRepeat(True)
        self.pushButton_cadastro_de_itens_menu.setAutoExclusive(False)
        self.pushButton_cadastro_de_itens_menu.setAutoRepeatDelay(300)
        self.pushButton_cadastro_de_itens_menu.setAutoRepeatInterval(100)
        self.pushButton_cadastro_de_itens_menu.setObjectName("pushButton_cadastro_de_itens_menu")
        self.verticalLayout.addWidget(self.pushButton_cadastro_de_itens_menu)
        self.label_cadastro_de_itens_menu = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastro_de_itens_menu.setMinimumSize(QtCore.QSize(366, 90))
        self.label_cadastro_de_itens_menu.setMaximumSize(QtCore.QSize(366, 90))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(26)
        font.setBold(True)
        self.label_cadastro_de_itens_menu.setFont(font)
        self.label_cadastro_de_itens_menu.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_de_itens_menu.setObjectName("label_cadastro_de_itens_menu")
        self.verticalLayout.addWidget(self.label_cadastro_de_itens_menu)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_cadastro_setores = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cadastro_setores.setMinimumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_setores.setMaximumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_setores.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\W10\\OneDrive\\Study\\Python\\PyQT\\App de Estoque\\Apps\\../Images/add_sectors.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cadastro_setores.setIcon(icon1)
        self.pushButton_cadastro_setores.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_cadastro_setores.setAutoRepeat(True)
        self.pushButton_cadastro_setores.setAutoExclusive(False)
        self.pushButton_cadastro_setores.setAutoRepeatDelay(300)
        self.pushButton_cadastro_setores.setAutoRepeatInterval(100)
        self.pushButton_cadastro_setores.setObjectName("pushButton_cadastro_setores")
        self.verticalLayout_2.addWidget(self.pushButton_cadastro_setores)
        self.label_cadastro_de_setores = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastro_de_setores.setMinimumSize(QtCore.QSize(366, 90))
        self.label_cadastro_de_setores.setMaximumSize(QtCore.QSize(366, 90))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(26)
        font.setBold(True)
        self.label_cadastro_de_setores.setFont(font)
        self.label_cadastro_de_setores.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_de_setores.setObjectName("label_cadastro_de_setores")
        self.verticalLayout_2.addWidget(self.label_cadastro_de_setores)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line_3 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_cadastro_fornecedores = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cadastro_fornecedores.setMinimumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_fornecedores.setMaximumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_fornecedores.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("c:\\Users\\W10\\OneDrive\\Study\\Python\\PyQT\\App de Estoque\\Apps\\../Images/add_fornecedor.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cadastro_fornecedores.setIcon(icon2)
        self.pushButton_cadastro_fornecedores.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_cadastro_fornecedores.setAutoRepeat(True)
        self.pushButton_cadastro_fornecedores.setAutoExclusive(False)
        self.pushButton_cadastro_fornecedores.setAutoRepeatDelay(300)
        self.pushButton_cadastro_fornecedores.setAutoRepeatInterval(100)
        self.pushButton_cadastro_fornecedores.setObjectName("pushButton_cadastro_fornecedores")
        self.verticalLayout_3.addWidget(self.pushButton_cadastro_fornecedores)
        self.label_cadastro_de_fornecedores = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastro_de_fornecedores.setMinimumSize(QtCore.QSize(366, 90))
        self.label_cadastro_de_fornecedores.setMaximumSize(QtCore.QSize(366, 90))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(26)
        font.setBold(True)
        self.label_cadastro_de_fornecedores.setFont(font)
        self.label_cadastro_de_fornecedores.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_de_fornecedores.setWordWrap(True)
        self.label_cadastro_de_fornecedores.setObjectName("label_cadastro_de_fornecedores")
        self.verticalLayout_3.addWidget(self.label_cadastro_de_fornecedores)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(parent=self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_7.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_cadastro_categorias = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cadastro_categorias.setMinimumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_categorias.setMaximumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_categorias.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("c:\\Users\\W10\\OneDrive\\Study\\Python\\PyQT\\App de Estoque\\Apps\\../Images/add_categories.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cadastro_categorias.setIcon(icon3)
        self.pushButton_cadastro_categorias.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_cadastro_categorias.setAutoRepeat(True)
        self.pushButton_cadastro_categorias.setAutoExclusive(False)
        self.pushButton_cadastro_categorias.setAutoRepeatDelay(300)
        self.pushButton_cadastro_categorias.setAutoRepeatInterval(100)
        self.pushButton_cadastro_categorias.setObjectName("pushButton_cadastro_categorias")
        self.verticalLayout_4.addWidget(self.pushButton_cadastro_categorias)
        self.label_cadastro_de_categorias = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastro_de_categorias.setMinimumSize(QtCore.QSize(366, 90))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(26)
        font.setBold(True)
        self.label_cadastro_de_categorias.setFont(font)
        self.label_cadastro_de_categorias.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_de_categorias.setWordWrap(True)
        self.label_cadastro_de_categorias.setObjectName("label_cadastro_de_categorias")
        self.verticalLayout_4.addWidget(self.label_cadastro_de_categorias)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.line_4 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_2.addWidget(self.line_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.pushButton_cadastro_un_medida = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cadastro_un_medida.setMinimumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_un_medida.setMaximumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_un_medida.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("c:\\Users\\W10\\OneDrive\\Study\\Python\\PyQT\\App de Estoque\\Apps\\../Images/add_un_medidas.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cadastro_un_medida.setIcon(icon4)
        self.pushButton_cadastro_un_medida.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_cadastro_un_medida.setAutoRepeat(True)
        self.pushButton_cadastro_un_medida.setAutoExclusive(False)
        self.pushButton_cadastro_un_medida.setAutoRepeatDelay(300)
        self.pushButton_cadastro_un_medida.setAutoRepeatInterval(100)
        self.pushButton_cadastro_un_medida.setObjectName("pushButton_cadastro_un_medida")
        self.verticalLayout_5.addWidget(self.pushButton_cadastro_un_medida)
        self.label_cadastro_de_un_medida = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastro_de_un_medida.setMinimumSize(QtCore.QSize(366, 90))
        self.label_cadastro_de_un_medida.setMaximumSize(QtCore.QSize(366, 90))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(26)
        font.setBold(True)
        self.label_cadastro_de_un_medida.setFont(font)
        self.label_cadastro_de_un_medida.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_de_un_medida.setWordWrap(True)
        self.label_cadastro_de_un_medida.setObjectName("label_cadastro_de_un_medida")
        self.verticalLayout_5.addWidget(self.label_cadastro_de_un_medida)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)
        self.line_5 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_2.addWidget(self.line_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_cadastro_usuarios = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_cadastro_usuarios.setMinimumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_usuarios.setMaximumSize(QtCore.QSize(366, 180))
        self.pushButton_cadastro_usuarios.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("c:\\Users\\W10\\OneDrive\\Study\\Python\\PyQT\\App de Estoque\\Apps\\../Images/add_user.gif"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_cadastro_usuarios.setIcon(icon5)
        self.pushButton_cadastro_usuarios.setIconSize(QtCore.QSize(150, 150))
        self.pushButton_cadastro_usuarios.setAutoRepeat(True)
        self.pushButton_cadastro_usuarios.setAutoExclusive(False)
        self.pushButton_cadastro_usuarios.setAutoRepeatDelay(300)
        self.pushButton_cadastro_usuarios.setAutoRepeatInterval(100)
        self.pushButton_cadastro_usuarios.setObjectName("pushButton_cadastro_usuarios")
        self.verticalLayout_6.addWidget(self.pushButton_cadastro_usuarios)
        self.label_cadastro_de_usuarios = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_cadastro_de_usuarios.setMinimumSize(QtCore.QSize(366, 90))
        self.label_cadastro_de_usuarios.setMaximumSize(QtCore.QSize(366, 90))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(26)
        font.setBold(True)
        self.label_cadastro_de_usuarios.setFont(font)
        self.label_cadastro_de_usuarios.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_cadastro_de_usuarios.setObjectName("label_cadastro_de_usuarios")
        self.verticalLayout_6.addWidget(self.label_cadastro_de_usuarios)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.line_6 = QtWidgets.QFrame(parent=self.centralwidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_6.setObjectName("line_6")
        self.verticalLayout_7.addWidget(self.line_6)
        self.label_horario = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_horario.setFont(font)
        self.label_horario.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.label_horario.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_horario.setObjectName("label_horario")
        self.verticalLayout_7.addWidget(self.label_horario)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 22))
        self.menubar.setObjectName("menubar")
        self.menuCadastros = QtWidgets.QMenu(parent=self.menubar)
        self.menuCadastros.setObjectName("menuCadastros")
        self.menuRelat_rios = QtWidgets.QMenu(parent=self.menubar)
        self.menuRelat_rios.setObjectName("menuRelat_rios")
        self.menuItens = QtWidgets.QMenu(parent=self.menuRelat_rios)
        self.menuItens.setObjectName("menuItens")
        self.menuMovimenta_o = QtWidgets.QMenu(parent=self.menubar)
        self.menuMovimenta_o.setObjectName("menuMovimenta_o")
        self.menuEntrada = QtWidgets.QMenu(parent=self.menuMovimenta_o)
        self.menuEntrada.setObjectName("menuEntrada")
        self.menuSa_da = QtWidgets.QMenu(parent=self.menuMovimenta_o)
        self.menuSa_da.setObjectName("menuSa_da")
        MainWindow.setMenuBar(self.menubar)
        self.actionCadastro_de_Item = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_Item.setObjectName("actionCadastro_de_Item")
        self.actionCadastro_de_Setores = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_Setores.setObjectName("actionCadastro_de_Setores")
        self.actionCadastro_de_Fornecedores = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_Fornecedores.setObjectName("actionCadastro_de_Fornecedores")
        self.actionCadastro_de_Categorias = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_Categorias.setObjectName("actionCadastro_de_Categorias")
        self.actionCadastro_de_Un_de_Medida = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_Un_de_Medida.setObjectName("actionCadastro_de_Un_de_Medida")
        self.actionCadastro_de_Usu_rios = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_Usu_rios.setObjectName("actionCadastro_de_Usu_rios")
        self.actionCadastro_de_tipos_de_Movimenta_o = QtGui.QAction(parent=MainWindow)
        self.actionCadastro_de_tipos_de_Movimenta_o.setObjectName("actionCadastro_de_tipos_de_Movimenta_o")
        self.actionValores_Gerais = QtGui.QAction(parent=MainWindow)
        self.actionValores_Gerais.setObjectName("actionValores_Gerais")
        self.actionFornecedores = QtGui.QAction(parent=MainWindow)
        self.actionFornecedores.setObjectName("actionFornecedores")
        self.actionUsu_rios = QtGui.QAction(parent=MainWindow)
        self.actionUsu_rios.setObjectName("actionUsu_rios")
        self.actionCategorias = QtGui.QAction(parent=MainWindow)
        self.actionCategorias.setObjectName("actionCategorias")
        self.actionUnidades_de_Medida = QtGui.QAction(parent=MainWindow)
        self.actionUnidades_de_Medida.setObjectName("actionUnidades_de_Medida")
        self.actionValores_Gerais_2 = QtGui.QAction(parent=MainWindow)
        self.actionValores_Gerais_2.setObjectName("actionValores_Gerais_2")
        self.actionItens_INFO = QtGui.QAction(parent=MainWindow)
        self.actionItens_INFO.setObjectName("actionItens_INFO")
        self.actionValores_Gerais_3 = QtGui.QAction(parent=MainWindow)
        self.actionValores_Gerais_3.setObjectName("actionValores_Gerais_3")
        self.actionItens_X_Fornecedores = QtGui.QAction(parent=MainWindow)
        self.actionItens_X_Fornecedores.setObjectName("actionItens_X_Fornecedores")
        self.actionItens_X_Categorias = QtGui.QAction(parent=MainWindow)
        self.actionItens_X_Categorias.setObjectName("actionItens_X_Categorias")
        self.actionSetores = QtGui.QAction(parent=MainWindow)
        self.actionSetores.setObjectName("actionSetores")
        self.actionTipos_de_Movimenta_o = QtGui.QAction(parent=MainWindow)
        self.actionTipos_de_Movimenta_o.setObjectName("actionTipos_de_Movimenta_o")
        self.actionEntrada_de_Item = QtGui.QAction(parent=MainWindow)
        self.actionEntrada_de_Item.setObjectName("actionEntrada_de_Item")
        self.actionAjuste_Positivos = QtGui.QAction(parent=MainWindow)
        self.actionAjuste_Positivos.setObjectName("actionAjuste_Positivos")
        self.actionAloca_o_em_Setor = QtGui.QAction(parent=MainWindow)
        self.actionAloca_o_em_Setor.setObjectName("actionAloca_o_em_Setor")
        self.actionAjustes_Negativos = QtGui.QAction(parent=MainWindow)
        self.actionAjustes_Negativos.setObjectName("actionAjustes_Negativos")
        self.actionPerda = QtGui.QAction(parent=MainWindow)
        self.actionPerda.setObjectName("actionPerda")
        self.actionDevolu_o = QtGui.QAction(parent=MainWindow)
        self.actionDevolu_o.setObjectName("actionDevolu_o")
        self.menuCadastros.addAction(self.actionCadastro_de_Item)
        self.menuCadastros.addAction(self.actionCadastro_de_Setores)
        self.menuCadastros.addAction(self.actionCadastro_de_Fornecedores)
        self.menuCadastros.addAction(self.actionCadastro_de_Categorias)
        self.menuCadastros.addAction(self.actionCadastro_de_Un_de_Medida)
        self.menuCadastros.addAction(self.actionCadastro_de_Usu_rios)
        self.menuCadastros.addAction(self.actionCadastro_de_tipos_de_Movimenta_o)
        self.menuItens.addAction(self.actionItens_INFO)
        self.menuItens.addAction(self.actionValores_Gerais_3)
        self.menuItens.addAction(self.actionItens_X_Fornecedores)
        self.menuItens.addAction(self.actionItens_X_Categorias)
        self.menuRelat_rios.addAction(self.menuItens.menuAction())
        self.menuRelat_rios.addAction(self.actionFornecedores)
        self.menuRelat_rios.addAction(self.actionUsu_rios)
        self.menuRelat_rios.addAction(self.actionCategorias)
        self.menuRelat_rios.addAction(self.actionUnidades_de_Medida)
        self.menuRelat_rios.addAction(self.actionSetores)
        self.menuRelat_rios.addAction(self.actionTipos_de_Movimenta_o)
        self.menuEntrada.addAction(self.actionEntrada_de_Item)
        self.menuEntrada.addAction(self.actionAjuste_Positivos)
        self.menuSa_da.addAction(self.actionAloca_o_em_Setor)
        self.menuSa_da.addAction(self.actionAjustes_Negativos)
        self.menuSa_da.addAction(self.actionPerda)
        self.menuSa_da.addAction(self.actionDevolu_o)
        self.menuMovimenta_o.addAction(self.menuEntrada.menuAction())
        self.menuMovimenta_o.addAction(self.menuSa_da.menuAction())
        self.menubar.addAction(self.menuCadastros.menuAction())
        self.menubar.addAction(self.menuRelat_rios.menuAction())
        self.menubar.addAction(self.menuMovimenta_o.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_cadastro_de_itens_menu.setText(_translate("MainWindow", "Cadastro de Itens"))
        self.label_cadastro_de_setores.setText(_translate("MainWindow", "Cadastro de Setores"))
        self.label_cadastro_de_fornecedores.setText(_translate("MainWindow", "Cadastro de Fornecedores"))
        self.label_cadastro_de_categorias.setText(_translate("MainWindow", "Cadastro de Categorias"))
        self.label_cadastro_de_un_medida.setText(_translate("MainWindow", "Cadastro de                   Un. de Medida"))
        self.label_cadastro_de_usuarios.setText(_translate("MainWindow", "Cadastro de Usuários"))
        self.label_horario.setText(_translate("MainWindow", "HORARIO"))
        self.menuCadastros.setTitle(_translate("MainWindow", "Cadastros"))
        self.menuRelat_rios.setTitle(_translate("MainWindow", "Relatórios"))
        self.menuItens.setTitle(_translate("MainWindow", "Itens"))
        self.menuMovimenta_o.setTitle(_translate("MainWindow", "Movimentação"))
        self.menuEntrada.setTitle(_translate("MainWindow", "Entrada"))
        self.menuSa_da.setTitle(_translate("MainWindow", "Saída"))
        self.actionCadastro_de_Item.setText(_translate("MainWindow", "Cadastro de Item"))
        self.actionCadastro_de_Setores.setText(_translate("MainWindow", "Cadastro de Setores"))
        self.actionCadastro_de_Fornecedores.setText(_translate("MainWindow", "Cadastro de Fornecedores"))
        self.actionCadastro_de_Categorias.setText(_translate("MainWindow", "Cadastro de Categorias"))
        self.actionCadastro_de_Un_de_Medida.setText(_translate("MainWindow", "Cadastro de Un. de Medida"))
        self.actionCadastro_de_Usu_rios.setText(_translate("MainWindow", "Cadastro de Usuários"))
        self.actionCadastro_de_tipos_de_Movimenta_o.setText(_translate("MainWindow", "Cadastro de tipos de Movimentação"))
        self.actionValores_Gerais.setText(_translate("MainWindow", "Valores Gerais"))
        self.actionFornecedores.setText(_translate("MainWindow", "Fornecedores"))
        self.actionUsu_rios.setText(_translate("MainWindow", "Usuários"))
        self.actionCategorias.setText(_translate("MainWindow", "Categorias"))
        self.actionUnidades_de_Medida.setText(_translate("MainWindow", "Unidades de Medida"))
        self.actionValores_Gerais_2.setText(_translate("MainWindow", "Valores Gerais"))
        self.actionItens_INFO.setText(_translate("MainWindow", "Itens (INFO)"))
        self.actionValores_Gerais_3.setText(_translate("MainWindow", "Valores Gerais"))
        self.actionItens_X_Fornecedores.setText(_translate("MainWindow", "Itens X Fornecedores"))
        self.actionItens_X_Categorias.setText(_translate("MainWindow", "Itens X Categorias"))
        self.actionSetores.setText(_translate("MainWindow", "Setores"))
        self.actionTipos_de_Movimenta_o.setText(_translate("MainWindow", "Tipos de Movimentação"))
        self.actionEntrada_de_Item.setText(_translate("MainWindow", "Compra/Entrada"))
        self.actionAjuste_Positivos.setText(_translate("MainWindow", "Ajuste Positivos"))
        self.actionAloca_o_em_Setor.setText(_translate("MainWindow", "Alocação em Setor"))
        self.actionAjustes_Negativos.setText(_translate("MainWindow", "Ajustes Negativos"))
        self.actionPerda.setText(_translate("MainWindow", "Perda"))
        self.actionDevolu_o.setText(_translate("MainWindow", "Devolução"))
