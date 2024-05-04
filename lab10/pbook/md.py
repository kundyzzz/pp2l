import csv
import psycopg2
from lab10.pbook.database import insert_data, query_data, delete_data, update_data, enter_data, upload_csv

conn = psycopg2.connect(host="localhost",database="suppliers",user="postgres",password="1")
cur = conn.cursor()

# enter_data()
#upload_csv('num.csv')
#enter_data()

delete_data(name='fake')

query_data()