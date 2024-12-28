# LABORATORIOETIKETTISOVELLUKSEN PÄÄIKKUNAN
# LUOMINEN Labra_ui.py TIEDOSTON PERUSTEELLA
# =========================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets
from labra_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

import identityCheck2 # Henkilötunnuksen tarkistukseen liittyvät työkalut
import barcode # Viivakoodin muodostukseen tarvittavat rutiinit
from avtools import sound # Äänitoiminnot

# Määritellään luokka, joka perii Qmainwindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""

    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()
        
        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindown ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta.
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # OHJELMOIDUT SIGNAALIT
        # ---------------------

        # Kun poistutaan ssnLineEdit-elementistä suoritetaan barcodeLabel-elementin päivitys
        self.ui.ssnLineEdit.editingFinished.connect(self.updateBarcodeLabel)

        # Siistitään etunimi- ja sukunimielementit poistuttaessa
        self.ui.firstNameLineEdit.editingFinished.connect(self.beautifyFirstName)
        self.ui.lastNameLineEdit.editingFinished.connect(self.beautifyLastName)

        # Aktivoidaan tulostuspainiken sen jälkeen kun etikettin määrä on säädetty
        self.ui.amountSpinBox.valueChanged.connect(self.enablePrintButton)

    

    # OHJELMOIDUT SLOTIT
    #-------------------

    # Viivakoodin muodostus ja barcodeLabel:n päivitys
    def updateBarcodeLabel(self):
        # Tarkistetaan, että henkilötunnus on oikein muodostettu
        uiSsn = self.ui.ssnLineEdit.text().upper() # Luetaan käyttöliittymästä henkilötunnus
        ssnToCheck = identityCheck2.NationalSSN(uiSsn) # Luodaan henkilötunnusobjekti
        self.ui.ssnLineEdit.setText(uiSsn) # Päivitetään myös syöyttökenttä isoihin kirjaimiin

        # Jos se on oikein, luodaan viivakoodi
        if ssnToCheck.isValidSsn():
            barcode128 = barcode.Code128B(uiSsn) # Luodaan viivakoodi-olio
            barCodeToPrint = barcode128.buildBarcode() # Lisätään alku- ja loppumerkki sekä varmistusssumma
            self.ui.barcodeLabel.setText(barCodeToPrint) # Päivitetään käyttöliittymän barcodeLabel

        # Jos se on muodostettu väärin näytetään virheilmoitus MessageBox-ikkunassa
        else:
            self.errorTitle = 'Henkilötunnus virheellinen'
            self.errorText = ssnToCheck.errorMessage
            self.openErrorMsgBox(self.errorTitle, self.errorText)

    def beautifyFirstName(self):
        firstName = self.ui.firstNameLineEdit.text()
        firstName = firstName.strip() # Poistetaan ylimääräiset tyhjät välit tms
        firstName = firstName.title() # Muutetaan isot alkukirjaimet
        self.ui.firstNameLineEdit.setText(firstName) # Päivitetään elementti

    def beautifyLastName(self):
        lastName = self.ui.lastNameLineEdit.text()
        lastName = lastName.strip()  # Poistetaan ylimääräiset tyhjät välit tms
        lastName = lastName.title()  # Muutetaan isot alkukirjaimet
        self.ui.lastNameLineEdit.setText(lastName)  # Päivitetään elementti

    # Aktivoidaan tulostuspainike
    def enablePrintButton(self):
        self.ui.printPushButton.setEnabled(True)

    # Virheilmoitusikkuna
    def openErrorMsgBox(self, errorTitle, errorText):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle(errorTitle)
        msgBox.setText(errorText)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()

    # TODO: Tulostuspainike aktiiviseksi vain, kun kaikki tiedot on täytetty ja OK -> disabled oletus, kun kaikki tiedot -> enabled

    # TODO: Lisää tilariville tiedot asiakkaasta tyyliin:
    # Asiakas on 96-vuotias nainen

if __name__ == "__main__":

    # Luodaan sovellus, jossa on käyttöjärjestelmästä riippumaton ulkonäkö (Fusion)
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    # Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
    window = MainWindow()
    window.show()

    # Käynnistetään sovellus ja tapahtumienkäsittelijä
    app.exec()
