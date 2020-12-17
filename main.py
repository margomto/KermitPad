import sys
from PyQt5.QtWidgets import QApplication


from menu import Menu
from elements import MyMarkdownBrowser


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Kermit Pad')
    app.setStyle('Fusion')
    menu = Menu()
    menu.actions()
    menu.window.markdown_converter()
    menu.window.show()
    sys.exit(app.exec())