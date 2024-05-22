import firebase_admin
from firebase_admin import credentials, db
import json

SA_Key = 'ServiceAccount.json'

database_url = 'https://btl-python-de2-default-rtdb.firebaseio.com/'

data_file = 'data.json'

cred = credentials.Certificate(SA_Key)

firebase_admin.initialize_app(cred, {'databaseURL': database_url})

with open(data_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

ref = db.reference('/')
ref.set(data)

print("Upload dữ liệu thành công tới database!")
