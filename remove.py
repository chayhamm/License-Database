from tinydb import Query
from sendwebhook import csendWebhook

def removeKey(db):
    license = Query()
    key = input("Enter License Key: ")
    name = input("Enter Key Name: ")
    db.remove((license.id == key) & (license.name == name))
    print(f'Removed: {key}')