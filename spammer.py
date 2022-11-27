import requests
import os

### CONFIG ###

channelID = "ID"  # Channel ID
account = {"authorization": "TOKEN",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
message = "You bastards"
howmany = 100

### CONFIG ###

url = f"https://discord.com/api/v9/channels/{channelID}/messages"  # !LEAVE THIS!
manysend = 0  # !LEAVE THIS!

while howmany > 0:
    r = requests.post(url=url, headers=account, data={"content": message})
    manysend += 1
    print(f"[!] Status Code: {r.status_code} | Message: {manysend} | Any error")
    howmany -= 1
