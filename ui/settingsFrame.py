import customtkinter as CTk, main, configparser, ui.deviceManagerUI
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

    leftSide_frame = CTk.CTkFrame(master=settingsFrame, width=200, height=580, border_width=1)
    leftSide_frame.place(x=5,y=5, anchor=NW)

    rightSide_frame = CTk.CTkFrame(master=settingsFrame, width=680, height=580, border_width=1)
    rightSide_frame.place(x=205,y=5, anchor=NW)

    button_showDevices = CTk.CTkButton(master=leftSide_frame, width=40, height=40, text='Показать устройства', 
                                    command= lambda: ui.deviceManagerUI.showDevices_frame())
    button_showDevices.pack(pady=10)

    settingsFrame.mainloop()


