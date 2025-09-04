from tinydb import Query

def searchDB(db):
    license = Query()
    name = input("Enter key name: ")
    output = db.search(license.name == name)

    if output:
        for id in output:
            print(f'ID: {id['id']}, Name: {id['name']}')
    else:
        print(f"No ID with the name: {name}")