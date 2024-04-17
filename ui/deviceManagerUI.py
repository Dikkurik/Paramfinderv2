import customtkinter as CTk, main, configparser
from tkinter import *
from PIL import Image



def deviceManager_Frame():
    """
    Frame for settings and device manager
    """

    deviceManager = CTk.CTk()
    deviceManager.geometry("900x600")
    deviceManager.title('Менеджер устройства')
    deviceManager.resizable(0,0)

    deviceManager.mainloop()
