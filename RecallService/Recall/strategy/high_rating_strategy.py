from Recall.strategy.recall_strategy import RecallStrategy
from Recall.dataset import anime
from random import sample

class HighRatedStrategy(RecallStrategy):
      def __init__(self):
          super().__init__()
          self.create_pool()

      def name(self):
          return 'HighRatedStrategy'


      def create_pool(self):
          (anime_df,_)=anime.Load_dataset()
          sorted_df=anime_df.sort_values(by=['rating'])
          self.pool=sorted_df.iloc[:1000].index.tolist()
          print(f"{self.name()} has loaded")

      def recall(self,context,n):
          return sample(self.pool,n)

