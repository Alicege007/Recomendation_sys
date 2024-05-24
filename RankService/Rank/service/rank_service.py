from Rank.context import Context
from Rank.util.recall_service_client import get_recall
from random import sample

def anime_rank(context:Context, n=10):
    res=get_recall(context)
    return sample(res,n)