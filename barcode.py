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

    text = text.strip() # Poistetaan ylimääräiset tyhjät merkit alusta ja lopusta
    numberOfLetters = len(text)
    weightedSum = 0 # Alustetaan summa tyhjäksi

    # Käydään teksti kirjaimittain läpi
    for number in range(numberOfLetters):
        letter = text[number]
        
        # Kutsutaan funktiota, joka palauttaa 128-koodin arvon
        code128BValue = barCodeValue(letter)

        # Lasketaan sijainnilla painotettu arvo
        weightedValue = code128BValue * (number + 1)

        # Lisätään se summaan
        weightedSum = weightedSum + weightedValue

    # Lisätään alkumerkin arvo silmukan jälkeen
    weightedSum += 104 
    
    # Lasketaan jakojäännös mod 103
    code128BChecksum = weightedSum % 103
    return code128BChecksum

def createCode128B(text: str) -> str:
    """Creates a complete code128B barcode to be printed using Libre Code 128B font

    Args:
        text (str): The text for a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BarcodeString = ''
    startChar = chr(204)
    stopChar = chr(206)
    checkSum = calculateCode128BChecksum(text)
    checkSumSymbol = chr(checkSum + 32)
    code128BarcodeString = startChar + text + checkSumSymbol + stopChar
    return code128BarcodeString

#LUOKKA VIIVAKOODEILLE
# ====================

class Code128B():
    """Generates Code128B barcodes. Suppoerts variants common, uncommon and Barcodesoft"""
    def __init__(self, text: str, variant:str ='Common') -> None:
        """Checks if text contains only valid characters for Code128B barcode.

        Args:
            text (str): A text string to be converted into a barcode
            variant (str, optional): Variant of code128. Valid values: Common, Uncommon and Barcodesoft. Defaults to 'Common'.
        """
        self.text = text
        self.variant = variant
        self.validRangeAll = range(33,126)
        self.ValidRangeCommon = range(195,202)
        self.validRangeUncommon = range(200,207)
        self.validRangeBarcodesoft = range(240,247)
        self.commonSpecialChar = (32, 194,207)
        self.uncommonSpecialChar = 212
        self.barcodesoftSpecialChar = 252

    def checkValidityOfText(self) -> bool | None:
        textLenght = len(self.text)
        isValid = False
        if self.variant == 'Common':
            for index in range(textLenght):
                character = self.text[index]
                characterValue = ord(character)
                if characterValue in self.validRangeAll or characterValue in self.ValidRangeCommon or characterValue in self.commonSpecialChar:
                    isValid = True
                else:
                    errorMessage = 'Text string contains invalid characters ' + '(' + character + ')'
                    raise ValueError(errorMessage)


        elif self.variant == 'Uncommon':
            for index in range(textLenght):
                character = self.text[index]
                characterValue = ord(character)
                if characterValue in self.validRangeAll or characterValue in self.validRangeUncommon or characterValue == self.uncommonSpecialChar:
                    isValid = True
                else:
                    errorMessage = 'Text string contains invalid characters ' + '(' + character + ')'
                    raise ValueError(errorMessage)
        elif self.variant == 'Barcodesoft':
            for index in range(textLenght):
                character = self.text[index]
                characterValue = ord(character)
                if characterValue in self.validRangeAll or characterValue in self.validRangeBarcodesoft or characterValue == self.barcodesoftSpecialChar:
                    isValid = True
                else:
                    errorMessage = 'Text string contains invalid characters ' + '(' + character + ')'
                    raise ValueError(errorMessage)
        else:
            errorMessage = 'Invalid variant ' + '(' + self.variant + '): Common, Uncommon and BarcodeSoft supported'
            raise ValueError(errorMessage)


        return isValid
    
    # Metodi, joka tuottaa viivakoodin sisällön
    def buildBarcode(self) -> str:
        """Returns a string presentation of the barcode

        Returns:
            str: barcode with start symbol, text, checksum symbol and stop symbol
        """
        rawText = self.text
        variant = self.variant
        startValues = {'Common': 204, 'Uncommon': 209, 'Barcodesoft': 249}
        stopValues = {'Common': 206, 'Uncommon': 211, 'Barcodesoft': 251}
        subtractValues = {'Common': 100, 'Uncommon': 105, 'Barcodesoft': 145}

        # Katsotaan onko tekstissä pelkästään sallittuja merkkejä
        if self.checkValidityOfText() == True:
            rawTextLenght = len(rawText)
            weightedSum = 0

            # Käydään merkkijono silmukassa läpi ja lasketaan varmistussumman arvot
            for index in range(rawTextLenght):
                character = rawText[index]
                characterValue = ord(character)

                # Normaalit merkit 32 - 126, alle 32 ei tarvitse enää huomioida
                if characterValue < 127:
                    value = characterValue -32 # Tätä arvoa käytetään varmistussumman laskennassa
                
                # Erikoismerkit, joiden arvo on 0
                elif characterValue in (194, 207, 212, 252):
                    value = 0

                # Varianttien erikoismerkit, rajat tarkistettu jo aiemmin 
                else:
                    value = characterValue - subtractValues[variant]

                # Kirjaimen painotetun arvon lisääminen, huom indeksi alkaa 0:sta, kertoimet 1:stä
                weightedSum = weightedSum + (index +1) * value

            # Alkumerkin sisältävä painotettu summa
            weightedSum = weightedSum + startValues[variant] - subtractValues[variant]

            # Lopullinen varmistussumma jakojäännös 103:lla jaettaessa
            checksum = weightedSum % 103

            # Generoidaan lopullinen viivakoodi alkumerkki + raakateksti + varmistussumma + loppumerkki
            startChar = chr(startValues[variant])
            stopChar = chr(stopValues[variant])
            checksumChar = chr(checksum + 32)
            barcode = startChar + rawText + checksumChar + stopChar

        return barcode
            

if __name__ == "__main__":
    testi = Code128B('128B')
    try:
        tulos = testi.checkValidityOfText()
        print(testi.text, 'on kelvollinen viivakoodiksi', tulos)
        viivakoodi = testi.buildBarcode()
        print(f"viivakoodin sisältö on {viivakoodi}")
    except Exception as e:
        print(f"Tapahtui virhe {testi.text} {e}")
