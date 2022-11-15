from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import *

app = QApplication([])

class qt(QWidget):
    def __init__(self):
        super(qt, self).__init__()
        main_layout = QHBoxLayout()
        self.setLayout(main_layout)
        button = QPushButton("getInt")
        button.clicked.connect(self.show_get_int_dialog)
        main_layout.addWidget(button)
        app.setQuitOnLastWindowClosed(False)

    def show_get_int_dialog(self):
        port, ok = QInputDialog.getInt(self, "Port", "input port number:")

        if ok:
            print("input is port is:", port)
            return port


    def taskbar_ico(self):
        # Create the icon
        icon = QIcon("keybOardSC.png")

        # Create the tray
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)

        # Create the menu
        menu = QMenu()
        menu1 = QAction(self)
        menu.addAction(menu1)

        # Add a Quit option to the menu.
        quit = QAction("Quit")
        quit.triggered.connect(app.quit)
        menu.addAction(quit)

        # Add the menu to the tray
        tray.setContextMenu(menu)

        app.exec_()

    # def change_menu_text(self):
    #     menu1.setText(self)
