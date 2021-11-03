import random

INFO = {'name': 'stevenston', 'desc': "interactions for katbot's home server"}


async def respondOnDelete(message):
    if message.guild.id == 706345833750069260:
        if message.author.id == 203483343281455104:
            return "dilan moment:\n> {}".format(message.content)
        elif message.author.id == 827458123551604756 and "dilan moment" in message.content:
            return "dilan moment (meta):\n> {}".format(
                message.content.split(">")[-1])


async def respondOnText(messageText, messageData):
    if messageData['message'].guild.id == 706345833750069260:
        sender = messageData['sender'].id

        # claire
        if sender == 396422982857392139 and messageText.startswith("s!bw"):
            return [("<@396422982857392139> you're addicted to bedwars",
                     random.randint(10, 30))]

        # dilan. also reaction test
        if sender == 203483343281455104 and (not random.randint(0, 50)):
            return {'reacts': ["🇨", "🇷", "🇮", "🇳", "🇬", "🇪"]}

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
