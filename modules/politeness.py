import random

INFO = {
    'name':
    'politeness',
    'desc':
    'responds to certain phrases',
    'help':
    'try saying hi, goodnight, or asking me about my pronouns! i also like saying poggers'
}

# phrase sets
greetings = ["hi", "hello", "hey"]
thankYous = ["thanks", "ty", "thank you"]
youreWelcomes = ["you're welcome", "ofc", "no prob", "np", "yw", "any time"]
goodnights = [
    "night", "night night", "goodnight", "good night", "sleep well",
    "sweet dreams", "gn", "nini"
]
meows = ["meow", "mew", "mraow"]

# specific questions
questions = [(["pronouns"], "i like she/her or it/its!"),
             (["color", "colour"], "purple!")]

# absolute responses
absoluteResponses = [(["poggers"], [("poggers!", 3)])]

# this is a weird model of human interaction huh
mappings = [(greetings, greetings), (thankYous, youreWelcomes),
            (goodnights, goodnights), (meows, meows)]


async def respondOnDM(messageText, messageData):
    return await respondOnText(messageText, messageData)


async def respondOnText(messageText, messageData):
    messageText = messageText.lower()
    if (not messageData['sender'].bot
        ) and "katbot" in messageText and "tell" not in messageText:
        for triggers, responses in mappings:
            if any(trigger in messageText for trigger in triggers):
                return "{} <@{}>!".format(random.choice(responses),
                                          messageData['sender'].id)
        for question in questions:
            if any(prompt in messageText
                   for prompt in question[0]) and "?" in messageText:
                return question[1]

    for response in absoluteResponses:
        if any(prompt in messageText for prompt in response[0]):
            return response[1]
