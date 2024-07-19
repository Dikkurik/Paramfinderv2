# -*- coding: utf-8 -*-
# This file contains utility func's that clear string data
# and return readable info. 


tagList = ['<th>','</th>','<tbody>','</tbody>','<td>','</td>','<tr>','</tr>',
           '<th width="50%">','<table>','</table>','<th width="19%">','<th width="24%">',
           '<th width="25%">','<table class="enceladus">','<table class="titan">','<th colspan="2">',' ']


def makeIndexList(pagetext:str) -> list:
    """
    Clear page from HTML tags and pack data to list.
    """
    outputList = []
    proxyVarString = str(pagetext)
    n = 0
    for i in tagList:
        proxyVarString = proxyVarString.replace(tagList[n],' ')
        n+=1
    outputList = list(proxyVarString.split(' '))

    
    getIndexes(outputList)
    return outputList

def getIndexes(params:list) -> list:
    # need save output to txt
    """
    iterate all data in list and print it with index
    """
    n = 0
    for i in params:
        print(f'index {n}: {i}')
        n+=1

def floatFunc(number):
    try:
        return float(number)
    except:
        print('Ошибка при попытке преобразования')
        return (number)
    
def roundFucn(number):
    try:
        return round(number, 1)
    except:
        print('Ошибка в округлении')
        return number

def checkModulatorRRA(data):
    if data == 'Вкл.':
        return ['AB']
    else:
        return ['BA']


def makeParamArray(device_name, params): #! <--- need to finish this
    pass



def savePage(page, name):

    print("Saving devica page to file ", name)
    with open(f"files/{name}.html", "w", encoding="UTF-8") as blank_file:
                blank_file.write(page)
        

