# MODUULI ÄÄNIMERKKIEN ANTAMISEEN
# ===============================

"""A module to produce various sound patterns and play wav-files
    """

# KIRJASTOT JA MODUULIT
#----------------------

# Windows-äänet
import winsound

# Ajankäsittely
import time

# ÄÄNIFUNKTIOT
#-------------

def shortBeep():
    """Creates a 1 kHz sound for 1/4 second
    """
    winsound.Beep(1000, 250)

def longBeep():
    """Creates a 1Khz sound for 2 seconds
    """
    winsound.Beep(1000, 2000)

def waitMs(ms):
    """Waits for a timeperiod

    Args:
        ms (int): time in milliseconds
    """
    seconds = ms / 1000
    time.sleep(seconds)

# Säädettävät äänet 1. korkeus ja kesto parametreina
def parametricBeep(frequency, duration):
    """Produces a sound at given frequency and duration

    Args:
        frequency (int): _Frequency of the tone in Hz
        duration (int): Duration in milliseconds
    """
    winsound.Beep(frequency, duration)

# Säädettävät äänet 2. toistuva äänimerkki korkeus, kesto ja määrä

def repeatingBeep(frequency: int, duration: int, count: int) -> None:
    """Creates a repeating buzzer sound

    Args:
        frequency (int): Tone frequency in Hz
        duration (int): Duration of the single tone in milliseconds
        count (int): How many times sound will be repeated
    """
    for i in range(count):
        winsound.Beep(frequency, duration)
        waitMs(250)


# Ääni tulee halutusta tiedostosta, parametrina äänen nimi.
def playWav(fileName: str) -> None:
    """Plays a wav file

    Args:
        fileName (str): Name of the audiofile
    """
    winsound.PlaySound(fileName, winsound.SND_FILENAME)