import uuid

def add_license(db):
    name = input("Enter User Name: ")
    uniqueID = str(uuid.uuid4())
    db.insert({"\n"})
    db.insert({
        "id": uniqueID,
        "name": name
    })
    print(f"License added for {name}: {uniqueID}{name}")
