from Recall.strategy.recall_strategy import RecallStrategy
from Recall.context import Context
from Recall.dataset import anime

class SimilarAnimeStrategy(RecallStrategy):
    def __init__(self):
        super().__init__()

    def name(self):
        return "SimilarAnimeStrategy"

    def recall(self,context:Context,n):
         """把表格按照评分排序，取该anime_id的上面10个，下面10个"""
         aid=context.anime_id
         (anime_df,_)=anime.Load_dataset()
         sorted_df=anime_df.sort_values(by=['rating'])
         loc_anime=sorted_df.index.get_loc(aid)
         if loc_anime<int(n//2):
             return sorted_df.iloc[0:n].index.tolist()
         elif len(sorted_df)-1-loc_anime<int(n//2):
             return sorted_df.iloc[len(sorted_df)-n:len(sorted_df)].index.tolist()
         return sorted_df.iloc[loc_anime - int((n // 2)):loc_anime + int((n // 2))].index.tolist()

