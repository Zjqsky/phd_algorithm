from utils.wrappers import api, validate, Field
from utils.api import Response, ApiStatusCode
import logging
from algorithms import svm_al


class RecommentLangHandler:
    def __init__(self, *args, **kwargs):
        pass

    @api
    @validate(
        Field('recommend_num', int, default=1),
        Field('longitude', float, required=True),
        Field('latitude', float, required=True),
    )
    def recommend_lang_list(self, recommend_num, longitude, latitude, *args, **kwargs):
        pred_proba_labels = svm_al.predictPre([longitude, latitude], recommend_num)
        recommend_lang_list = pred_proba_labels.tolist()
        return Response(data={"recommend_lang_list": recommend_lang_list}, status=ApiStatusCode.ok.value)
