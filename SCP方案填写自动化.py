import pyautogui as pa
import pyperclip as pe
import time

def paste(txt):
    pe.copy(txt)
    pa.hotkey('ctrl','v')




