# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0.


while True:
    userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
    userGivenSsn = userGivenSsn.upper() # Varmistetaan, että tarkiste on isolla

    # TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä

    # TODO: Rakenna funktio, jolla kysytään nimet ja muutetaan yhdysnimet isoille alkukirjaimille -> reg exp

    ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            ssnToCheck.getDateOfBirth()
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()
            userGivenLastName = input('Syötä asiakkaan sukunimi: ')
            userGivenLastName = userGivenLastName.capitalize()
            userGivenFirstName = input('Syötä asiakkaan etunimi: ')
            userGivenFirstName = userGivenFirstName.capitalize()
            print('Asiakkaan nimi on:', userGivenLastName, userGivenFirstName)
            print('Syntymäaika: ', ssnToCheck.dateOfBirth)
            print('Sukupuoli: ', ssnToCheck.gender)
            print('Ikä: ', age)
        except Exception as e:
            print('Syöttämässäsi sosiaaliturvatunnuksessa oli virhe', e)


    # Kysytään halutaanko poistua ohjelmasta
    wantAbort = input('Haluatko päättää ohjelman k/E:')
    # Muutetaan vastaus isoksi kirjaimiksi ja tarkastetaan kirjain K
    if wantAbort.upper() == 'K':
        break

    # Käynnistetään videokuva ja ilmoitetaan sen käynnistymisestä äänimerkillä
    #sound.parametricBeep(400, 330)
    #sound.playWav('Alkaa.WAV')

