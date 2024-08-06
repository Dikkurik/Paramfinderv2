import json, pprint

class deviceJsonEditor():
    def __init__(self, device_data, array, name):

        self.name = str(name)
        self.array = str(array)
        self.device_data = device_data
        

    def editParams(self, paramsdict):
            device = self.device_data[self.array][self.name]
            device["URL_address"] = paramsdict["URL_address"]
            device["login"] = paramsdict["login"]
            device["password"] = paramsdict["password"]
            device["tag"] = paramsdict["tag"]
            device["cells"] = paramsdict["cells"]
            device["index_data"] = paramsdict["index_data"]
            device["sheet"] = paramsdict["sheet"]
            pprint.pp(self.device_data)


    def saveData(self):
        with open('devices_test.json', 'r+', encoding='UTF-8') as file:
            json.dump(self.device_data, file, ensure_ascii=False)
        print('Succeful saved')


if __name__ == "__main__":

    with open('devices.json', 'r+', encoding='UTF-8') as file:
        devices = json.load(file)
     

    testdict = {
            "URL_address": "TestURL",
            "login": "TestLogin",
            "password": "TestPassword",
            "tag": "testtag",
            "cells": "testCell",
            "index_data": "testIndex",
            "sheet": "testsheet"
    }
    testobj = deviceJsonEditor(devices, 'RCU', 'TEST_RCU_page RCU')
    testobj.editParams(testdict)