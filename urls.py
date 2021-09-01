from app import app
from handlers import recomment_lang_handler, user_operation_handler

recomment_lang_handler_view = recomment_lang_handler.RecommentLangHandler()
user_operation_handler_view = user_operation_handler.UserOperationHandler()


@app.route('/recommend_lang_list', methods=['GET'])
def recommend_lang_list(*args, **kwargs):
    return recomment_lang_handler_view.recommend_lang_list(*args, **kwargs)


@app.route('/user_operation', methods=['POST'])
def update_user_operation(*args, **kwargs):
    return user_operation_handler_view.update_user_operation(*args, **kwargs)


@app.route('/user_operation', methods=['GET'])
def get_user_operation(*args, **kwargs):
    return user_operation_handler_view.get_user_operation(*args, **kwargs)

