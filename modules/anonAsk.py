import random
import pickle
import os
import requests

INFO = {
    'name':
    'anonAsk',
    'desc':
    'enables semi-anonymous questions',
    'help':
    'dm me `ask [channelCode] [your question]` and i\'ll ask it for you. this isn\'t anonymous to admins though! to respond to a question, begin your message with @[codename]'
}

channelCodes = {
    'a11ce': (298235375476932618, 902451668166250506),
    'stevenston': (902773710547714078, 902451668166250506)
}

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
    chanCode = messageText.split()[1]
    if messageText.split()[0] == 'ask' and chanCode in channelCodes:
        name = newName()
        nameCache[name] = messageData['sender'].id
        #print(messageData['sender'].id)
        question = messageText.split(chanCode)[-1]
        message = "{} says:\n>{}".format(name, question)
        logMessage = "{} ({}) says:\n>{}".format(messageData['sender'], name,
                                                 question)

        await messageData['client'].get_channel(channelCodes[chanCode][0]
                                                ).send(message)
        if channelCodes[chanCode][1] is not None:
            await messageData['client'].get_channel(channelCodes[chanCode][1]
                                                    ).send(logMessage)
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
