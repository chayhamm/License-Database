from tinydb import TinyDB, Query
import uuid

def add_license(db):
    name = input("Enter User Name: ")
    db.insert({uuid.uuid4})
