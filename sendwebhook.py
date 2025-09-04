import requests
from datetime import datetime

url = "https://ptb.discord.com/api/webhooks/1413243029589987379/3V6bLpfY7z4VyVwgsOec_FKurLGbRV_bD58gs6JCe0i1x-X_JloRuQgR7RteNlDwlH2n"

def csendWebhook(fullKey, action): # add, remove
    data = {
        "content": "<@924269659774156822>",
        "embeds": [ 
        {
            "title": "New Action",
            "description": action,
            "fields": [
                {
                "name": f'`{fullKey}`',
                "value": datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                "inline": False
                }
            ]
        }
        ]
    }
    response = requests.post(url, json = data)
    if response.status_code == 204:
        print("Webhook sent!")
    else:
        print(f"Webhook failed to send: {response.status_code} | {response.text}")