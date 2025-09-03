import asyncio
from tinydb import TinyDB, Query
from add import add_license

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
            #link the remove.py here
            continue
        print("Invalid answer!")
        continue

asyncio.run(Main())