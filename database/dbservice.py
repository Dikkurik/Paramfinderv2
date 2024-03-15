from openpyxl import load_workbook

# [ ] connect to db
# [ ] read data from DB
# [ ] write data to DB
# [ ] change sheet
# [ ] 


class Database():
    def __init__(self):
        self.workbook = None
        self.sheet = None
        self.link = None

    def dbconn(self, linkToDB):
        try:
            self.workbook = load_workbook(filename=linkToDB)
            self.link = linkToDB
        except:
            print('    !ERROR connect to db\n')

    def insertToDB(self, sheet:str, cells:list, data:list):
        n = 0
        curr_sheet = self.workbook[sheet]
        for i in data:
            curr_sheet[cells[n]] = data[n]
            n+=1
        print(f'    !INFO Successfull add data to {sheet} sheet\n')

    def readFromDB(self, sheet:str):
        pass

    def saveDb(self):
        self.workbook.save(self.link) 

if __name__ == '__main__':

    cells = ['A1', 'A2', 'B3']
    data = ['test', 123, '765']

    test = Database()
    test.dbconn ('D:\GIT\Paramfinder v2\\test.xlsx')
    test.insertToDB('Лист1', cells, data)
    test.saveDb()

