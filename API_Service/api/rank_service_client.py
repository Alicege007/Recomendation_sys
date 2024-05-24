import requests
from context import Context


def get_rank_animes(context:Context):
    params={}
    params['userid']=context.user_id
    res=requests.get("http://127.0.0.1:5002/rank",params=params)
    return res.json()



def get_recall_animes(context:Context):
    params = {}
    params['animeid'] = context.anime_id
    """直接从recall返回"""
    res = requests.get("http://127.0.0.1:5000/sim", params=params)
    return res.json()

