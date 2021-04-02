import random

INFO = {
    'name': 'politeness',
    'desc': 'responds to certain phrases when mentioned'
}

greetings = ["hi", "hello", "hey"]
thankYous = ["thanks", "ty", "thank you"]
youreWelcomes = ["you're welcome", "ofc", "no prob", "np", "yw", "any time"]

# this is a weird model of human interaction huh
mappings = [(greetings, greetings), (thankYous, youreWelcomes)]


def respondOnText(messageText, messageData):
    messageText = messageText.lower()
    if "katbot" in messageText and "tell" not in messageText:
        for triggers, responses in mappings:
            if any(trigger in messageText for trigger in triggers):
                return "{} <@{}>!".format(random.choice(responses),
                                          messageData['sender'].id)
