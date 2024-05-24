from flask import Flask,request,jsonify
from Rank.context import Context
from Rank.service import rank_service
app=Flask(__name__)


@app.route('/rank')
def get_anime():
    user_id =request.args.get('userid',type=int)
    context=Context(user_id)#初始化同时也保存anime id 和 userid
    anime_rank_id=rank_service.anime_rank(context)
    return jsonify(anime_rank_id)


if __name__=='__main__':
    app.run(port=5002)

