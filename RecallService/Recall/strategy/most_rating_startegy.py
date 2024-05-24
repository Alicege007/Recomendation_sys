from Recall.strategy.recall_strategy import RecallStrategy
from Recall.dataset.anime import Load_dataset
from random import sample

class MostRatedStrategy(RecallStrategy):
    def __init__(self):
        super().__init__()
        self.create_pool()

    def name(self):
        return "MostRated"

    def create_pool(self):
        (anime_df,_)=Load_dataset()
        sorted_df=anime_df.sort_values(by=['members'],ascending=False)
        self.pool=sorted_df.iloc[:1000].index.to_list()
        print(f"{self.name()} pool loaded")


    def recall(self,context,n):
        return sample(self.pool,n)
