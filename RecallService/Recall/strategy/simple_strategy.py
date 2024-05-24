from Recall.strategy.recall_strategy import RecallStrategy
from Recall.context import Context
from Recall.dataset import anime
from typing import List

class SimpleRecallStrategy(RecallStrategy):

    def __init__(self):
        super().__init__()#初始化基类

    def name(self):
        return 'Simple'

    def recall(self,context,m=20):
        (anime_df, _) = anime.Load_dataset()
        return anime_df.iloc[:m].index.to_list()




