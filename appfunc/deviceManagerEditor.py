import json, pprint

class deviceJsonEditor():
    def __init__(self, device_data, array, name):

        self.name = str(name)
        self.array = str(array)
        self.device_data = device_data

    def editParams(self):
            self.device_data
            pprint.pp(self.device_data)

    def saveData(self):
        with open('devices_test.json', 'r+', encoding='UTF-8') as file:
            json.dump(self.device_data, file, ensure_ascii=False)
        print('Succeful saved')


if __name__ == "__main__":
    with open('devices.json', 'r+', encoding='UTF-8') as file:
            devices = json.load(file)
    test = deviceJsonEditor(devices, "RCU", "TEST_RCU_page RCU")
    # test.editParams()
    test.saveData()