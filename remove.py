def removeKey(db):
    key = input("Enter License Key: ")
    if key not in db:
        print("Not valid key!")
        return
    db.remove({key})
    print(f'Removed: {key}')