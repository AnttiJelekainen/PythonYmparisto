# YKSIKKÖTESTIT MODUULILLE identityCheck.py

import identityCheck

def test_opiskelijanumeroOk_kirjain():
    assert identityCheck.opiskelijanumeroOk('12X45') == False

def test_opiskelijanumeroOk_6():
    assert identityCheck.opiskelijanumeroOk('123456') == True
def test_opiskelijanumeroOk_4():
    assert identityCheck.opiskelijanumeroOk('1234') == False
def test_opiskelijanumeroOk_7():
    assert identityCheck.opiskelijanumeroOk('1234567') == False
def test_opiskelijanumeroOk_5():
    assert identityCheck.opiskelijanumeroOk('12345') == True

def test_opiskelijanumeroOk_desimaali1():
    assert identityCheck.opiskelijanumeroOk('12.45') == False

def test_opiskelijanumeroOk_desimaali2():
    assert identityCheck.opiskelijanumeroOk('12,45') == False

# TODO: Tee testit HeTua varten ja vasta sitten kirjoita koodi

# Henkilötunnus esimerkki 130728-478N testataan
# 1. Pituus 
# 2. Syntymäaikaosan oikeellisuus
# 3. Vuosisatakoodit +, - ja A
# 4. Modulo 31 tarkistus