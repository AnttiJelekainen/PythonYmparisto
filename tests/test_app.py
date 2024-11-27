# PÄÄOHJELMAN TESTIT
# ==================

# Tuodaan testattava moduuli
import app

# Testitapaus 1 pienellä kirjoitettu nimi tulee isolla:
def test_smallInput(monkeypatch):
    simulatedInput = 'antti-ville' # Simuloitu käyttäjän syöte

    # Lähetetään simuloitu syöte monkeypatch:n avulla funktiolle
    monkeypatch.setattr('builtins.input', lambda _: simulatedInput)
    assert app.askName('Etunimi') == 'Antti-Ville'