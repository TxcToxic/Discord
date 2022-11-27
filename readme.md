# Developers:
[-TOXIC-#1835](https://discord.com/users/856594604812009502) & [Cyber Frodo#2750](https://discord.com/users/370986466555199490)
# Instruction:
* Never use our code for illegal stuff!
* Don't use this code for [self-bots](https://support.discord.com/hc/en-us/articles/115002192352-Automated-user-accounts-self-bots-) it's against the [Discord ToS](https://discord.com/terms)
# Requires:
* Python 3.5.3 or higher
* Git
# Imports:
###### *will not show imports like os or time*
* requests
* [discord.py-message-components](https://github.com/mccoderpy/discord.py-message-components/tree/developer) **|** [Install Instructions](https://github.com/TxcToxic/Discord/blob/main/TemplateBot/readme.md#installing)
* asyncio
* pypresence
# Discord return codes:
| Code | Description | 
| - | - |
| 200  | The request completed successfully |
| 201  | The entity was created successfully |
| 204  | The request completed successfully but returned no content |
| 304  | No action was taken |
| 400  | The request was improperly formatted, or the server couldn't understand it |
| 401  | The Token was missing or invalid |
| 403  | The Token you passed did not have permission to the resource |
| 404  | The resource at the location specified doesn't exist |
| 405  | The HTTP method used is not valid for the location specified |
| 429  | Too many requests |
| 502  | There was not a gateway available to process your request. Wait a bit and retry |
| 5xx  | Server had an error processing your request |
# Info & Others:
#### [Mutli Accounting](https://github.com/TxcToxic/Discord/tree/main/MultiAccounting) (*botnet*)
* The same tools but for more accounts at once
#### [Server Cleaner](https://github.com/TxcToxic/Discord/blob/main/server-cleaner.py)
* It's a bot, he'll remove channels and categories (except the "excepted")
#### [Joiner](https://github.com/TxcToxic/Discord/blob/main/joiner.py)
* let the account you want join into the server you want
#### [RPC](https://github.com/TxcToxic/Discord/blob/main/RPC.py)
* Discord Rich Presence (RPC)
#### [Spammer](https://github.com/TxcToxic/Discord/blob/main/spammer.py)
* will spam messages with the account you want
#### [Webhook Spammer](https://github.com/TxcToxic/Discord/blob/main/webhook-spammer.py)
* same as [Spammer](https://github.com/TxcToxic/Discord/blob/main/spammer.py) but with a [Webhook](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
#### [TemplateBot](https://github.com/TxcToxic/Discord/tree/main/TemplateBot):
* without Cogs & Classes
* in 1 file
#### [TemplateBot2](https://github.com/TxcToxic/Discord/tree/main/TemplateBot2):
* with Cogs & Classes
* splittet into more files (Cogs)
#### [MessageLogger](https://github.com/TxcToxic/Discord/tree/main/MessageLogger):
* in 1 file
* will create 2 files
* logs **all** messageevents (except `message_sent`)
