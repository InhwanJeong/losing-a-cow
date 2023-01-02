import os
import shutil
import csv
from data_preprocessing import DataPreprocessing


class App:
    def __init__(self):
        self.file_path: str = '../data'
        self.files: list = os.listdir(self.file_path)

    def start_app(self):
        while True:
            print("0. 종료\n1. 데이터 일부 조회")
            input_data = int(input("파일이름 입력:"))
            if not input_data:
                break
            self.__retrieve_data()

    def __retrieve_data(self):
        while True:
            print("b 입력시 뒤로가기")
            print("\n".join(self.files[:5]))
            file = input("파일이름 입력:")
            if file == 'b':
                break
            if file not in self.files:
                continue
            self.__read_csv(file)

    def __read_csv(self, file):
        with open(os.path.join(self.file_path, file), 'r', encoding='euc-kr') as f:
            table = csv.reader(f)
            for i, item in enumerate(table):
                print(item)
                if i == 10:
                    break

    def get_data(self):
        pass

    def upload_data(self):
        pass


if __name__ == '__main__':
    app = App()
    app.start_app()
