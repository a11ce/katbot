import random

INFO = {
    'name': 'politeness',
    'desc': 'responds to certain phrases when mentioned'
}

greetings = ["hi", "hello", "hey"]
thankYous = ["thanks", "ty", "thank you"]
youreWelcomes = ["you're welcome", "ofc", "no prob", "np", "yw", "any time"]
goodnights = [
    "night", "night night", "goodnight", "good night", "sleep well",
    "sweet dreams", "gn", "nini"
]
# this is a weird model of human interaction huh
mappings = [(greetings, greetings), (thankYous, youreWelcomes),
            (goodnights, goodnights)]


def respondOnText(messageText, messageData):
    messageText = messageText.lower()
    if (not messageData['sender'].bot
        ) and "katbot" in messageText and "tell" not in messageText:
        for triggers, responses in mappings:
            if any(trigger in messageText for trigger in triggers):
                return "{} <@{}>!".format(random.choice(responses),
                                          messageData['sender'].id)
