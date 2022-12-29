import os
import shutil
import csv
from data_preprocessing import DataPreprocessing


class App:
    def __init__(self):
        self.file_path = '../data'
        self.files: list = os.listdir(self.file_path)

    def get_data(self):
        pass

    def upload_data(self):
        pass


if __name__ == '__main__':
    app = App()
    with open(os.path.join('../data', app.files[1]), 'r', encoding='euc-kr') as f:
        table = csv.reader(f)
        for i, item in enumerate(table):
            # if i == 0:
            #     continue
            print(item)
            if i == 10:
                break
