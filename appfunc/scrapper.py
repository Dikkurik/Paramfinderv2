import appfunc.utility as utility, time, main
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class ScrapDevice():

    def __init__(self, name:str , url:str, cred:list, c_tag):
        s = Service('firefoxdrivers/geckodriver') 
        o = Options(); #o.add_argument('--headless') 
        self.driver = webdriver.Firefox(service=s, options=o)
        print('    !INFO Run container... Loading web page...')
        self.name = name
        self.url = url
        self.cred = cred
        self.c_tag = c_tag
        self.time = time.process_time()

    def connectToDevice(self, ) -> str:
        """
        Connecting to RCS device using selenium. 
        """
        try:
            conn = self.driver.get(self.url) 
            
            print(f'    !INFO Connected to device {self.name}')
            self.driver.find_element(By.NAME, 'username').send_keys(self.cred[0])
            self.driver.find_element(By.NAME, 'userpass').send_keys(self.cred[1])
            self.driver.find_element(By.CLASS_NAME, 'auth_submit').click()
        except Exception as ex:
            print('    !ERROR\n',ex)
    
         
    def scrapData(self,) -> list:
        """
        Scraping data from RCS device page
        """

        try:
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            data = soup.find(class_=self.c_tag).find_all('td')
            params = utility.makeIndexList(data)
            print('    !INFO Gathered parametrs:\n', params)
            return params
        except Exception as ex:
            main.RCU_list_repot.append(f"{self.name} ERROR <----")
            print('    !ERROR\n', ex)

        
    def quitDriver(self):
        self.driver.quit()
        print("Time: ",self.time)

    def saveToFile(self):
        print("Saving device page to file ", self.name)
        with open(f"files/{self.name}.html", "w", encoding="UTF-8") as blank_file:
                    blank_file.write(self.driver.page_source)


class ScrapOffline():
        """
    Inherited class from ScrapDevice() where method
    scrapData() is redifined for scraping repeated
    tags on page
        """
        def scrapData(self, page:str, c_tag: str) -> list:
            try:
                soup = BeautifulSoup(page, 'lxml')
                data = soup.find_all(class_=c_tag)
                params = utility.makeIndexList(data)
                print('    !INFO Gathered parametrs:\n', params)
                return params
            except Exception as ex:
                print('    !ERROR\n', ex)
        
