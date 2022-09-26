import asyncio
import discord

# made by -TOXIC-#1835, don't use it for illegal stuff except it's not my blame ¯\_(ツ)_/¯

intents = discord.Intents.all()
client = discord.Client(intents=intents)
exceptions = []


@client.event
async def on_ready():
    print("Slave online")


@client.event
async def on_message(message):
    if message.author.bot:
        return
    message2 = message.content.casefold()
    if message2.startswith("$exc"):
        args = message2.split(" ")
        if args[1] == "clear":
            deleted = 0
            for x in exceptions:
                deleted += 1
            exceptions.clear()
            await message.reply(f"{deleted} exceptions got cleared")
        elif args[1] == "add":
            if args[2].isdigit():
                try:
                    exceptions.append(str(args[2]))
                    excList = ", ".join(exceptions)
                    await message.reply(f"successfully added\n\n"
                                        f"**Exceptions:**\n"
                                        f"```"
                                        f"{excList}"
                                        f"```")
                except:
                    await message.reply("There was an error :/")
            else:
                await message.reply("The ID must be a number!")
        elif args[1] == "info":
            await message.reply("This command works easy\n\n"
                                "`clear` - clears the list\n"
                                "`add <CHANNELID/CATEGORYID>` - adds an id (the channel/category will not get deleted)")
        elif args[1] == "list":
            if len(exceptions) == 0:
                excList = "NONE"
            else:
                excList = ", ".join(exceptions)
            await message.reply(f"**Exceptions:**\n"
                                f"```"
                                f"{excList}"
                                f"```")
    if message2.startswith("$clear"):
        await message.reply("**Are you really sure?** this will delete all categories and channels except the "
                            "exceptions!\n\n"
                            "**(Y/N)**")
        try:
            msg = await client.wait_for("message", check=lambda m: m.author == message.author and m.channel.id == message.channel.id,
                                        timeout=10)
            if msg.content.casefold() in ("yes", "y"):
                for c in message.guild.channels:
                    if str(c.id) in exceptions:
                        pass
                    else:
                        await c.delete()
                for cat in message.guild.categories:
                    if str(cat.id) in exceptions:
                        pass
                    else:
                        await cat.delete()
            else:
                await message.reply("Canceled (`false_answer`) // Canceled by Author")
        except asyncio.TimeoutError:
            await message.reply("Canceled (`timed_out`) // Canceled by Client")

client.run("BOT-TOKEN")
