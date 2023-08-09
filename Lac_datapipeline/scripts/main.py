import os
import pandas as pd


class App:
    def __init__(self):
        self.file_path: str = '../data'
        self.files: list = os.listdir(self.file_path)

    def start_app(self):
        for file in self.files:
            self.__get_data(file)

    def __get_data(self, file: str):
        df = pd.read_csv(os.path.join(self.file_path, file), encoding='euc-kr')

        key = [
            key for key in df.keys()
            if '접수일' in key and not '코드' in key
               or '위해자연령' in key and not '코드' in key
               or '원인' in key and not '코드' in key
               or '품목대분류' in key and not '코드' in key
               or '부위' in key and not '코드' in key
               or '발생장소' in key and not '코드' in key
        ]
        if len(key) != 6:
            return

        filtered_df = df.get(key)
        rows = filtered_df[:].values.tolist()
        self.__upload_data(rows)

    def __upload_data(self, rows: list):
        # TODO 서버에서 데이터를 받을 수 있도록 준비 및 데이터 업로드
        pass


if __name__ == '__main__':
    app = App()
    app.start_app()
