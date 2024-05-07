import customtkinter as CTk, ui.deviceManagerUI
from main import config
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

    # Buttons
    button_showDevices = CTk.CTkButton(master=leftSide_frame, width=40, height=40, text='Показать устройства', 
                                    command= lambda: ui.deviceManagerUI.showDevices_frame())
    button_showDevices.pack(pady=10)

    button_lightTheme = CTk.CTkButton(master=leftSide_frame, width=40, height=40, text='Светлая тема', 
                                    command= lambda: switchToLight())
    button_lightTheme.pack(pady=10)

    button_lightTheme = CTk.CTkButton(master=leftSide_frame, width=40, height=40, text='Темная тема' , 
                                    command= lambda: switchToDark())
    button_lightTheme.pack(pady=10)

    button_setTime = CTk.CTkButton(master=rightSide_frame, width=30, height=30, text='+' , 
                                    command= lambda: gettextbox())
    button_setTime.place(x= 230, y=15)

    # Textbox and labels
    pageload_label = CTk.CTkLabel(master=rightSide_frame, width=180, height=40, text='Время загрузки страницы')
    pageload_label.place(x=10, y=10)

    pageload_textbox = CTk.CTkTextbox(master=rightSide_frame, width=30, height=20, activate_scrollbars=False)
    pageload_textbox.place(x=200, y=15)


    # attrs

    pageload_text = pageload_textbox.get('1.0', END)

    settingsFrame.mainloop()


def switchToLight():
    config.set('USER INTERFACE','theme', 'light')
    
    with open('config.cfg', 'w') as f:
        config.write(f)

def switchToDark():
    config.set('USER INTERFACE','theme', 'dark')
    
    with open('config.cfg', 'w') as f:
        config.write(f)

def gettextbox(): #! <- need to finish this func for getting data from textbox
    print(settings_Frame.pageload_text)
    # print(settings_Frame.('1.0', END))

