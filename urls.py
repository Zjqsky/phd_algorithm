from app import app
from handlers import recomment_lang_handler

recomment_lang_handler_view = recomment_lang_handler.RecommentLangHandler()


@app.route('/recommend_lang_list', methods=['GET'])
def recommend_lang_list(*args, **kwargs):
    return recomment_lang_handler_view.recommend_lang_list(*args, **kwargs)

