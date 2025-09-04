import uuid
from sendwebhook import csendWebhook

def add_license(db):
    name = input("Enter User Name: ")
    uniqueID = str(uuid.uuid4())
    db.insert({
        "id": uniqueID,
        "name": name
    })
    print(f"License added for {name}: {uniqueID}{name}")
    wholeKey = f'{uniqueID}{name}'
    csendWebhook(wholeKey, action = "Add")