import requests
from bs4 import BeautifulSoup


class ScrapDevice():
    def __init__(self):
        
        self.page = ''
        pass

    def connectToDevice(self, url:str, cred:list, name:str, auth_key: str) -> str:
        """
        Connecting to RCS device using requests. 
        """
        try:
            headers = {'authorization': auth_key}
            conn = requests.get(url, auth=(cred[0], cred[1]), verify=False, headers=headers)
            conn.encoding = 'UTF-8' 
            print(f'!INFO Connected to device {name}, status code:', conn.status_code)
            self.name = name
            self.page = conn.text
            
        except Exception as ex:
            print('!ERROR',ex)
            input('press enter to exit')

    #need to call this method with class tag (c_tag) and id tag (id_tag) passed
    def scrapData(self, c_tag:str, tag:str ):
        """
        Scraping data from RCS device page
        """
        try:
            soup = BeautifulSoup(self.page, 'lxml')
            print('!INFO SOUP', soup)
            data = soup.find(class_=c_tag)
            print(data)
            input('press enter to exit')
        except Exception as ex:
            print('!ERROR', ex)
            input('press enter to exit')    

        

if __name__ == "__main__":
    #test data NEED TO DELETE THIS AFTER MAKE FULL APP
    url = 'https://10.29.1.3/config/tx_radio_microtec/?id=5'
    login = 'admin'
    password = 'AUcy1-8'
    auth_key = 'KRC51SRV-D2G1B7DR-BCSMPBIN-T6KPBUA7-93IJBO6T-9MD1N4O0'
    name = 'Radio Rossii TF 5000'
    cred = [login, password]


    testCall = ScrapDevice()
    testCall.connectToDevice(url, cred, name, auth_key)
    testCall.scrapData('titan', 'td')