from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import *

from elements import MyMainWindow

class Menu:
    def __init__(self):
        super().__init__()
        self.window = MyMainWindow()
        self.menu_bar = self.window.menuBar()
        self.file_menu = self.menu_bar.addMenu("&Archivo")
        self.refresh_menu = self.menu_bar.addMenu("&Conversor Markdown")
        self.help_menu = self.menu_bar.addMenu("&Ayuda")
        
    def actions(self):
        # ============== New File ================= #
        self.action_new = QAction("&Nuevo")
        self.action_new.setShortcut(QKeySequence.New)
        self.action_new.triggered.connect(self.window.new)
        self.file_menu.addAction(self.action_new) 

        # ============== Open File ================= #
        self.action_open = QAction("&Abrir")
        self.action_open.setShortcut(QKeySequence.Open)
        self.action_open.triggered.connect(self.window.show_open_dialog)
        self.file_menu.addAction(self.action_open)   

        # ============== Save File ================= #
        self.action_save = QAction("&Guardar")
        self.action_save.setShortcut(QKeySequence.Save)
        self.action_save.triggered.connect(self.window.save)
        self.file_menu.addAction(self.action_save)

        # ============== Save File As ================= #
        self.action_saveas = QAction("&Guardar como")
        self.action_saveas.setShortcut(QKeySequence.SaveAs)
        self.action_saveas.triggered.connect(self.window.show_save_dialog)
        self.file_menu.addAction(self.action_saveas)
        
        # ============== Save File As ================= #
        self.action_close = QAction("&Cerrar")
        self.action_close.triggered.connect(self.window.close)
        self.file_menu.addAction(self.action_close)

        # ============== About ================= #
        self.action_about = QAction("&Acerca de")
        self.action_about.triggered.connect(self.window.show_about_dialog)
        self.help_menu.addAction(self.action_about)

        # ====== Refresh Markdown Converter ===== #
        self.action_refresh = QAction("&Actualizar")
        self.action_refresh.triggered.connect(self.window.markdown_converter)
        self.refresh_menu.addAction(self.action_refresh)

    