import json
import time
import requests
from database.database import Table_wall_social_media, engine, metadata
from parse_json import parse_json

conn = engine.connect()
table_object = Table_wall_social_media


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


def extract_posts(domain:str = "science_technology", posts_number:int = 100_000):
    token = "Your token here"
    version = "5.131"
    count= 100
    offset = 0

    while offset < posts_number :
        response = requests.get(
            "https://api.vk.com/method/wall.get",
            params= {
                'access_token'  :token,
                'v'             :version,
                'domain'        :domain,
                'count'         :count,
                'offset'        :offset
            })

        data = response.json()
        normalized_data = parse_json(data, group_name=domain)
        load_db(normalized_data)

        offset += count
        time.sleep(0.5)

    return data


def main():
    group_name = input("Enter group name: ")
    posts_data = extract_posts(domain=group_name, posts_number=100)
    with open('output.json', 'w') as f:
        json.dump(posts_data, f)
    print(posts_data)


if __name__ == '__main__':
    main()