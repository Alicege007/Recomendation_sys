import pyspark
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from collections import defaultdict


def build_seq(rating_df):
    """
    每个用户的anime观看序列
    """
    watch_seq_df = rating_df.groupby('user_id').agg(collect_list(col('anime_id').cast('string')).alias("anime_ids"))
    watch_seq = watch_seq_df.collect()
    watch_seq1 = [w['anime_ids'] for w in watch_seq]
    build_matrix(watch_seq1)

def build_matrix(watch_seq1):
    """
    创建邻接矩阵
    """
    matrix = defaultdict(lambda: defaultdict(int))
    for i in range(len(watch_seq1)):
        seq = watch_seq1[i]
        for j in range(len(seq)):
            for k in range(j + 1, len(seq)):
                a = seq[j]
                b = seq[k]
                if a == b:
                    continue
                matrix[a][b] += 1
                matrix[b][a] += 1

