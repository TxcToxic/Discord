import asyncio
import discord
from discord.ext import commands
from TemplateBot2.main import client


class on_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        author = message.author
        channel = message.channel
        message2 = message.content.casefold()
        guild = message.guild
        if message2.startswith(f"{client.command_prefix}help"):
            embed = discord.Embed(title="Help-Command",
                                  description=f"Author   : {author.mention}\n"
                                              f"Channel  : {channel.mention}\n"
                                              f"Message  : {message.content}\n"
                                              f"Message2 : {message2}\n\n"
                                              f"**Commands:**\n"
                                              f"`{client.command_prefix}setup`")
            await message.reply(embed=embed)
        if message2.startswith(f"{client.command_prefix}setup"):
            if author.guild_permissions.administrator:
                pass
            else:
                await message.reply("False Permissions `administrator`")
                return
            embed = discord.Embed(title="Really Sure?",
                                  description="This will **delete all** your **channels**, are you **really sure?** (y/n)\n\n"
                                              "Will create a little community Discord.\n\n"
                                              "**DO NOT USE IF YOUR DISCORD IS BIG OR YOU CREATED MUCH CHANNELS!**\n\n"
                                              "-> [How it looks like](https://imgur.com/a/DCDvUdH) <-")
            await message.reply(embed=embed)
            try:
                msg = await self.bot.wait_for("message", check=lambda m: m.author == author and m.channel.id == channel.id, timeout=10)
                if msg.content.casefold() in ("y", "yes"):
                    for c in guild.channels:
                        await c.delete()
                    for cat in guild.categories:
                        await cat.delete()
                    catOverwrites = {
                        guild.default_role: discord.PermissionOverwrite(view_channel=False)
                    }
                    cat = await guild.create_category(name="----- BOT ----", position=0, overwrites=catOverwrites)
                    cchannel = await guild.create_text_channel(name="📄┃bot",
                                                               topic=f"Channel created by {client.user.name} [BOT]",
                                                               overwrites=catOverwrites, category=cat)
                    embed = discord.Embed(title="Hello",
                                          description=f"This channel got created by the bot: {client.user.name}.\n\n"
                                                      f"Bot template by [-TOXIC-#1835](https://github.com/TxcToxic/Discord).\n\n"
                                                      f"Use `$help` for start.",
                                          color=0x00ff00)
                    await cchannel.send("@everyone", embed=embed)
                    chatCat = await guild.create_category(name="----- CHAT ----", position=1)
                    await chatCat.create_text_channel(name="💬┃General")
                    await chatCat.create_text_channel(name="🤣┃MemeZ")
                    await chatCat.create_text_channel(name="🔊┃Music")
                else:
                    await message.reply("Canceled (`false_answer`)")
            except asyncio.TimeoutError:
                await message.reply("Canceled (`timed_out`)")


def setup(bot):
    bot.add_cog(on_message(bot))
