import re
import random
from datetime import datetime, date

INFO = {
    'name':
    'crab decider',
    'desc':
    'crab',
    'help':
    'ask me who the Crab Decider is. it changes daily at midnight. they can carcinize people by saying `carcinize @user`'
}


async def todaySeed():
    today = date.today()
    # lol crab in ascii is all numeric
    return int(today.strftime("%Y%m%d")) + 63726162 + 27


async def getDeciderID(guild):
    users = [m for m in guild.members if not m.bot]
    random.seed(await todaySeed())
    return random.choice(users).id


async def respondOnText(messageText, messageData):
    deciderID = await getDeciderID(messageData['message'].guild)

    if all(map(lambda s: s in messageText.lower(), ["who", "crab"])):
        return "<@{}> is the Crab Decider today!".format(deciderID)
    if (matched := re.findall("carcinize *<@!([0-9]+)>", messageText.lower())):
        if messageData['sender'].id == deciderID:
            matched = matched[0]
            await messageData['message'].guild.get_member(int(matched)
                                                          ).edit(nick="crab")
            return "<@{}> you are now crab".format(matched)
        else:
            return "you are not the Crab Decider today"
