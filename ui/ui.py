import customtkinter as CTk
import tkinter, json, main, ui.deviceFrame
from database import dbservice
from tkinter import *
from PIL import Image


class Uinterface():
    def __init__(self):
        self.num = 0

        # открытие файла настроек
        try:
            with open('settings.json', 'r+') as file:
                self.settings = json.load(file)
        except Exception as ex:
            print('!ERROR ', ex)
        
        self.db = dbservice.Database()

        self.main_frame = CTk.CTk()
        self.main_frame.title('Paramfinder')
        self.main_frame.geometry('800x600')
        self.main_frame.resizable(0,0)

        self.load_img()
        self.dbConnect()
        
        self.main_frame_buttons()
        self.main_frame_labels()
        self.devices_frame()

        self.main_frame.mainloop()



    def main_frame_buttons(self,):
        buton_find = CTk.CTkButton(master=self.main_frame, 
                                   text='Найти данные', 
                                   command= lambda: self.find_cell())
        buton_find.place(relx=0.1, y=20, anchor=tkinter.CENTER)

        buton_collect = CTk.CTkButton(master=self.main_frame, 
                                      text='Собрать данные',  
                                      command= lambda: self.collectData())
        buton_collect.place(relx=0.1, y=50, anchor=tkinter.CENTER)

        buton_saveData = CTk.CTkButton(master=self.main_frame, 
                                      text='Сохранить данные',  
                                      command= lambda: self.saveToDb())
        buton_saveData.place(relx=0.1, y=80, anchor=tkinter.CENTER)

        button_settings = CTk.CTkButton(master=self.main_frame, 
                                        width= 40, height=40,
                                        fg_color='transparent',
                                        text='', image = self.cog_image, command= lambda: print('test'))
        button_settings.place(relx=0.01, rely=0.9)

        db_status_img = CTk.CTkButton(master=self.main_frame, text='', fg_color='transparent',hover='false', width=40, height=40, image=self.image_to_load)
        db_status_img.place(relx=0.07, rely = 0.9)

        CTk.set_appearance_mode('dark')
        
    def main_frame_labels(self):
        self.status1_var = StringVar()
        self.status2_var = StringVar()
        self.status3_var = StringVar()

        self.status1_labe = CTk.CTkLabel(master=self.main_frame, textvariable=self.status1_var)
        self.status1_labe.place(relx=0.5, y=110, anchor = tkinter.CENTER)

        self.status2_labe = CTk.CTkLabel(master=self.main_frame, textvariable=self.status2_var)
        self.status2_labe.place(relx=0.5, y=130, anchor = tkinter.CENTER)

        self.status3_labe = CTk.CTkLabel(master=self.main_frame, textvariable=self.status3_var)
        self.status3_labe.place(relx=0.5, y=150, anchor = tkinter.CENTER)


    def devices_frame(self):
        devicesField = CTk.CTkScrollableFrame(master=self.main_frame, width=580, height=560, bg_color="WHITE")
        devicesField.place(x=180, y=5, anchor=NW)
        pass


    def load_img(self):
        self.cog_image = CTk.CTkImage(light_image=Image.open('image\iconcog.png'), size=(30,30))
        self.dbOk_image = CTk.CTkImage(light_image=Image.open('image\databaseOk.png'), size=(30,30))
        self.dbFail_image = CTk.CTkImage(light_image=Image.open('image\databaseFail.png'), size=(30,30))
        self.imagedb = CTk.CTkImage(light_image=Image.open('image\database.png'), size=(30,30))
        self.image_to_load = self.imagedb

    def collectData(self):
        try:
            main.startApp(self.num)
            self.status2_var.set(f'Данные сообраны, ошибок: ')
        except Exception as ex:
            print('!ERROR ', ex)

    def dbConnect(self):
        try:
            self.db.dbconn(self.settings['app_settings']['link_to_db'])
            self.image_to_load = self.dbOk_image

        except Exception as ex:
            print('!ERROR ', ex)
            self.image_to_load = self.dbFail_image

    def find_cell(self):
        self.num = self.db.findEmptyCell()
        self.status1_var.set(f'Дата ок. Ячейка {self.num}')
        print(self.num)
    
    def saveToDb(self):
        try:
            main.save_to_db()
            self.status3_var.set(f"Сохранено в БД")
        except Exception as ex:
            self.status3_var.set(f"Ошибка сохранения\nв БД")
            print(ex)

    def run_app(self):
        pass



