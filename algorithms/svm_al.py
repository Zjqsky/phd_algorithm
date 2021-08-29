# -*- coding: UTF-8 -*-
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
import logging
import numpy as np

from algorithms import base_al


class SvmAl(base_al.BaseAl):
    def __init__(self, model_path):
        super().__init__()

        self.model_path = model_path

    def train(self, labels, datas):
        logging.info('svm model start train ...')
        model = OneVsRestClassifier(SVC(kernel='linear', probability=True))
        self.classifier = model.fit(datas, labels)
        self.save_model(self.model_path)
        logging.info('svm model finish train, path:%s', self.model_path)

        pass

    def predictFir(self, feature):
        if self.classifier is None:
            self.load_model(self.model_path)

        pred_label = self.classifier.predict([feature])[0]

        return pred_label
        pass

    def predictPre(self, feature, num):
        if self.classifier is None:
            self.load_model(self.model_path)

        # 预测，生成概率矩阵
        pred_proba = self.classifier.predict_proba([feature])[0]
        logging.info('svm model predict pred_proba: %s, classes: %s', str(pred_proba), str(self.classifier.classes_))

        # 从大到小按照概率排序并取前num标签
        pred_proba_labels = self.classifier.classes_[np.argsort(-pred_proba[:])[:num]]

        return pred_proba_labels
        pass

    def predictDis(self, feature, num):
        if self.classifier is None:
            self.load_model(self.model_path)

        # 预测，生成距离矩阵
        pred_dis = self.classifier.decision_function([feature])[0]
        logging.info('svm model predict pred_dis: %s, classes: %s', str(pred_dis), str(self.classifier.classes_))

        # 从大到小按照概率排序并取前num标签
        pred_dis_labels = self.classifier.classes_[np.argsort(-pred_dis[:])[:num]]

        return pred_dis_labels
        pass


if __name__ == '__main__':
    svm_al = SvmAl('../algorithm_models/classifier.model')
    labels, datas = svm_al.load_data("/Users/zhengjiaqi/python_service/phd_algorithm/data/position_lang_data.txt",
                                      "lang", ["longitude", "latitude"])
    # svm_al.train(labels, datas)
    svm_al.predictPre(datas[0], 2)
    pass