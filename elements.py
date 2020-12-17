import os
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from markdown2 import Markdown, markdown

file_path = None

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Kermit Pad')
        self.text = QPlainTextEdit() 
        self.text.setMinimumWidth(300)
        self.setCentralWidget(self.text)
        self.mk = MyMarkdownBrowser(self)
        
        
    def new(self):
        global file_path
        if self.save_if_modified():
            self.text.clear()
            file_path = None

    def confirmation_dialog(self):
        return QMessageBox.question(
            self, "Confirmación",
            "Tienes cambios sin guardar. ¿Seguro que quieres salir?",
            QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel,
            QMessageBox.Save
            ) 

    def save_if_modified(self):
        if self.text.document().isModified():
            answer = self.confirmation_dialog()
            if answer == QMessageBox.Save:
                self.save()
                return False
            elif  answer == QMessageBox.Cancel:
                return False
            return True
            
    def show_open_dialog(self):
        global file_path
        filename, _ = QFileDialog.getOpenFileName(self,  
                        "Abrir fichero...",
                        os.getcwd(),
                         "Ficheros de texto(*.txt *.py)")
        if filename:
            with open(filename, 'r') as f:
                self.text.setPlainText(f.read())
            file_path = filename

    def save(self):
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.text.toPlainText())
            self.text.document().setModified(False)
        else:
            self.show_save_dialog()

    def show_save_dialog(self):
        global file_path
        filename, _ = QFileDialog.getSaveFileName(self,
                        "Guardar fichero...",
                        os.getcwd(),
                         "Ficheros de texto(*.txt *.py)")
        if filename:
            with open(filename, 'w') as f:
                f.write(self.text.toPlainText())
        self.text.document().setModified(False)
        file_path = filename        

    def closeEvent(self, evt):
        if self.text.document().isModified():
            answer = self.confirmation_dialog()
            if answer == QMessageBox.Save:
                self.save()
            elif answer == QMessageBox.Discard:
                evt.accept()
            else:
                evt.ignore()

    def show_about_dialog(self):
        text = '''
            <center>
            <h2> Kermit Pad </h2>
            <br>
            <img src='img/kermit.jpg'>
            </center>
            <h4>Version 0.0.1</h4>
            <p>Copyright </p>
        '''
        QMessageBox.about(self, "Acerca de KermitPad...", text) 

    def markdown_converter(self):     
        my_markdown = Markdown()
        new_text = self.text.toPlainText()
        mk_to_html = my_markdown.convert(new_text)
        if '<p>' in new_text or '|' in new_text or '^'  in new_text  or '~'  in new_text:
            html_error = '''
            <p> No ha podido generarse ningún código HTML. <br>
            Revise que su texto existe y tiene el formato correcto. </p> 
            <p> Recuerde que no es posible traducir correctamente: 
            <ul>
                <li>Etiquetas como &lt;p&gt</li>
                <li>Emojis</li>
                <li>Tablas</li>
                <li>Texto tachado</li>
                <li>Superíndices y subíndices</li>

            </ul>
            '''
            self.mk.viewer.setHtml(html_error)
        else:    
            self.mk.viewer.setHtml(mk_to_html)               

class MyMarkdownBrowser(QWebEngineView):
    def __init__(self, window):
        super().__init__()
        self.viewer = QWebEngineView()
        self.browser = QDockWidget('Kermit Browser', window)
        self.browser.toggleViewAction()
        self.browser.setWidget(self.viewer)
        window.addDockWidget(Qt.RightDockWidgetArea, self.browser)        