import struct
import ctypes
import requests

PATH = 'C:\\Users\\NFletcher\\Mattdamonarthur.jpg'
SPI_SETDESKWALLPAPER = 20

def is_64bit_windows():
    """Check if 64 bit Windows OS"""
    return struct.calcsize('P') * 8 == 64

def changeBG(path):
    """Change background depending on bit size"""
    if is_64bit_windows():
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, PATH, 3)
    else:
        ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, PATH, 3)

def download_file(url):
    """Downloads the file that will be set as the wallpaper"""
    myFile = requests.get(url)
    wallpaper = open(PATH, 'wb')
    wallpaper.write(myFile.content)
    wallpaper.close()

url = 'http://img4.wikia.nocookie.net/__cb20131008034405/arthur/images/3/33/Mattdamonarthur.jpg'
download_file(url)
changeBG(PATH)
