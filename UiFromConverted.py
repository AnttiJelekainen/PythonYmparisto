# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets
from MainWindow import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii Qmainwindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""

    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.setupUi(self)


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()
