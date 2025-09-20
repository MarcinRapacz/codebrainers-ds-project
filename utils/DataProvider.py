import pandas as pd

class DataProvider:
    def __init__(self, data_source):
        self.data_source = data_source

    def get_data(self):
        return pd.read_csv(self.data_source)


