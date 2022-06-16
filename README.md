# Spoedebot

A Discord bot that generates short nonsense rhymes on demand. Not terribly useful, but good for a few laughs, at least.

The list of words is taken from the [Corpora](https://github.com/dariusk/corpora) project under Creative Commons.

## Dependencies
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/)
- [discord.py](https://discordpy.readthedocs.io/en/latest/index.html)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

They can generally be installed with the commands

`pip install beautifulsoup4`

`pip install discord.py`

`pip install python-dotenv`

## Usage
In order to actually make a bot, first follow the [guide to make a bot account](https://discordpy.readthedocs.io/en/latest/discord.html#discord-intro) and save the bot's token. Note that Discord will only let you see it once.

Then clone the repository and add an environment file called ".env" with the following text:

```
# .env 
DISCORD_TOKEN = [paste token here]
```

Invite your bot to a server and run "bot.py". Once joined and running, type "!spoede" in any channel to have the bot reply with a rhyme.