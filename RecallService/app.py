from flask import Flask,request,jsonify
from Recall.service import Recall_service
from Recall.context import Context
import requests

app=Flask(__name__)


@app.route("/recall")
def Anime():
    userid=request.args.get("userid",type=int)
    print(f'calling user {userid}')
    context=Context(userid)
    anime_list=Recall_service.Get_anime(context)
    return jsonify(anime_list)


@app.route('/sim')
def Anime_sim():
    anime_id=request.args.get('animeid',type=int)
    context=Context(None, anime_id)
    if anime_id==None:
        return "Anime id is bad",400
    anime_list=Recall_service.Get_sim_anime(context)
    return jsonify(anime_list)


if __name__=='__main__':
    app.run()







