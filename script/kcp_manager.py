import os
import pandas as pd
import requests


class App:
    def __init__(self):
        self.file_path: str = '.data'
        self.files: list = os.listdir(self.file_path)
        self.kca_data_url = 'http://127.0.0.1:8000/api/kca-data'

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
        for row in rows:
            _iter = iter(row)
            data = dict(
                filing_date=next(_iter),
                age=next(_iter),
                injury_item=next(_iter),
                injury_caused=next(_iter),
                affected_area=next(_iter),
                affected_place=next(_iter),
            )
            requests.post(self.kca_data_url, data=data)


if __name__ == '__main__':
    app = App()
    app.start_app()
