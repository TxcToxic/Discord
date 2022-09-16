import logging
import traceback
from os import listdir
from os.path import isfile, join
import discord
from discord.ext import commands
logging.basicConfig(level=logging.INFO)
# This the first version! later will come more https://github.com/TxcToxic/Discord


class Slash(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)
        self.bot = self

    async def on_ready(self):
        print(f"Bot started\n\n"
              f"Name   : {client.user.name}\n"
              f"ID     : {client.user.id}\n"
              f"Prefix : {client.command_prefix}")


client = Slash(command_prefix='$', intents=discord.Intents.all(), sync_commands=True, sync_commands_on_cog_reload=True)
server = [12345678910111213]    #Your server ID
client.remove_command('help')


if __name__ == '__main__':
    path = 'Commandlist'
    Commandlist = [file for file in listdir(path) if isfile(join(path, file))]
    for cog in Commandlist:
        try:
            client.load_extension(f'Commandlist.{cog[:-3]}')
        except Exception as exc:
            print(f'Fehler beim Laden Commandlist\n\n')
            print("\n".join(traceback.format_exception(type(exc), exc, exc.__traceback__)))
        else:
            print(f'loaded {cog}')

    token = "".join(open("./token").readlines())
    client.run(token)
