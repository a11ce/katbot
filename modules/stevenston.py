import random

INFO = {'name': 'stevenston', 'desc': "interactions for katbot's home server"}


def respondOnText(messageText, messageData):
    sender = messageData['sender'].id

    # claire
    if sender == 396422982857392139 and messageText.startswith("s!bw"):
        return [("<@396422982857392139> you're addicted to bedwars",
                 random.randint(10, 30))]

    # gamerbot
    if sender == 813921893567692820:
        if "katbot" in messageText and messageText[-1] == "?":
            return [("good gamer bot ! how are you?", random.randint(3, 5))]
        elif "katbot" not in messageText and "i'm" not in messageText:
            if (not random.randint(0, 3)):
                futureHello = "gamer bot {}".format(
                    random.choice([
                        "hi", "why do you hate me", "are you awake",
                        "tell me a joke", "are you gay", "do my homework",
                        "i love you", "you're cute", "pog"
                    ]))

                return [(futureHello, random.randint(30, 120))]
