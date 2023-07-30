import os
import json
import pandas as pd
import datetime

today = datetime.date.today()


col_names = ['src','hash','views','likes','reposts','comment_numb','date','owner_id','date_added']
def parse_json(doc,group_name):

    full = []
    for i, patr in doc.items():
        posts = patr['count']
        items_ = patr['items']
        for item in items_:
            hash_ = item.get("hash")  # Replace missing 'hash' with None
            comments = item.get('comments', {}).get('count')  # Replace missing 'comments' count with None
            date = datetime.datetime.fromtimestamp(int(item['date']))
            likes = item.get('likes', {}).get('count')  # Replace missing 'likes' count with None
            owner_id = item.get('owner_id')  # Replace missing 'owner_id' with None
            reposts = item.get('reposts', {}).get('count')  # Replace missing 'reposts' count with None
            text = item.get('text')  # Replace missing 'text' with None
            views = item.get('views', {}).get('count')  # Replace missing 'views' count with None
            data_load = datetime.date.today().strftime('%Y-%m-%d %H:%M:%S')
            lista_ = [
                group_name, hash_,
                views, likes, reposts, comments,
                date, owner_id, data_load
            ]
            full.append(lista_)

    return full

# print(parse_json("science_technology"))


# df = pd.DataFrame(data = parse_json("science_technology"),columns= col_names)
# print(df)
# df['date'] = pd.to_datetime(df['date'])
# df.to_sql(con=engine,index=False, name='vk_data',if_exists='append', )