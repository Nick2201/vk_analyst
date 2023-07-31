import json
import csv
import os

import requests
import time
from database.database import Table_wall_social_media,engine,metadata
from parse_json import parse_json
'''
    BUG:
    main:
        1.Ключ "(hash)=(EVA0rFWS74WiUzuRpF-MOWn7tSs)" уже существует

'''
table_object = Table_wall_social_media
conn = engine.connect()


def load_db(data):
    for row in data:
        insert_statement = table_object.insert().values(
        src=row[0],
        hash=row[1],
        views=row[2],
        likes=row[3],
        reposts=row[4],
        comment_numb=row[5],
        date=row[6],
        owner_id=row[7],
        date_added=row[8]
    )
        # Execute the insert statement
        conn.execute(insert_statement)
    metadata.create_all(engine)
    conn.commit()

def extract(        #TASK: divide load & extract paths
    domain:str = "science_technology",
    offset:int = 0  #TASK: call science_technology last post number
    ):
    token = "vk1.a.bmU7MwcqW_MXWgQZQCmf6XA-wQlGK-6jQsTnd3h3E7i9Vkmni8v8AUBYUTus29KjwhNiUs6rtdoa97CE8YLmGLqk1L5zgtWQD6SWaeRa3bzc6nuo6vTZivrpvj5k6IoMgA-vu2SwIiFvMsUJLVCxphZ9TbyZIF6JJF4bHOOD-W5LIRRjv6u-ouD8ZeML9vSUExO-_r2ek0k9TgWCH-kuoQ"
    version = "5.131"
    domain = 'science_technology'
    count= 100

    all_posts = []

    # url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=1000&access_token={token}&v={version}"
    while offset < 100_000:
        req = requests.get(
            "https://api.vk.com/method/wall.get",
            params= {
                'access_token'  :token,
                'v'             :version,
                'domain'        :domain,
                'count'         :count,
                'offset'        :offset
                    })

        src = req.json()

        get_normal_json = parse_json(src,group_name=domain)
        load_db(get_normal_json)

        offset += 100


        time.sleep(0.5)
    return all_posts


def main():
    group_name = input("Введите название группы: ")
    extract(domain=group_name,offset=10_100)


if __name__ == '__main__':
    main()