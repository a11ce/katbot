import random
#import spacy
#import pyinflect

INFO = {'name': 'stevenston', 'desc': "interactions for katbot's home server"}


#async def respondOnDelete(message):
#    if message.guild.id == 706345833750069260:
#        if message.author.id == 203483343281455104:
#            return "dilan moment:\n> {}".format(message.content)
#        elif message.author.id == 827458123551604756 and "dilan moment" in message.content:
#            return "dilan moment (meta):\n> {}".format(
#                message.content.split(">")[-1])
#

#nlp = spacy.load('en_core_web_sm')
async def respondOnText(messageText, messageData):
    if messageData['message'].guild.id == 706345833750069260:
        sender = messageData['sender'].id

        if messageData['message'].channel.id == 950126167493595206:
            await messageData['message'].delete()

        if ("katbot ping") in messageText.lower():
            pstr = ""
            for member in messageData['message'].guild.members:
                pstr += "<@{}> ".format(member.id)
            return pstr

        #print(messageText)
        #if (not random.randint(0, 20)):
        #    tokens = nlp(messageText)
        #    for token in tokens:
        #        if token.pos_ == 'VERB':
        #            for item in token.children:
        #                if (item.dep_ == "dobj" or item.dep_ == "dative"):
        #                    vp = str(token._.inflect("VBD"))
        #                    if vp == "None":
        #                        vp = str(token) + "ed"
        #                #print(vp)
        #                    return "i " + vp + " your mom's " + str(
        #                        item) + " last night"

        # claire
        if sender == 396422982857392139 and messageText.startswith("s!bw"):
            return [("<@396422982857392139> you're addicted to bedwars",
                     random.randint(10, 30))]

        #if (not random.randint(0, 100)):
        #    return {
        #        'reacts':
        #        random.choice([["🇨", "🇷", "🇮", "🇳", "🇬", "🇪"],
        #                       [
        #                           "🇧",
        #                           "🇦",
        #                           "🇸",
        #                           "🇪",
        #                           "🇩",
        #                       ], ["⭐"]])
        #    }

        # gamerbot
        if sender == 813921893567692820:
            if "katbot" in messageText and messageText[-1] == "?":
                return [("good gamer bot ! how are you?", random.randint(3,
                                                                         5))]
            elif "katbot" not in messageText and "i'm" not in messageText:
                if (not random.randint(0, 3)):
                    futureHello = "gamer bot {}".format(
                        random.choice([
                            "hi", "why do you hate me", "are you awake",
                            "tell me a joke", "are you gay", "do my homework",
                            "i love you", "you're cute", "pog",
                            "gamer bot drop an L on <@203483343281455104>"
                        ]))

                    return [(futureHello, random.randint(30, 120))]
