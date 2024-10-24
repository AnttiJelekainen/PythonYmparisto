# Kokeillaan luokkia ja olioita

# LUOKKIA

# Yliluokka (parent class, mother class, superclass..)
class Henkilo:

    # Konstruktori(metodi), jonka avulla luodaan uusi Henkilö-olio
    # Oliota luotaessa etunimi ja sukunimi ovat pakollisia tietoja
    def __init__(self, etunimi, sukunimi):
        self.etunimi = etunimi
        self.sukunimi = sukunimi

        # Oliolla on myös muita ominaisuuksia, joita ei määritellä olion luomisen yhteydessä
        self.ika = 0 # Oletusikä 0 
        self.kaupunki = "" # Asuinkaupunki tyhjä
        self.harrastus = [] # harratukset tyhjä lista

# Aliluokka (Child class, daughter class, subclass..) perii (inherit) Henkilö-luokan
class Opiskelija(Henkilo):

    # Oliota luotaessa pakollisia ovat etunimi ja sukunimi (koska pakollisia)
    # yliluokassa Henkilö sekä ryhmä
    # Metodi joka muodostaa opiskelija-olion
    def __init__(self, etunimi, sukunimi, ryhma): # Metodi joka muodostaa opiskelija-olion
        super().__init__(etunimi, sukunimi) # Kertoo, että yliluokassa on määritelty etunimen ja sukunimen käsittely
        self.ryhma = ryhma # Tämän parametrin käsittelyä ei ole kerrottu yliluokassa

# Aliluokka (Child class, daughter class, subclass..) perii (inherit) Henkilö-luokan
class Opettaja(Henkilo):
    def __init__(self, etunimi, sukunimi, aine):
        super().__init__(etunimi, sukunimi)
        self.aine = aine

# Aliluokka (Child class, daughter class, subclass..) perii (inherit) Henkilö-luokan
class Oppivelvollinen(Opiskelija):
    def __init__(self, etunimi, sukunimi, ryhma, paattyy):
        super().__init__(etunimi, sukunimi, ryhma)
        self.paattyy = paattyy

if __name__ == "__main__":

    # Johdetaan (instantiate) luokasta Henkilo olio rehtori
    rehtori = Henkilo('Reijo', 'Rantanen')
    rehtori.harrastus = ['sulkapallo', 'kaunokirjallisuus']

    # Luodaan olio opiskelija
    opiskelija = Opiskelija('Jakke', 'Jayna', 'Tivi20oA')
    opiskelija.harrastus = ['Kokkaaminen', 'Punttisali']

    # Luodaan olio Oppivelvollinen-luokasta
    oppivelvollinen = Oppivelvollinen('Jonne', 'Janttari', 'Tivi24A', '2027-05-02')
    oppivelvollinen.harrastus = ['Velttoilu']

    print(f"koulun rehtorina toimii {rehtori.etunimi} {rehtori.sukunimi}")

    print('Rehtori harrastaa', rehtori.harrastus)

    print('Jakke Jäynä harrastaa', opiskelija.harrastus)

    print ('Jonne harrastaa', oppivelvollinen.harrastus)