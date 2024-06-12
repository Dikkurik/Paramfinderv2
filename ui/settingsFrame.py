import customtkinter as CTk
from customtkinter import filedialog  
import main
from tkinter import *

from PIL import Image

def settings_Frame(deviceFrame):
    """
    Frame for settings and device manager
    """

    settingsFrame = CTk.CTkFrame(master=deviceFrame, width=797, height= 597, border_width=1)
    settingsFrame.place(x=1, y=1, anchor=NW)

    leftSide_frame = CTk.CTkFrame(master=settingsFrame, width=200, height=580, border_width=1)
    leftSide_frame.place(x=5,y=5, anchor=NW)

    rightSide_frame = CTk.CTkFrame(master=settingsFrame, width=595, height=580, border_width=1)
    rightSide_frame.place(x=200,y=5, anchor=NW)

    # Buttons

    button_lightTheme = CTk.CTkButton(master=leftSide_frame, width=40, height=40, text='Светлая тема', 
                                    command= lambda: switchToLight())
    button_lightTheme.pack(pady=10)

    button_lightTheme = CTk.CTkButton(master=leftSide_frame, width=40, height=40, text='Темная тема' , 
                                    command= lambda: switchToDark())
    button_lightTheme.pack(pady=10)

    button_update = CTk.CTkButton(master=leftSide_frame, width=30, height=30, text='Обновить окно' , 
                                    command= lambda: update_frame(settingsFrame, deviceFrame), fg_color="GREEN")
    button_update.pack(pady=10)


    button_setTime = CTk.CTkButton(master=rightSide_frame, width=30, height=30, text='+' , 
                                    command= lambda: savetocfg(pageload_textbox, 'pageloadtime'))
    button_setTime.place(x= 230, y=15)

    button_exit = CTk.CTkButton(master=leftSide_frame, width=30, height=30, text='Закрыть окно' , 
                                    command= lambda: killframe(settingsFrame), fg_color="RED")
    button_exit.pack(pady=10)

    

    

    # Textbox and labels
    pageload_label = CTk.CTkLabel(master=rightSide_frame, width=180, height=40, text='Время загрузки страницы')
    pageload_label.place(x=10, y=10, anchor=NW)

    pageload_label_curr = CTk.CTkLabel(master=rightSide_frame, width=180, height=40, 
                                       text=f'Текущее Время загрузки страницы : {main.config["APP SETTINGS"]["pageloadtime"]}')
    pageload_label_curr.place(x=280, y=10, anchor=NW)

    pageload_textbox = CTk.CTkTextbox(master=rightSide_frame, width=30, height=20, activate_scrollbars=False)
    pageload_textbox.place(x=200, y=15, anchor=NW)

    dblink_label = CTk.CTkLabel(master=rightSide_frame, width=180, height=40, text='База данных')
    dblink_label.place(x=10, y=50, anchor=NW)

    dblink_label_curr = CTk.CTkLabel(master=rightSide_frame, width=180, height=40, text=f'Текущщая ссылка:\n {main.config["APP SETTINGS"]["link_to_database"]}')
    dblink_label_curr.place(x=290, y=50, anchor=NW)

    dblink_dialogue = CTk.CTkButton(master=rightSide_frame, width=30, height=20, text='Обзор', command = lambda: selectfile())
    dblink_dialogue.place(x=200, y=55, anchor=NW)



def switchToLight():
    main.config.set('USER INTERFACE','theme', 'light')
    
    with open('config.cfg', 'w') as f:
        main.config.write(f)

def switchToDark():
    main.config.set('USER INTERFACE','theme', 'dark')
    
    with open('config.cfg', 'w') as f:
        main.config.write(f)


def savetocfg(textbox_object, param):
        text = textbox_object.get('1.0', 'end-1c')
        main.config.set('APP SETTINGS', param, text)
        with open('config.cfg', 'w') as f:
            main.config.write(f)

def update_frame(frame, deviceframe):
    killframe(frame)
    settings_Frame(deviceframe)

  
def selectfile():
        filename = filedialog.askopenfilename()
        if filename != None:
            print (filename)
            main.config.set('APP SETTINGS', 'link_to_database', filename)
            with open('config.cfg', 'w') as f:
                main.config.write(f)
        else:
             return None

def killframe(frame):
    frame.destroy()