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


# TODO: Pääohjelman ikuinen silmukka, josta poistutaan tarvittaessa (keksi mekanismi itse)
# TODO:  Paranna pääohjelma siten, että se ei kaadu, kun käyttäjä syöttää virheellisen henkilötunnuksen
userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
userGivenLastName = input('Syötä asiakkaan sukunimi')
# TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä
userGivenFirstName = input('Syötä asiakkaan etunimi')
# TODO: Tee tarkistus siitä, että nimi ei voi olla tyhjä
# TODO: Varaudu tilanteeseen, jossa hetu:n tarkiste on annettu pienillä kirjaimilla
# TODO: Muuta syötettyjen nimien alkukirjain isoksi
userGivenFirstName = input('Syötä asiakkaan etunimi')

ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
if ssnToCheck.isValidSsn() == True:
    dateOfBirth = ssnToCheck.getDateOfBirth()
    gender = ssnToCheck.getGender()
    age = ssnToCheck.calculateAge()
    print('Syntymäaika: ', ssnToCheck.dateOfBirth)
    print('Sukupuoli: ', ssnToCheck.gender)
    print('Ikä: ', age)

# Käynnistetään videokuva ja ilmoitetaan sen käynnistymisestä äänimerkillä
#sound.parametricBeep(400, 330)
#sound.playWav('Alkaa.WAV')

