from tinydb import Query

def wipeAll(db):
    db.truncate()
    print("Wiped all License Keys!")