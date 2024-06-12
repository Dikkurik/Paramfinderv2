import customtkinter as CTk

someArray = [1,1,1,1,1,11,1,1,1,1,11,1,1,1,1,11,1,1,1,1,11,1,1,1,1]
class Bar():
    def __init__(self):
        self.proggresBar_frame = CTk.CTk()
        self.proggresBar_frame.geometry('200x100')
        self.proggresBar_frame.resizable(0,0)
        self.proggresBar_frame.deiconify()
        self.load_num = 0


        self.progressbar = CTk.CTkProgressBar(master = self.proggresBar_frame, orientation='horizontal', mode='determinate', height=40)
        self.progressbar.pack(padx=0.5)
        self.progressbar.set(0)

        self.btn = CTk.CTkLabel(master=self.proggresBar_frame, width=20, height=20, text="Загрузка страниц...")
        self.btn.pack(padx=0.5)

        self.btn = CTk.CTkButton(master=self.proggresBar_frame, width=20, height=20, command= lambda: self.startWithInp())
        self.btn.pack(padx=0.5)
    
        self.proggresBar_frame.mainloop()


    def start(self, bar):
        print('began')
        
        progres = 1/len(bar)
        print(len(bar))
        self.progressbar.set(progres)
        point = 0
        self.progressbar.start() 
        ab = progres
        for i in bar:
            self.progressbar.set(ab)
            ab = point+progres
            self.proggresBar_frame.update_idletasks()
            print(ab)
            point = ab
            
        
        self.progressbar.stop()
        self.proggresBar_frame.destroy()

    def startWithInp(self, ab:float):
        self.progressbar.set(ab)
        self.load_num += ab
        self.proggresBar_frame.update_idletasks()



