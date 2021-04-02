import importlib
import os
import discord
import secret
import logging


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
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="kathelp"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    for module in modules:
        try:
            if (resp := module.respondOnText(message.content,
                                             {'sender': message.author})):
                await message.channel.send(resp)
        except discord.errors.HTTPException:
            await message.channel.send(
                "message was too long, are you sure you should be doing that?")
        except:
            logging.exception("during respondOnText")
            await message.channel.send(
                "something just went wrong in module {} <@298235229095723008> check my logs pls"
                .format(module.INFO['name']))

    if "kathelp" in message.content:
        s = "Hi! I'm katbot. I'm entirely modular (except for responding to kathelp), here's what I'm currently running:\n```yaml\n"
        for module in modules:
            s += "{}: {}\n".format(module.INFO['name'], module.INFO['desc'])
        s += "```"
        await message.channel.send(s)


client.run(secret.discordKey)
