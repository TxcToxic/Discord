import requests
import time


def webhookDataPrint():
    webhookID = requests.get(url=webhook).json()["id"]
    webhookName = requests.get(url=webhook).json()["name"]
    webhookAvatar = requests.get(url=webhook).json()["avatar"]
    webhookChanID = requests.get(url=webhook).json()["channel_id"]
    webhookGuildID = requests.get(url=webhook).json()["guild_id"]
    webhookToken = requests.get(url=webhook).json()["token"]
    print(f"Webhook Data:\n\n"
          f"Name       : {webhookName}\n"
          f"ID         : {webhookID}\n"
          f"Avatar     : {webhookAvatar}\n"
          f"Channel ID : {webhookChanID}\n"
          f"Guild ID   : {webhookGuildID}\n"
          f"Token      : {webhookToken}")


### CONFIG ###

data = {
    "content": "@everyone you bastards",
    "embeds": [
        {
            "title": "Spamming",
            "description": "This webhook is getting spammed!"
        }
    ],
    # "avatar_url": "https://cdn.discordapp.com/avatars/",
    "username": "Spammed Webhook!"
}
howmany = 100

### CONFIG ###

manysend = 0  # !LEAVE THIS!
print("start spam in 5 seconds...\n")
time.sleep(5)

for url in open("WHU", "r").readlines():
    # webhookDataPrint()  # In this case it would be shitty :/
    while howmany > 0:
        webhook = "{}".format(url.replace('\n', ''))
        r = requests.post(url=webhook, json=data)
        manysend += 1
        print(f"[!] Status Code: {r.status_code} | Message: {manysend}")
        howmany -= 1
