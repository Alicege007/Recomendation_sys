import pandas as pd

def Load_dataset():
    anime_data=pd.read_csv('E:/Recomendation_sys_project/archive/parsed_anime.csv', index_col='anime_id')
    rating_data=pd.read_csv('E:/Recomendation_sys_project/archive/rating.csv')
    return (anime_data,rating_data)

def spark_load_rating(spark):
    rating_df=spark.read.csv('E:/Recomendation_sys_project/archive/rating.csv')
    return rating_df


