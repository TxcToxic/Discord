import requests
import os

generateFile = True
if generateFile is True:
    if os.path.exists("./code_notes.txt"):
        pass
    else:
        text = """200 | The request completed successfully
201 | The entity was created successfully
204 | The request completed successfully but returned no content
304 | No action was taken
400 | The request was improperly formatted, or the server couldn't understand it
401 | The Token was missing or invalid
403 | The Token you passed did not have permission to the resource
404 | The resource at the location specified doesn't exist
405 | The HTTP method used is not valid for the location specified
429 | Too many requests
502 | There was not a gateway available to process your request. Wait a bit and retry
5xx | Server had an error processing your request"""
        open("./code_notes.txt", "w").write(text)
else:
    pass

### CONFIG ###

webhook = "https://discord.com/api/webhooks/"
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

while howmany > 0:
    r = requests.post(url=webhook, json=data)
    manysend += 1
    print(f"[!] Status Code: {r.status_code} | Message: {manysend}")
    howmany -= 1
