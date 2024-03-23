import ui, scrapper as sc, json
from database import dbservice 

#! [x] connect to device in RCU
    #! [x] get data without tags in lost or smh
#! [x] make json object for devices
#! [ ] parse data for devices:
    #! [x] 2 tags parse for:
        #! [x] rra main params
        #! [x] rr bereznik
        #! [x] rr kozma
        #! [x] rr mezen 
        #! [x] rr taiga
        #! [x] arh rtrs 1
        #! [x] arh rtrs 2
    #! [ ] 1 tag parse for: 
        #! [x] rra add params 
        #! [ ] rrs sevsk
        #! [ ] vesti sevsk
        #! [ ] mayak sevsk 
        #! [ ] radio retro
        #! [ ] rr belush guba
        #! [ ] solnce 
    #! [x] recievers:
        #! [x] 7100 mux1   
        #! [x] 7100 mux2
        #! [x] rx 8330 mux1
        #! [x] rx 8330 mux2
        #! [x] trk 555
        #! [x] trk 575
#! [x] db management
    #! [x] connect to db
    #! [x] read data from DB
    #! [x] write data to DB
    #! [x] change sheet

try:
    with open('settings.json', 'r+', encoding='UTF-8') as file:
        settings = json.load(file)
except:
    print('Не найден файл настроек')

try:
    with open('devices.json', 'r+', encoding='UTF-8') as file:
        devices = json.load(file)
except:
    print('Не найден файл со списком устройств')
try:
    db = dbservice.Database()
    db.dbconn(settings['app_settings']['link_to_db'])
except:
    print('неуспешное подключение к БД')

rcu_list = devices['RCU']
rcu_device_fa = devices['RCU_RRA']

#? snippets for for-loop
# url - rcu_list[i]['URL_address'],
# login - rcu_list[i]['login'],
# pass - rcu_list[i]['password']
# tag - rcu_list[i]['tag']
# index - rcu_list[i]['index_data']
# cells - rcu_list[i]['cells']
# sheet - rcu_list[i]['sheet']

RCU_list_repot = ['RCU_STATUS_REPORT','[____RCU_DEVICE_NAME_______]',]

page_massive = []

def showReport():
    print(RCU_list_repot)

def startApp(row_num):
    
    for device in rcu_list:
        print(device)
        try:
            scrapper = sc.ScrapDevice()
            scrapper.connectToDevice(rcu_list[device]['URL_address'],
                                    [rcu_list[device]['login'], 
                                    rcu_list[device]['password']],
                                    device)
            print(f'    !INFO {device} reached!')
            raw_data = scrapper.scrapData(rcu_list[device]['tag'])
            page_massive.append(raw_data[1])
            print(len(raw_data))
            data = []
            cells = []
            
            for i in rcu_list[device]['index_data']:
                data.append(raw_data[0][i])

            for i in rcu_list[device]['cells']:
                cells.append(str(i)+str(row_num))
            try:
                db.insertToDB(str(rcu_list[device]['sheet']), cells, data)
                RCU_list_repot.append(f'{device} added')
            except Exception as ex:
                RCU_list_repot.append(f'{device} ERROR<---')
                print('    !ERROR when trying insert data\n', ex)
            
        except Exception as ex:
            print(ex)


    #* Scrapping device througt FindAll method    
    print('Start parse addit data for RR')
    print('Massive list', page_massive)
    for device in rcu_device_fa:
            print(device)
            data = []
            cells = []
            
            
            #parse addit params for rra
            n = 0
            for i in rcu_device_fa:
                scrap = sc.ScrapOffline()
                raw_data = scrap.scrapData(page_massive[0], c_tag = 'enceladus')

                for i in rcu_device_fa[device]['index_data']:
                    data.append(raw_data[i])

                for i in rcu_device_fa[device]['cells']:
                    cells.append(str(i)+str(row_num))
                n+=1
                try:
                    db.insertToDB(('РРА'), cells, data)
                    RCU_list_repot.append(f'{device} added')
                except Exception as ex:
                    RCU_list_repot.append(f'{device} ERROR<---')
                    print('    !ERROR when trying insert data\n', ex)

    showReport()


        

def save_to_db():
    db.saveDb()
    print('    !INFO DB Saving OK')


        

if __name__ == '__main__':

    print("""
 ____   _    ____      _    __  __ _____ ___ _   _ ____  _____ ____  
|  _ \ / \  |  _ \    / \  |  \/  |  ___|_ _| \ | |  _ \| ____|  _ \ 
| |_) / _ \ | |_) |  / _ \ | |\/| | |_   | ||  \| | | | |  _| | |_) |
|  __/ ___ \|  _ <  / ___ \| |  | |  _|  | || |\  | |_| | |___|  _ < 
|_| /_/   \_\_| \_\/_/   \_\_|  |_|_|   |___|_| \_|____/|_____|_| \_\

\nStarted paramfinder ver 2.0.1a
""")

    startUi = ui.Uinterface()
    
