import json
import discord

def create_help(avatar_url):
    with open("commands.json", "r") as f:
       commands = json.load(f)
       embed = discord.Embed(description = commands["description"], colour=0xFF00CC)
       embed.set_author(name = "greatbot commands", icon_url = avatar_url)
       for i in commands["commands"]:
           embed.add_field(name = i["title"], value = i["description"], inline = False)

       f.close()

    return embed