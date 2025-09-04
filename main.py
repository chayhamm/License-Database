import asyncio
from tinydb import TinyDB, Query
from add import add_license
from remove import removeKey
from wipe import wipeAll

async def Main():
    database = TinyDB('licenses.json')
    license = Query()
    run = True

    while run == True:
        removeOrAdd = input("Type A to add | Type R to remove: ").lower()
        if removeOrAdd == "a":
            add_license(database)
            continue
        if removeOrAdd == "r":
            removeKey(database)
            continue
        if removeOrAdd == "w":
            wipeAll(database)
        print("Invalid answer!")
        continue

asyncio.run(Main())