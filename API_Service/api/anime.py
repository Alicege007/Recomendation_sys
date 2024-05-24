import csv

anime_file = open('E:/Recomendation_sys_project/archive/parsed_anime.csv', encoding='utf-8')
anime_dict = csv.DictReader(anime_file)
anime_object = {row['anime_id']: row for row in anime_dict}

def get_anime_object(anime_id):
    anime_id=str(anime_id)
    """在读取字典的时候如果没有键就会报错，所以就需要判断"""
    if anime_id not in anime_object:
        return None
    return anime_object[anime_id]