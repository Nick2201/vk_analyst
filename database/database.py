from sqlalchemy import create_engine
from sqlalchemy import ( create_engine,
    MetaData, Table,Column,
    String, DateTime,Integer)
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение значений переменных окружения
host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USER")
port = os.getenv("PORT")
password = os.getenv("PASSWORD")
# DB_CONFIG = {
#     "host": "localhost",
#     "database": "vk_social_media",
#     "user": "postgres",
#     "port": "5432",
#     "password": "22051969"
# }
host = os.getenv("HOST")
database = os.getenv("DATABASE")
user = os.getenv("USER")
port = os.getenv("PORT")
password = os.getenv("PASSWORD")

# Создание строки подключения и создание объекта engine
connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)



metadata = MetaData()
# ['src','hash','views','likes','reposts','comment_numb','date','owner_id']

Table_wall_social_media = Table (
    'wall_social_media', metadata,
    Column('id', Integer(), primary_key=True),
    Column('src', String(30)),
    Column('hash', String(30),unique=True),
    Column('views', Integer()),
    Column('likes', Integer()),
    Column('reposts', Integer()),
    Column('comment_numb', Integer()),
    Column('date', DateTime()),
    Column('owner_id', String(30)),
    Column('date_added', DateTime()),
)

