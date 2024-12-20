# PYSIDE6-MALLINNE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# =================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET

import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# Luodaan käyttöliittymätiedoston lataajaobjekti QUiloader-luokasta
loader = QUiLoader()

# Määritellään sovellusobjekti
app = QtWidgets.QApplication(sys.argv)

# Luodaan pääikkunan objekti ui-tiedoston perusteella, pääikkunalla ei ole isäntäobjektia
window = loader.load("mainWindow.ui", None)

statusBar = window.findChild(QtWidgets.QStatusBar, 'statusbar')
if statusBar != None:
    statusBar.showMessage('Kaikki hyvin', -1)

# Asetetaan pääikkunan nimi
window.setWindowTitle("PÄÄIKKUNA ON TÄMÄ")
label = window.findChild(QtWidgets.QLabel, 'label')
if label != None:
    label.setText('Muutettu teksti')

# Määritellään ikkunan näkyväksi
window.show()

# Ajetaan sovellus
app.exec()

