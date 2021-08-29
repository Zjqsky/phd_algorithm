# -*- coding: UTF-8 -*-
import numpy as np
import pandas as pd
import joblib
import conf


class BaseAl:
    def __init__(self):
        self.classifier = None
        pass

    def load_data(self, file_name, label_col, data_cols):
        columns = [label_col] + data_cols
        csv_data = pd.read_csv(file_name, usecols=columns)  # 读取数据

        # 读取标签
        labels = csv_data[label_col].values

        # 读取数据
        data_val = []
        for data_col in data_cols:
            data_val.append(csv_data[data_col].values)
        datas = np.column_stack(data_val)

        return labels, datas
        pass

    def save_model(self, path=conf.MODEL_PATH):
        joblib.dump(self.classifier, path)
        pass

    def load_model(self, path=conf.MODEL_PATH):
        self.classifier = joblib.load(path)
        pass


if __name__ == '__main__':
    base_al = BaseAl()
    labels, datas = base_al.load_data("/Users/zhengjiaqi/python_service/phd_algorithm/data/position_lang_data.txt",
                      "lang", ["longitude", "latitude"])
    print(datas)
    pass
