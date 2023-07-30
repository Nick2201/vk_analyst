from sqlalchemy import create_engine
from sqlalchemy import ( create_engine,
    MetaData, Table,Column,
    String, DateTime,Integer)
from sqlalchemy.orm import sessionmaker


DB_CONFIG = {
    "host": "localhost",
    "database": "vk_social_media",
    "user": "postgres",
    "port": "5432",
    "password": "22051969"
}
dialect = 'postgresql'
unpack_conf = dialect + '://{user}:{password}@{host}:{port}/{database}'.format(**DB_CONFIG)

engine = create_engine(unpack_conf)

print(unpack_conf)


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

conn = engine.connect()
metadata.create_all(engine)