import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
import pandas as pd
from collections import defaultdict
from Recall.dataset import anime as dataset

def train_emb():
       """
       读取文件
       """
       spark = SparkSession \
              .builder \
              .appName("concre-reall") \
              .getOrCreate()
       rating_df = dataset.spark_load_rating(spark)
       """
       创建物品序列
       """


