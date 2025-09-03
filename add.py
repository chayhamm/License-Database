import uuid

def add_license(db):
    name = input("Enter User Name: ")
    uniqueID = uuid.uuid4
    db.insert({f'{uniqueID}{name}'})
    print(f"License added for {name}: {uniqueID}{name}")
