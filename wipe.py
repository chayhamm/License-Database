from tinydb import Query
import requests

url = "https://ptb.discord.com/api/webhooks/1413247248325804204/8N6b0dp6_bvDZ7cGMVhJXnHJ19e49xJcH-BUz6lH44RTmd9BKtfjTjf_g-dSUV2AdQlw"

def wipeAll(db):
    data = {
        "content": "<@924269659774156822>"
    }
    db.truncate()
    requests.post(url, json = data)
    print("Wiped all License Keys!")