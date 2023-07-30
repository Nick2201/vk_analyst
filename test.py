from database.database import Table_wall_social_media,engine,metadata
import pandas as pd
table_object = Table_wall_social_media
conn = engine.connect()
df = pd.read_sql_query(
    '''
SELECT *
FROM wall_social_media
WHERE DATE_PART('year', date) IN (2023,2022,2021)'''
,con=conn
)
df.to_csv('test.csv')