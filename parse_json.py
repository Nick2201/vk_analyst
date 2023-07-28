import os
import json
import pandas as pd

col_names = ['src','hash','views','likes','reposts','comment_numb','date','owner_id']
def parse_json(group_name:str):
    with open(f"{group_name}/{group_name}.json", "r", encoding="utf-8") as file:
        doc = json.load(file)
        full = []
        for i,patr in doc.items():
            posts =  patr['count']
            items_ =  patr['items']
            for item in items_:
                hash_ = item["hash"]
                comments = item['comments']['count']
                date = item['date']
                likes = item['likes']['count']
                owner_id = item['owner_id']
                reposts = item['reposts']['count']
                text = item['text']
                views = item['views']['count']

                lista_ = [
                    group_name,hash_,
                    views,likes,reposts,comments,
                    date,owner_id,
                    ]

                full.append(lista_)
        return full

# print(parse_json("science_technology"))

df = pd.DataFrame(data = parse_json("science_technology"),columns= col_names)
print(df)
df['date'] = pd.to_datetime(df['date'])
print(df['date'].dtype)