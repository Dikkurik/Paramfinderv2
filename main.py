import appfunc.scrapper as sc, json, configparser
import appfunc.utility 
from database import dbservice 
import ui.ui as ui, ui.progresBarFrame as Bar

"""
 ____   _    ____      _    __  __ _____ ___ _   _ ____  _____ ____  
|  _ \ / \  |  _ \    / \  |  \/  |  ___|_ _| \ | |  _ \| ____|  _ \ 
| |_) / _ \ | |_) |  / _ \ | |\/| | |_   | ||  \| | | | |  _| | |_) |
|  __/ ___ \|  _ <  / ___ \| |  | |  _|  | || |\  | |_| | |___|  _ < 
|_| /_/   \_\_| \_\/_/   \_\_|  |_|_|   |___|_| \_|____/|_____|_| \_\\

"""


# define config 
config = configparser.ConfigParser()
config.read("config.cfg")



# open diveces list from json

try:
    with open('devices.json', 'r+', encoding='UTF-8') as file:
        devices = json.load(file)
except:
    print('Не найден файл со списком устройств')


# trying to connect exel file


try:
    db = dbservice.Database()
    print(db)
    if db.dbconn(config["APP SETTINGS"]["link_to_database"]) == True:
        dbconn = True
    else: 
        dbconn = False
except:
    print('Неуспешное подключение к БД')
    dbconn = False



print('Conn to db: ', dbconn, __name__)



# define arrays with devices list
rcu_list = devices['RCU']
rcu_device_fa = devices['RCU_RRA']
rcu_device_addit = devices['RCU_ADDIT']



# define report list
RCU_list_repot = []

# array with offline pages
page_array = [] 

def start_ui():
    print("""
          
 ____   _    ____      _    __  __ _____ ___ _   _ ____  _____ ____  
|  _ \ / \  |  _ \    / \  |  \/  |  ___|_ _| \ | |  _ \| ____|  _ \ 
| |_) / _ \ | |_) |  / _ \ | |\/| | |_   | ||  \| | | | |  _| | |_) |
|  __/ ___ \|  _ <  / ___ \| |  | |  _|  | || |\  | |_| | |___|  _ < 
|_| /_/   \_\_| \_\/_/   \_\_|  |_|_|   |___|_| \_|____/|_____|_| \_\\

\nStarted paramfinder ver 2.0.1a
""")
    ui.Uinterface()

def showReport():
    print('RCU_STATUS_REPORT__________\n[____RCU_DEVICE_NAME_______]')
    for i in RCU_list_repot:
        print(i)


def startApp(row_num):
    # main parsing data
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
            #adding page to array for offline parsing
            device_page = raw_data[1]
            page_array.append(device_page) 
            print(len(raw_data))
            data = []
            cells = []
            
            for i in rcu_list[device]['index_data']:
                # make array with raw data
                data.append(raw_data[0][i]) 

            for i in rcu_list[device]['cells']:
                # make array with table cells 
                cell_id = str(i)+str(row_num)
                cells.append(cell_id) 

            try:
                db.insertToDB(str(rcu_list[device]['sheet']), cells, data)
                RCU_list_repot.append(f'{device} added')
            except Exception as ex:
                RCU_list_repot.append(f'{device} ERROR <---')
                print('    !ERROR when trying insert data\n', ex)
            
        except Exception as ex:
            print(ex)


    # Scrapping device througt FindAll method    
    print('Start parse addit data for RR')
    print('array list', page_array)
    
    # parse addit params for rra (offline)
    for device in rcu_device_fa:
            print(device)
            data = []
            cells = []
            mod_ind = rcu_device_fa[device]['mod_index']
            mod_cell = rcu_device_fa[device]['mod_cell']
            n = 0
            for i in rcu_device_fa:
                pos = rcu_device_fa[device]['array_pos']
                scrap = sc.ScrapOffline()
                raw_data = scrap.scrapData(page_array[pos], rcu_device_fa[device]['tag'])
                

                for i in rcu_device_fa[device]['index_data']:
                    data.append(raw_data[i])

                for i in rcu_device_fa[device]['cells']:
                    cells.append(str(i)+str(row_num))
                n+=1

                try:
                    print('Index 70',raw_data[mod_ind])
                    mod_data = appfunc.utility.checkModulatorRRA(raw_data[mod_ind])
                    print(mod_data)
                    print('Модулятор в работе', mod_data)
                    mod_cell_list = [str(mod_cell)+str(row_num)]
                    print(' Ячейка модуляторов ',mod_cell_list)

                    db.insertToDB(('Текущий'), mod_cell_list, mod_data)
                    RCU_list_repot.append(f'{device} added')
                    
                except Exception as ex:
                    RCU_list_repot.append(f'{device} ERROR <---')
                    print('    !ERROR when trying insert data\n', ex)

                try:
                    db.insertToDB(('РРА'), cells, data)
                    RCU_list_repot.append(f'{device} added')
                except Exception as ex:
                    RCU_list_repot.append(f'{device} ERROR <---')
                    print('    !ERROR when trying insert data\n', ex)

    # parse addit devices (offline) it takes
    def add_audio():
            print('Try add audio')
            n = 0
            for device in rcu_device_addit:  #! <--- need parse throuth cycle 
                print(device)
                data = []
                cells = []
            
                n = 0
                pos = rcu_device_addit[device]['array_pos']
                scraps = sc.ScrapOffline()
                raw_data = scraps.scrapData(page_array[pos], rcu_device_addit[device]['tag'])

                for i in rcu_device_addit[device]['index_data']:
                    data.append(appfunc.utility.roundFucn(raw_data[i]))

                cells = rcu_device_addit[device]['cells']
                n+=1
                try:
                    db.insertToDB(rcu_device_addit[device]['sheet'], cells, data)
                    RCU_list_repot.append(f'{device} Ok')
                except Exception as ex:
                    RCU_list_repot.append(f'{device} ERROR <----')
                    print('    !ERROR when trying insert data\n', ex)
    try:
        add_audio()
    except Exception as ex:
        RCU_list_repot.append(' Не удалось собрать или сохранить аудиоданные')
    showReport()

def save_to_db():
    db.saveDb()
    print('    !INFO DB Saving OK')


if __name__ == "__main__":
    start_ui()
    

    
    
    
    
