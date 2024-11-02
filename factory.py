from abc import ABC,abstractmethod
import pandas as pd
import json
class File(ABC):

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class ExcelFile(File):
    def __init__(self,fileAddress):
        self.fileAddress = fileAddress

    def read(self):
        with open(self.fileAddress,'rb') as file:
            excel_data = pd.read_excel(file)
            return excel_data
    def write(self,data):
        with open(self.fileAddress,'w') as file:
            marks_data = pd.DataFrame(data)
            marks_data.to_excel(file)

class JsonFile(File):
    def __init__(self,fileAddress):
        self.fileAddress = fileAddress

    def read(self):
        with open(self.fileAddress,'r') as file:
            data = file.read()
            return json.loads(data)

    def write(self,data):
        with open(self.fileAddress, 'w') as file:
            json_object  = json.dumps(data)
            file.write(json_object)


if __name__ == '__main__':
    j1 = JsonFile('test.json')
    excel = ExcelFile('users.xlsx')

    files = [j1, excel]
    for f in files:
        data = f.read()
        print(data)
        print('='*30)

