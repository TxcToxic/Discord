import discord
from discord.ext import commands


class on_guild_join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        catOverwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False)
        }
        cat = await guild.create_category(name="----- BOT ----", position=0, overwrites=catOverwrites)
        channel = await guild.create_text_channel(name="📄┃bot", topic=f"Channel created by {self.bot.user.name} [BOT]",
                                                  overwrites=catOverwrites, category=cat)
        embed = discord.Embed(title="Hello",
                              description=f"This channel got created by the bot: {self.bot.user.name}.\n\n"
                                          f"Bot template by [-TOXIC-#1835](https://github.com/TxcToxic/Discord).\n\n"
                                          f"Use `$help` for start.",
                              color=0x00ff00)
        await channel.send("@everyone", embed=embed)


def setup(bot):
    bot.add_cog(on_guild_join(bot))
