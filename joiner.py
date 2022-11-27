import os
import requests

inviteID = "bxsN3avF"  # without https://discord.gg/
url = f"https://discord.com/api/v9/invites/{inviteID}"
account = {"authorization": "TOKEN",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
r = requests.post(url=url, headers=account)

print(f"[!] Status Code: {r.status_code}")
