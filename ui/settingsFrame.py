import customtkinter as CTk, main, configparser
from tkinter import *
from PIL import Image


# need to defive buttons and device manager

def settings_Frame():
    """
    Frame for settings and device manager
    """

    settingsFrame = CTk.CTk()
    settingsFrame.geometry("900x600")
    settingsFrame.title('Настройки')
    settingsFrame.resizable(0,0)

    settingsFrame.mainloop()


