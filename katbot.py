import importlib
import os
import discord
import secret
import logging
import sys
import asyncio
import subprocess


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
clientIntents = discord.Intents.default()
clientIntents.members = True
client = discord.Client(intents=clientIntents)


@client.event
async def on_ready():
    log('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening, name="kathelp"))
    if len(sys.argv) > 1:
        await client.get_channel(int(sys.argv[1])).send(
            "remote upgrade complete! last change:\n> {}".format(
                subprocess.check_output(['git', 'show', '-s', '--format=%s'
                                         ]).decode('utf-8').strip()))


async def sendLater(message, channel, delay=0):
    await asyncio.sleep(delay)
    await channel.send(message)


async def handleResp(resp, message):
    if isinstance(resp, str):
        await message.channel.send(resp)
    elif isinstance(resp, list):
        for respElem in resp:
            if isinstance(respElem, tuple):
                await sendLater(respElem[0], message.channel, respElem[1])
            elif isinstance(respElem, str):
                await message.channel.send(respElem)
            elif callable(respElem):
                await respElem()
    elif isinstance(resp, dict):
        if 'reacts' in resp:
            for react in resp['reacts']:
                await message.add_reaction(react)
    elif callable(resp):
        await resp()


@client.event
async def on_message_delete(message):
    for module in modules:
        resp = None
        if hasattr(module, 'respondOnDelete'):
            try:
                resp = await module.respondOnDelete(message)
            except:
                logging.exception("during respondOnDelete")
                await message.channel.send(
                    "something just went wrong, please tell @a11ce to check my logs"
                )
        if (resp):
            await handleResp(resp, message)


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        await client.get_channel(909345223505739798).send(
            "dm from {}:\n> {}".format(message.author, message.content))

    # TODO combine with others on_s
    for module in modules:
        resp = None
        if isinstance(message.channel, discord.DMChannel):
            if hasattr(module, 'respondOnDM'):
                try:
                    resp = await module.respondOnDM(message.content, {
                        'sender': message.author,
                        'client': client
                    })
                except:
                    logging.exception("during respondOnText")
                    await message.channel.send(
                        "something just went wrong, please tell @a11ce to check my logs"
                    )

        else:
            try:
                resp = await module.respondOnText(
                    message.content, {
                        'sender': message.author,
                        'channel': message.channel,
                        'voice': message.author.voice,
                        'client': client,
                        'message': message,
                    })
            except discord.errors.HTTPException as e:
                print(e)
                await message.channel.send(
                    "message was too long, are you sure you should be doing that?"
                )
            except SystemExit:
                await message.channel.send("byebye")
                exit()
            except:
                logging.exception("during respondOnText")
                await message.channel.send(
                    "something just went wrong in module {} <@298235229095723008> check my logs pls"
                    .format(module.INFO['name']))
        if (resp):
            await handleResp(resp, message)

    if "kathelp" in message.content:
        if len(message.content.split()) > 1:
            # TODO better selection by name

            if (requestedHelp :=
                    message.content.split("kathelp")[1].strip()) in [
                        module.INFO['name'] for module in modules
                    ]:
                for module in modules:
                    if module.INFO['name'] == requestedHelp:
                        if 'help' in module.INFO:
                            await message.channel.send(
                                "`help for {}:`\n {}".format(
                                    requestedHelp, module.INFO['help']))
                        else:
                            await message.channel.send(
                                "sorry! no help info for {}".format(
                                    requestedHelp))
        else:
            s = "Hi! I'm katbot. I'm entirely modular (except for responding to kathelp), here's what I'm currently running:\n```yaml\n"
            for module in modules:
                s += "{}: {}\n".format(module.INFO['name'],
                                       module.INFO['desc'])
            s += "```\n My source can be found here:\n<https://github.com/a11ce/katbot>\n\nsay 'kathelp <module name>' for more information about a specific module! for example, try 'kathelp example module'"
            await message.channel.send(s)


client.run(secret.discordKey)
