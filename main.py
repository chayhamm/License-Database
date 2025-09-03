import asyncio

async def Main():
    while True:
        removeOrAdd = input("Type A to add | Type R to remove: ").lower()
        if removeOrAdd == "a":
            #link the add.py here
            continue
        if removeOrAdd == "r":
            #link the remove.py here
            continue
        print("Invalid answer!")
        continue

asyncio.run(Main())