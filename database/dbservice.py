from openpyxl import load_workbook
import datetime as dt

# [X] connect to db
# [X] read data from DB
# [X] write data to DB
# [ ] change sheet
# [ ] 


class Database():
    def __init__(self):
        """
        define params when class is callde
        workbook - define exel table
        sheet - define sheet of exel table
        time - define current pc time and get today day
        """
        self.workbook = None
        self.sheet = None
        self.link = None
        self.time = str(dt.datetime.utcnow()).split(' ')[0]

    def dbconn(self, linkToDB):
        """
        Func that connect to DB using path to exel file
        """
        try:
            self.workbook = load_workbook(filename=linkToDB)
            self.link = linkToDB
        except:
            print('    !ERROR connect to db\n')

    def insertToDB(self, sheet:str, cells:list, data:list):
        """
        Func that insert data from list in cell using index
        ['cell'] -> ['index'] 
        """
        
        n = 0
        curr_sheet = self.workbook[sheet]
        for i in data:
            curr_sheet[cells[n]] = data[n]
            n+=1
        print(f'    !INFO Successfull add data to {sheet} sheet\n')

    def findEmptyCell(self, sheet:str) -> str:
        """
        Func that find empty cell in DB at 'A' column 
        and return cell that empty
        """
        curr_sheet = self.workbook[sheet]
        n=1
        cell = 'A1'
        for i in range(730):
            if str(curr_sheet[cell].value) == 'None':
                return cell
            else:
                print('Not empty')
                n+=1
                cell = 'A'+str(n)
        pass

    def check_date(self):
        """Func check date in cell from 'A' column and return 
        true if its equal to date on PC"""
        pass

    def saveDb(self):
        """Func that save current DB state"""
        try:
            self.workbook.save(self.link) 
        except Exception as ex:
            print('    !ERROR while saving database', ex)


if __name__ == '__main__':

    cells = ['A1', 'A2', 'B3']
    data = ['test', 123, '765']

    test = Database()
    test.dbconn ('D:\GIT\Paramfinder v2\\test.xlsx')
    # test.insertToDB('Лист1', cells, data)
    print(test.findEmptyCell('Лист1'))
    # test.saveDb()

