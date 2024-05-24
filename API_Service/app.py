from flask import Flask,jsonify,request
from context import Context
from api.rank_service_client import get_rank_animes,get_recall_animes
from api.anime import get_anime_object
app=Flask(__name__)

@app.route('/recomendation')
def get_recomendation():
    user_id=request.args.get('userid',type=int)
    context=Context(user_id)
    res=get_rank_animes(context)
    anime_object_list=[get_anime_object(aid) for aid in res]
    return jsonify(anime_object_list)


@app.route("/sim")
def get_similar():
    anime_id=request.args.get('animeid',type=int)
    context=Context(anime_id=anime_id)
    """直接从recall service获取，最近邻找到相似物品embedding,然后返回这些animeid"""
    anime_obe_list=get_recall_animes(context)
    re=[get_anime_object(ob) for ob in anime_obe_list]
    return jsonify(re)




if __name__=='__main__':
    app.run(port=5004)




