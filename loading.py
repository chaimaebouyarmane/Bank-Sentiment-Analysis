import psycopg2
import json
import pandas as pd

con = psycopg2.connect(
    database='rabat',
    user='root',
    password='MTY0NjctY2JvdXlh',
    host='127.0.0.1',
    port='3306'
)

cursor_obj = con.cursor()


# Iterate over rows using iterrows()
for index, row in dataframe.iterrows():
    agence = row['title']
    adresse = row['address']
    phone = row['phone']
    comment = row['commentaires']
    score = row['semtiment']
    comment_time = row['publishedAtDate']
    
        # Use parameterized query to insert values
    cursor_obj.execute("INSERT INTO banques (agence,adresse,phone,comment,score, time) VALUES (%s, %s, %s, %s, %s)",
                       (agence, adresse,phone,comment,score, comment_time))
    print('inserted')
con.commit()
cursor_obj.close()
con.close()
