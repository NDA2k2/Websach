import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("ServiceAccount.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://btl-python-de2-default-rtdb.firebaseio.com/'})

paths = ['/Book1', '/Book2', '/Book3', '/Book4', '/Book5', '/Book6', '/Book7', '/Book8', 
         '/Book9', '/Book10', '/Book11', '/Book12', '/Book13', '/Book14', '/Book15']

data_dictionary = {}

for path in paths:
    ref = db.reference(path)
    data_dictionary[path] = ref.get()

for path, data in data_dictionary.items():
    print(f'Data at {path}: {data}')
