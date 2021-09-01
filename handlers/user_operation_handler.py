from utils.wrappers import api, validate, Field
from utils.api import Response, ApiStatusCode
from model import user_operation
import logging
from algorithms import svm_al


class UserOperationHandler:
    def __init__(self, *args, **kwargs):
        pass

    @api
    @validate(
        Field('user_id', str, required=True),
        Field('choice_language', str, required=True),
        Field('location_info', str, required=False, default='{}'),
        Field('longitude', float, required=True),
        Field('latitude', float, required=True),
    )
    def update_user_operation(self, user_id, choice_language, location_info, longitude, latitude, *args, **kwargs):
        user_operation.insert(user_id, choice_language, longitude, latitude, location_info)

        return Response(status=ApiStatusCode.ok.value)

    @api
    @validate(
        Field('user_id', str, required=True),
    )
    def get_user_operation(self, user_id, *args, **kwargs):
        user_operation_data = user_operation.get(user_id)
        if user_operation_data is None:
            return Response(message="数据不存在", status=ApiStatusCode.error.value)

        user_operation_info = user_operation.model_to_dict_data(user_operation_data)

        return Response(data=user_operation_info, status=ApiStatusCode.ok.value)

