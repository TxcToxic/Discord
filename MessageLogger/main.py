import time
import discord
import json
import os

if os.path.exists("./config.json"):
    pass
else:
    data = {
        "token": "YOUR TOKEN"
    }
    open("./config.json", "w").write(json.dumps(data, indent=4))
    pass

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True
client = discord.Client()
aToken = json.load(open("config.json", "r"))["token"]


@client.event
async def on_ready():
    print("Message Logger Started!\n\n"
          "Account: {}#{}".format(client.user.name, client.user.discriminator))


@client.event
async def on_message_delete(message):
    if message.content == "":
        return
    else:
        pass
    with open("./deletedMessages.txt", "a") as file:
        file.write(f"MA: {message.author.name}#{message.author.discriminator} | MC: {message.content} |"
                   f" TIME: {time.strftime('%T -- %D')}\n")
        file.close()


@client.event
async def on_message_edit(message_before, message_after):
    if message_before.content == message_after.content:
        return
    else:
        pass
    with open("./editedMessages.txt", "a") as file:
        file.write(f"MA: {message_before.author.name}#{message_before.author.discriminator} "
                   f"| MBC: {message_before.content} | MAC: {message_after.content} | TIME: {time.strftime('%T -- %D')}"
                   f"\n")
        file.close()

client.run(aToken, bot=False)
