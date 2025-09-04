from tinydb import Query

def wipeAll(db):
    license = Query()
    for id in license.id:
        for name in license.name:
            db.remove((id) & (name))
    print("Wiped all License Keys!")