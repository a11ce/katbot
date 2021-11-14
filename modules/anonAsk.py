import random
import pickle
import os
import requests
import re
import discord

INFO = {
    'name':
    'anonAsk',
    'desc':
    'enables semi-anonymous questions',
    'help':
    'dm me `ask [channelCode] [your question]` and i\'ll ask it for you. this isn\'t anonymous to admins though! to respond to a question, begin your message with @[codename]'
}

# TODO something better
channelCodes = {
    'a11ce': (298235375476932618, 902451668166250506),
    'stevenston': (902773710547714078, 902451668166250506),
    'ask-an-instructor': (887755351385063436, 902810584981061633),
    'homework-questions': (887755477134504007, 902810584981061633),
    'power-user-questions': (887755295252701255, 902810584981061633),
}

generalLogs = 902451668166250506

cacheLoc = "cache/anonAsk.p"
if os.path.exists(cacheLoc):
    with open(cacheLoc, "rb") as p:
        nameCache = pickle.load(p)
else:
    nameCache = {}


def saveCache():
    os.makedirs(os.path.dirname(cacheLoc), exist_ok=True)
    with open(cacheLoc, "wb") as p:
        pickle.dump(nameCache, p)


def newName(idx=0):
    name = requests.get("https://api.scryfall.com/cards/random?q=t%3Acreature"
                        ).json()["name"].replace(" ", "")

    if idx == 50:
        raise Exception("anonAsk name-cache full")
    if name in nameCache:
        idx += 1
        return newName(idx=idx)
    return name


async def respondOnDM(messageText, messageData):
    if len(messageText.split()) > 1:
        chanCode = messageText.split()[1]
    else:
        return

    for name in nameCache.keys():
        if "@{}".format(name) in messageText:
            user = await messageData['client'].fetch_user(nameCache[name])
            await user.send("{}, you've received a response!\n> {}".format(
                name, messageText))
            await messageData['client'].get_channel(generalLogs).send(
                "{} responds to {} ({})\n> {}".format(messageData['sender'],
                                                      name, user, messageText))

    if messageText.split()[0] == 'ask':

        name = newName()
        question = messageText.split(chanCode)[-1]

        if chanCode in channelCodes:

            message = "{} says:\n>{}".format(name, question)
            logMessage = "{} ({}) says:\n>{}".format(messageData['sender'],
                                                     name, question)

            messageChannel = messageData['client'].get_channel(
                channelCodes[chanCode][0])
            logChannel = messageData['client'].get_channel(
                channelCodes[chanCode][1])

        elif re.match("^.{3,32}#[0-9]{4}", chanCode):
            client = messageData["client"]
            username, discrim = chanCode.split("#")
            memberResults = list(
                filter(
                    lambda m: m.discriminator == discrim and m.name ==
                    username, client.get_all_members()))

            if len(memberResults) == 0:
                return "user not found: `{}` . please try again".format(
                    chanCode)

            messageChannel = memberResults[0]
            logChannel = generalLogs

            message = "You have a message from {}!:\n>{} \n You may respond by saying `@{} <your response>`".format(
                name, question, name)

            logMessage = "{} ({}) says to {}\n>{}".format(
                messageData['sender'], name, messageChannel, question)

        else:
            return

        if isinstance(messageChannel, int):
            messageChannel = messageData['client'].get_channel(messageChannel)

        if isinstance(logChannel, int):
            logChannel = messageData['client'].get_channel(logChannel)

        await messageChannel.send(message)
        if logChannel:
            await logChannel.send(logMessage)

        nameCache[name] = messageData['sender'].id
        saveCache()
        return "sent! your codename is {}".format(name)


async def respondOnText(messageText, messageData):
    for name in nameCache.keys():
        if "@{}".format(name) in messageText:

            rawMessage = messageData["message"]
            answerLink = "https://discordapp.com/channels/{}/{}/{}".format(
                rawMessage.guild.id, rawMessage.channel.id, rawMessage.id)
            user = await messageData['client'].fetch_user(nameCache[name])
            await user.send("{}, you've received a response!\n{}".format(
                name, answerLink))
