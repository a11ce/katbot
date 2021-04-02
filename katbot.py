import importlib
import os
import discord
import secret


def log(text):
    print(text)


def loadModules():
    modules = []
    for module in os.listdir("modules"):
        if "__" not in module and ".py" in module:
            modules.append(
                importlib.import_module('.' + module[:-3], 'modules'))
    log("Loaded {} modules".format(len(modules)))
    for module in modules:
        log("LOADED MODULE: " + module.INFO['name'])
    return modules


modules = loadModules()
client = discord.Client()


@client.event
async def on_ready():
    log('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for module in modules:
        if (resp := module.respondOnText(message.content)):
            await message.channel.send(resp)

    if "kathelp" in message.content:
        s = "Hi! I'm katbot. I'm entirely modular (except for responding to kathelp), here's what I'm currently running:\n```yaml\n"
        for module in modules:
            s += "{}: {}\n".format(module.INFO['name'], module.INFO['desc'])
        s += "```"
        await message.channel.send(s)


client.run(secret.discordKey)
