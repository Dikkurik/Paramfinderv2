import customtkinter as CTk, main, configparser
from tkinter import *
from PIL import Image

def devicesManager_frame():
    devices_frame = CTk.CTk()
    devices_frame.geometry("900x600")
    devices_frame.title('Менеджер устройств')
    devices_frame.resizable(0,0)

    leftSide_frame = CTk.CTkFrame(master=devices_frame, width=200, height=580)
    leftSide_frame.place(x=5,y=5, anchor=NW)

    rightSide_frame = CTk.CTkScrollableFrame(master=devices_frame, width=680, height=580, border_width=1)
    rightSide_frame.place(x=205,y=5, anchor=NW)

    for i in main.devices:
        btn = deviceArrayBtn(i, leftSide_frame, rightSide_frame)
        btn.drawButton()

    devices_frame.mainloop()


class Device():
    """
    Class for drawing and editing device and device information in device.
    """

    def drawDevice(self, frame, mainArray, name, device_data):
        self.device_frame = CTk.CTkFrame(master=frame, width=580, height=60, border_color="BLACK",border_width=1)
        self.device_frame.pack(pady=5)

        self.mainArray = mainArray
        self.device_name = name

        self.device_url = device_data['URL_address']
        self.device_cells = device_data['cells']
        self.device_indexes = device_data['index_data']
        self.device_sheet = device_data['sheet']

        

        name_label = CTk.CTkLabel(master=self.device_frame, width=50, height=30, text = self.device_name)
        url_label = CTk.CTkLabel(master=self.device_frame, width=50, height=30,text=self.device_url)
        cells_label = CTk.CTkLabel(master=self.device_frame, width=50, height=30, text=self.device_cells)
        indexes_label = CTk.CTkLabel(master=self.device_frame, width=50, height=30, text=self.device_indexes)
        sheet_label = CTk.CTkLabel(master=self.device_frame, width=50, height=30, text=self.device_sheet)

        name_label.place(x=1, y=1, anchor=NW)
        url_label.place(x=1, y=31, anchor=NW)
        cells_label.place(x=100, y=1, anchor=NW)
        indexes_label.place(x=100, y=31, anchor=NW)
        sheet_label.place(x=160, y=1, anchor=NW)

        editBtn = CTk.CTkButton(master=self.device_frame, width=50, height=30, text='Ред.', command = lambda: self.openEditor())
        editBtn.place(x=500, y=1, anchor=NW)
        
    def openEditor(self):

        pass

class deviceArrayBtn():
    """
    Class for drawing button and devices to the left and right side frame of 
    device manager
    """
    def __init__ (self, name, left_frame, right_frame):
        self.name = name
        self.left_frame = left_frame
        self.right_frame = right_frame
        

    def showDevicesInArray(self, array):
        for i in main.devices[array]:
            device_data = main.devices[array][i]
            deviceInfo = Device()
            deviceInfo.drawDevice(self.right_frame, str(array), str(i), device_data)

    def drawButton(self):
        button_deviceArray = CTk.CTkButton(master=self.left_frame, width=190, height=50, text=self.name,
                                command= lambda: self.showDevicesInArray(self.name))
        button_deviceArray.pack(pady=4)