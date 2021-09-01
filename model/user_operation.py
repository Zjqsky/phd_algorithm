# -*- coding: UTF-8 -*-
from peewee import *
from utils.mysql import COMMON_DB
import time


# 课程
class UserOperation(Model):
    id = IntegerField(primary_key=True)
    user_id = CharField(default='')
    choice_language = CharField(default='')
    longitude = FloatField(default=0)
    latitude = FloatField(default=0)
    location_info = TextField(default='')
    create_time = DateTimeField()
    modify_time = DateTimeField()

    class Meta:
        db_table = 'user_operation'
        database = COMMON_DB


def insert(user_id, choice_language, longitude, latitude, location_info):
    with COMMON_DB.connection_context():
        if UserOperation.select().where(UserOperation.user_id == user_id).exists():
            user_operation_data = UserOperation.get(UserOperation.user_id == user_id)
            user_operation_data.choice_language = choice_language
            user_operation_data.longitude = longitude
            user_operation_data.latitude = latitude
            user_operation_data.location_info = location_info
        else:
            user_operation_data = UserOperation(user_id=user_id, choice_language=choice_language, longitude=longitude,
                                                latitude=latitude, location_info=location_info)
        user_operation_data.save()
    pass


def get(user_id=None):
    if user_id is None:
        return None

    if not UserOperation.select().where(UserOperation.user_id == user_id).exists():
        return None

    user_operation_data = UserOperation.get(UserOperation.user_id == user_id)

    return user_operation_data


def get_train_info():
    user_operation_list = UserOperation.select().dicts()

    return user_operation_list


def model_to_dict_data(data):
    return dict(
        id=data.id,
        user_id=data.user_id,
        choice_language=data.choice_language,
        longitude=data.longitude,
        latitude=data.latitude,
        location_info=data.location_info,
        create_time=int(data.create_time.timestamp()),
        modify_time=int(data.modify_time.timestamp()),
    )
    pass

