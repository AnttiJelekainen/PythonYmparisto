# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# ==================================

# KIRJASTOT
#------------

# ASETUKSET
#------------
def barCodeValue(character: str) -> int:
    """Calculates a value of character used in Code128B barcode generation

    Args:
        character (_type_): a single character to convert

    Returns:
        int: Code128B value for calculating checksum    
    """
    asciiValue = ord(character)
    code128BValue = asciiValue - 32
    return code128BValue

def calculateCode128BChecksum(text: str) -> int:
    """Calculates a checksum for a given string

    Args:
        text (str): text string to use in a barcode

    Returns:
        int: modulo 103 checksum of weighted values
    """

    text = text.strip()
    numberOfLetters = len(text)
    weightedSum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1)
        weightedSum = weightedSum + weightedValue
    weightedSum += 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum

#TODO: Tee tämä funktio loppuun ja testaa sitä Notepadissa
def createCode128B(text: str) -> str:
    """Creates a complete code128B barcode to be printed using Libre Code 128 font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128Barcodestring = ''
    return code128BarcodeString

if __name__ == "__main__":
    testString = '128B'
    print(f"Painotetut arvot yhteensä: {calculateCode128BChecksum(testString)}")