import os
import requests

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

inviteID = "bxsN3avF"  # without https://discord.gg/
url = f"https://discord.com/api/v9/invites/{inviteID}"
account = {"authorization": "TOKEN"}
r = requests.post(url=url, headers=account, json={})

if r.status_code == 200 or 204:
    print(f"[+] Status Code: {r.status_code} | Account correctly joined!")
else:
    print(f"[-] Status Code: {r.status_code} | Account won't join | Any error")
