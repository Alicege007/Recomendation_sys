import concurrent.futures
import Recall.strategy as Strategy
from typing import List

from Recall.context import Context

#List[Strategy.recall_strategy]指明list的类是Recall_strategy类
strategies:List[Strategy.RecallStrategy]=[
   Strategy.MostRatedStrategy(),
   Strategy.HighRatedStrategy()
]
#猜你喜欢(simple_strategy策略)
def Get_anime(context,n=20)->List[int]:
    with concurrent.futures.ThreadPoolExecutor() as executor:
          outputs=executor.map(lambda s: s.recall(context,n), strategies)
          #[[1,2,3],[1,2,3]]
          outputs=[aid for l in outputs for aid in l]
          #去重
          outputs=list(dict.fromkeys(outputs))
          return outputs

#相似推荐（similar strategy策略）
def Get_sim_anime(context:Context, n=20)->List[int]:
    anime_list=Strategy.SimilarAnimeStrategy().recall(context,n)
    return anime_list

