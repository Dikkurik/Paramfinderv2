import customtkinter as CTk
from tkinter import *
from PIL import Image

class Device():
    """Single device class for drawing in report"""

    def __init__(self):
        self.load_img()

    def load_img(self):
        self.device_image = CTk.CTkImage(light_image=Image.open('image/device.png'), size=(30,30))
        self.deviceOk_image = CTk.CTkImage(light_image=Image.open('image/deviceOk.png'), size=(30,30))
        self.deviceFail_image = CTk.CTkImage(light_image=Image.open('image/deviceFail.png'), size=(30,30))

    def drawDevice(self, frame:object, name:str):
        """
        Method for drawing single device with name passed
        """
        if self.checkForError(name) == True:
            self.device_image = self.deviceOk_image
        else:
            self.device_image = self.deviceFail_image
        device_frame = CTk.CTkFrame(master=frame, width=500, height=50, border_color="BLACK", border_width=1)
        device_name = CTk.CTkLabel(master=device_frame, width=60, height=20, text=name)
        device_icon = CTk.CTkButton(master=device_frame, text='', fg_color='transparent', hover='false', width=40, height=40, image=self.device_image)
        device_frame.pack(pady=3, anchor=NW)
        device_name.place(x=60, y=10, anchor=NW)
        device_icon.place(x=1, y=1)

    @staticmethod
    def checkForError(name):
        """
        Method for checking error in device name
        """
        if "ERROR" in name:
            return False
        else:
            return True





