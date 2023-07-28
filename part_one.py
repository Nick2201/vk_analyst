import json
import csv
import os

import requests
import time
app = 'test_2'


def get_posts(domain:str = "science_technology"):
    token = "vk1.a.bmU7MwcqW_MXWgQZQCmf6XA-wQlGK-6jQsTnd3h3E7i9Vkmni8v8AUBYUTus29KjwhNiUs6rtdoa97CE8YLmGLqk1L5zgtWQD6SWaeRa3bzc6nuo6vTZivrpvj5k6IoMgA-vu2SwIiFvMsUJLVCxphZ9TbyZIF6JJF4bHOOD-W5LIRRjv6u-ouD8ZeML9vSUExO-_r2ek0k9TgWCH-kuoQ"
    version = "5.131"
    domain = 'science_technology'
    count= 100
    offset = 0
    all_posts = []

    # url = f"https://api.vk.com/method/wall.get?domain={group_name}&count=1000&access_token={token}&v={version}"
    while offset < 10000:
        req = requests.get("https://api.vk.com/method/wall.get",
                            params= {
                                'access_token'  :token,
                                'v'             :version,
                                'domain'        :domain,
                                'count'         :count,
                                'offset'        :offset
                                            })

        src = req.json()
        for i,patr in src.items():
            posts =  patr['count']
            items_ =  patr['items']
            print(src)
        # offset += 100
        # print(offset)
        all_posts.extend(src)
        time.sleep(0.5)
    return all_posts

def file_writer(all_posts,group_name):
    if os.path.exists(f"{group_name}"):
        print(f"Директория с именем {group_name} уже существует!")
    else:
        os.mkdir(group_name)
    with open(f"{group_name}/{group_name}.csv", "w", encoding="utf-8") as _file:
        csv.writer(_file)


    # # сохраняем данные в json файл, чтобы видеть структуру
    # with open(f"{group_name}/{group_name}.json", "w", encoding="utf-8") as file:
    #     json.dump(src, file, indent=4, ensure_ascii=False)

    # # собираем ID новых постов в список
    # fresh_posts_id = []
    # posts = src["response"]["items"]

    # for fresh_post_id in posts:
    #     fresh_post_id = fresh_post_id["id"]
    #     fresh_posts_id.append(fresh_post_id)



#     """Проверка, если файла не существует, значит это первый
#     парсинг группы(отправляем все новые посты). Иначе начинаем
#     проверку и отправляем только новые посты."""
#     if not os.path.exists(f"{group_name}/exist_posts_{group_name}.txt"):
#         print("Файла с ID постов не существует, создаём файл!")

#         with open(f"{group_name}/exist_posts_{group_name}.txt", "w") as file:
#             for item in fresh_posts_id:
#                 file.write(str(item) + "\n")

#         # извлекаем данные из постов
#         for post in posts:

#             post_id = post["id"]
#             print(f"Отправляем пост с ID {post_id}")

#             try:
#                 if "attachments" in post:
#                     post = post["attachments"]

#                     # забираем фото
#                     if post[0]["type"] == "photo":

#                         photo_quality = [
#                             "photo_2560",
#                             "photo_1280",
#                             "photo_807",
#                             "photo_604",
#                             "photo_130",
#                             "photo_75"
#                         ]

#                         if len(post) == 1:

#                             for pq in photo_quality:
#                                 if pq in post[0]["photo"]:
#                                     post_photo = post[0]["photo"][pq]
#                                     print(f"Фото с расширением {pq}")
#                                     print(post_photo)
#                                     break
#                         else:
#                             for post_item_photo in post:
#                                 if post_item_photo["type"] == "photo":
#                                     for pq in photo_quality:
#                                         if pq in post_item_photo["photo"]:
#                                             post_photo = post_item_photo["photo"][pq]
#                                             print(f"Фото с расширением {pq}")
#                                             print(post_photo)
#                                             break
#                                 else:
#                                     print("Линк или аудио пост")
#                                     break

#             except Exception:
#                 print(f"Что-то пошло не так с постом ID {post_id}!")

#     else:
#         print("Файл с ID постов найден, начинаем выборку свежих постов!")


def main():
    group_name = input("Введите название группы: ")
    get_posts(domain=group_name)


if __name__ == '__main__':
    main()