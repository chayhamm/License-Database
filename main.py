import asyncio
from tinydb import TinyDB, Query
from add import add_license
from remove import removeKey
from wipe import wipeAll
from search import searchDB

async def Main():
    database = TinyDB('licenses.json')
    license = Query()
    run = True

    while run == True:
        removeOrAdd = input("Type A to add | Type R to remove | Type S to search | Type W to wipe: ").lower()
        if removeOrAdd == "a":
            add_license(database)
            continue
        if removeOrAdd == "r":
            removeKey(database)
            continue
        if removeOrAdd == "w":
            wipeAll(database)
            continue
        if removeOrAdd == "s":
            searchDB(database)
            continue
        else:
            print("Invalid answer!")
            continue

asyncio.run(Main())