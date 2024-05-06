import customtkinter as CTk, main, configparser
from tkinter import *
from PIL import Image



def deviceManager_frame():
    """
    Frame for device manager
    """

    deviceManager = CTk.CTk()
    deviceManager.geometry("900x600")
    deviceManager.title('Менеджер устройств')
    deviceManager.resizable(0,0)


    
    deviceManager.mainloop()


def showDevices_frame():
    devices_frame = CTk.CTk()
    devices_frame.geometry("900x600")
    devices_frame.title('Менеджер устройств')
    devices_frame.resizable(0,0)

    leftSide_frame = CTk.CTkFrame(master=devices_frame, width=200, height=580)
    leftSide_frame.place(x=5,y=5, anchor=NW)

    rightSide_frame = CTk.CTkScrollableFrame(master=devices_frame, width=680, height=580, border_width=1)
    rightSide_frame.place(x=205,y=5, anchor=NW)

    # def showDevicesInArray(array): #! <---- passed last array in divecis.json
    #     for i in main.devices[array]:
    #         print('name', i)
    #         print(main.devices[array][i].values())
    #         device_data = main.devices[array][i]
    #         print(device_data)
    #         print(device_data['URL_address'])
    #         deviceInfo = DrawDevice()
    #         deviceInfo.drawDevice(rightSide_frame, i, device_data) #! <---- problem there

    for i in main.devices:
        btn = deviceArrayBtn(i, leftSide_frame, rightSide_frame)
        btn.drawButton()

    devices_frame.mainloop()





class DrawDevice():
    """
    Class for drawing device and device information in device manager frame.
    
    """

    def drawDevice(self, frame, name, device_data):
        device_frame = CTk.CTkFrame(master=frame, width=400, height=60, border_color="BLACK",border_width=1)
        device_frame.pack(pady=5)

        print('in class data:', device_data)

        self.device_name = name
        self.device_url = device_data['URL_address']
        self.device_cells = device_data['cells']
        self.device_indexes = device_data['index_data']
        self.device_sheet = device_data['sheet']

        name_label = CTk.CTkLabel(master=device_frame, width=50, height=30, text = self.device_name)
        url_label = CTk.CTkLabel(master=device_frame, width=50, height=30,text=self.device_url)
        cells_label = CTk.CTkLabel(master=device_frame, width=50, height=30, text=self.device_cells)
        indexes_label = CTk.CTkLabel(master=device_frame, width=50, height=30, text=self.device_indexes)
        sheet_label = CTk.CTkLabel(master=device_frame, width=50, height=30, text=self.device_sheet)

        name_label.place(x=1, y=1, anchor=NW)
        url_label.place(x=1, y=31, anchor=NW)

        cells_label.place(x=31, y=1, anchor=NW)
        indexes_label.place(x=31, y=31, anchor=NW)

        sheet_label.place(x=61, y=1, anchor=NW)



class deviceArrayBtn():
    '''
    Class for drawing button and devices to the left and side frame of device
    manager
    '''
    def __init__ (self, name, left_frame, right_frame):
        self.name = name
        self.left_frame = left_frame
        self.right_frame = right_frame
        

    def showDevicesInArray(self, array): #! <---- passed last array in divecis.json
        for i in main.devices[array]:
            print('name', i)
            print(main.devices[array][i].values())
            device_data = main.devices[array][i]
            print(device_data)
            print(device_data['URL_address'])
            deviceInfo = DrawDevice()
            deviceInfo.drawDevice(self.right_frame, i, device_data) #! <---- problem there

    def drawButton(self):
        button_deviceArray = CTk.CTkButton(master=self.left_frame, width=190, height=50, text=self.name,
                                command= lambda: self.showDevicesInArray(self.name))
        button_deviceArray.pack(pady=4)