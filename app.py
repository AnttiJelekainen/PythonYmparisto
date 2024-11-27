# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound  # Äänimerkit ja äänitiedostot
from avtools import video  # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1  # Ensimmäinen kamera on aina 0.

# FUNKTIOT
# ----------



def askName(question: str) -> str:
    """Prompts user to answer a question and converts the answer to title and removes white space

    Args:
        question (str): Prompt to user

    Returns:
        str: modifies answer
    """
    name = ''
    while name == '':
        question = question + ': '
        name = input(question).strip()
    name = name.title()
    return name

if __name__ == "__main__":

    # PÄÄOHJELMAN IKUINEN SILMUKKA
    # =============================
    while True:

        # Alustetaan muuttujat tyhjiksi
        userGivenSsn = ''
        userGivenLastName = ''
        userGivenFirstName = '' 

        # Kysytään asiakkaan henkilötunnus ja muutetaan kirjaimet isoksi
        userGivenSsn = input('Syötä asiakkaan henkilötunnus')
        userGivenSsn = userGivenSsn.upper()  # Varmistetaan, että tarkiste on isolla

        # Luodaan syötetystä henkilötunnuksesta NationalSSN-objekti
        ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)

        # Tarkistetaan onko henkilötunnus oikein muodostettu
        if ssnToCheck.isValidSsn() == True:

            # Virheenkäsittely, mahdollisen vuosisatakoodivirheen varalta
            try:
                ssnToCheck.getDateOfBirth()  # Asetetaan syntymäaika ominaisuus
                ssnToCheck.getGender()  # Asetetaan sukupuoliominaisuus
                age = ssnToCheck.calculateAge()  # Lasketaan ikä tänään

                # Kysytään loput tiedot, jos ei virhettä
                userGivenLastName = askName('Asiakkaan sukunimi')
                userGivenFirstName = askName('Asiakkaan etunimi')

                # Tulostetaan tiedot ruudulle
                print('Asiakkaan nimi on:', userGivenLastName, userGivenFirstName)
                print('Syntymäaika: ', ssnToCheck.dateOfBirth)
                print('Sukupuoli: ', ssnToCheck.gender)
                print('Ikä: ', age)

            # Virhetilanteessa näytetään virheilmoitus
            except Exception as e:
                print('Syöttämässäsi sosiaaliturvatunnuksessa oli virhe:', e)

        else:
            print('Henkilötunnuksessa virhe, syötä tunnus uudelleen: ')

        # Kysytään halutaanko poistua ohjelmasta
        wantToAbort = input('Haluatko päättää ohjelman k/E:')
        # Muutetaan vastaus isoksi kirjaimiksi ja tarkastetaan kirjain K
        if wantToAbort.upper() == 'K':
            break
