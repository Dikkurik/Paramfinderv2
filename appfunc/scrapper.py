#own modules
import utility, time, configparser

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



class ScrapDevice():
    def __init__(self):
        s = Service('firefoxdrivers/geckodriver') 
        o = Options(); o.add_argument('--headless') 
        self.driver = webdriver.Firefox(service=s, options=o)
        print('    !INFO Run container... Loading web page...')
        self.page = ''
        config = configparser.ConfigParser()
        config.read('config.cfg')

        
    def connectToDevice(self, url:str, cred:list, name:str) -> str:
        """
        Connecting to RCS device using selenium. 
        """
        try:
            conn = self.driver.get(url) 
            print(f'    !INFO Connected to device {name}')
            self.name = name
            self.driver.find_element(By.NAME, 'username').send_keys(cred[0])
            self.driver.find_element(By.NAME, 'userpass').send_keys(cred[1])
            self.driver.find_element(By.CLASS_NAME, 'auth_submit').click()
            # set timer to load page
            time.sleep(10)
            self.page = self.driver.page_source
            
        except Exception as ex:
            print('    !ERROR\n',ex)

        finally:
            self.driver.close()
            self.driver.quit()
            print('    !INFO Close container...')

    #need to call this method with class tag (c_tag) and id tag (id_tag) passed
    def scrapData(self, c_tag:str) -> list:
        """
        Scraping data from RCS device page
        """
        try:
            soup = BeautifulSoup(self.page, 'lxml')
            data = soup.find(class_=c_tag).find_all('td')
            params = utility.makeIndexList(data)
            print('    !INFO Gathered parametrs:\n', params)
            return params, self.page
        except Exception as ex:
            print('    !ERROR\n', ex)



class ScrapFindAll(ScrapDevice): # <--- need to finish
    """
    Inherited class from ScrapDevice() where method
    scrapData() is redifined for scraping repeated
    tags on page
    """
    def scrapData(self, c_tag: str) -> list:
        try:
            soup = BeautifulSoup(self.page, 'lxml')
            data = soup.find_all(class_=c_tag)
            params = utility.makeIndexList(data)
            print('    !INFO Gathered parametrs:\n', params)
            return params
        except Exception as ex:
            print('    !ERROR\n', ex)


class ScrapOffline():
        def scrapData(self, page:str, c_tag: str) -> list:
            try:
                soup = BeautifulSoup(page, 'lxml')
                data = soup.find_all(class_=c_tag)
                params = utility.makeIndexList(data)
                print('    !INFO Gathered parametrs:\n', params)
                return params
            except Exception as ex:
                print('    !ERROR\n', ex)
        
