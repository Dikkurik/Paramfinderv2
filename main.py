import ui.ui as ui, appfunc.scrapper as sc, json, configparser
import appfunc.utility 
from database import dbservice 

"""
 ____   _    ____      _    __  __ _____ ___ _   _ ____  _____ ____  
|  _ \ / \  |  _ \    / \  |  \/  |  ___|_ _| \ | |  _ \| ____|  _ \ 
| |_) / _ \ | |_) |  / _ \ | |\/| | |_   | ||  \| | | | |  _| | |_) |
|  __/ ___ \|  _ <  / ___ \| |  | |  _|  | || |\  | |_| | |___|  _ < 
|_| /_/   \_\_| \_\/_/   \_\_|  |_|_|   |___|_| \_|____/|_____|_| \_\\

"""
# open settings file #! <-- migrate to config
try:
    with open('settings.json', 'r+', encoding='UTF-8') as file:
        settings = json.load(file)
except:
    print('Не найден файл настроек')

# open diveces list from json
try:
    with open('devices.json', 'r+', encoding='UTF-8') as file:
        devices = json.load(file)
except:
    print('Не найден файл со списком устройств')

# trying to connect exel file
try:
    db = dbservice.Database()
    db.dbconn(settings['app_settings']['link_to_db'])
except:
    print('Неуспешное подключение к БД')

# define arrays with devices list
rcu_list = devices['RCU']
rcu_device_fa = devices['RCU_RRA']
rcu_device_addit = devices['RCU_ADDIT']

# define config 
config = configparser.ConfigParser()
config.read("config.cfg")

# define report list
RCU_list_repot = []

# array with offline pages
page_array = [] 

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
            page_array.append(raw_data[1]) 
            print(len(raw_data))
            data = []
            cells = []
            
            for i in rcu_list[device]['index_data']:
                # make array with raw data
                data.append(raw_data[0][i]) 

            for i in rcu_list[device]['cells']:
                # make array with table cells 
                cells.append(str(i)+str(row_num)) 

            try:
                db.insertToDB(str(rcu_list[device]['sheet']), cells, data)
                RCU_list_repot.append(f'{device} added')
            except Exception as ex:
                RCU_list_repot.append(f'{device} ERROR<---')
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
                    db.insertToDB(('Текущий'), str(mod_cell)+str(row_num), mod_data) #! <--- ошибка "Tuple object has no attribute value"
                    RCU_list_repot.append(f'{device} added')
                    
                except Exception as ex:
                    RCU_list_repot.append(f'{device} ERROR<---')
                    print('    !ERROR when trying insert data\n', ex)

                try:
                    db.insertToDB(('РРА'), cells, data)
                    RCU_list_repot.append(f'{device} added')
                except Exception as ex:
                    RCU_list_repot.append(f'{device} ERROR<---')
                    print('    !ERROR when trying insert data\n', ex)

    # parse addit devices (offline)
    for device in rcu_device_addit: #! <--- work on that for addit devices
            print(device)
            data = []
            cells = []
        
            n = 0
            for i in rcu_device_addit:  #! <--- need parse throuth cycle 
                pos = rcu_device_addit[device]['array_pos']
                scrap = sc.ScrapOffline()
                raw_data = scrap.scrapData(page_array[pos], rcu_device_addit[device]['tag'])

                for i in rcu_device_addit[device]['index_data']:
                    data.append(raw_data[i])

                for i in rcu_device_addit[device]['cells']:
                    cells.append(str(i)+str(row_num))
                n+=1
                try:
                    db.insertToDB(rcu_device_addit[device]['sheet'], cells, data)
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
|_| /_/   \_\_| \_\/_/   \_\_|  |_|_|   |___|_| \_|____/|_____|_| \_\\

\nStarted paramfinder ver 2.0.1a
""")

    startUi = ui.Uinterface()
    
