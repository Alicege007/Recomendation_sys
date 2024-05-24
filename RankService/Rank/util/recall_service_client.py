import requests
#from Rank.config import config
#因为recall service是暴露了一个restful的接口，所以可以通过Python的requests库来进行http的调用
#params是一个空字典，用于存储要传递给HTTP GET请求的参数。
#发送给召回API请求，通过http GET来发送请求
"""params参数是一个字典，用于存储请求的查询参数。这些参数会自动附加到URL的末尾。
例如，如果params字典是{'user_id': 123}, 那么最终的请求URL可能是http://example.com/recall?user_id=123。"""

def get_recall(context):
    params={}
    params['userid']=context.user_id
    res=requests.get("http://127.0.0.1:5000/recall",params=params)
    print(res.json())
    return res.json()
