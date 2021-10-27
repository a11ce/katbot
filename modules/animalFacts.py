import requests

animals = {
    'lizard': 'lizards',
    'raccoon': 'raccoon',
    'geese': 'goose',
    'sheep': 'sheep',
    'dingo': 'dingo',
    'camel': 'camel',
    'crab': 'crab',
    'cow': 'cow',
    'hippo': 'hippo',
    'fish': 'fish',
    'chicken': 'chicken',
    'shark': 'shark',
    'lion': 'lion',
    'whale': 'whale',
    'snake': 'snake',
    'cat': 'cat',
    'dog': 'dog',
    'bear': 'bear',
    'orca': 'killerwhale',
    'giraffe': 'giraffe',
    'dolphin': 'dolphin',
}

INFO = {
    'name': 'animal facts',
    'desc': ':)',
    'help': 'here are the animals i know: {}'.format(animals.keys())
}

baseURL = "https://and-here-is-my-code.glitch.me/facts/"


async def respondOnText(messageText, messageData):
    if "katbot what animals do you know" in messageText:
        return " ".join(animals.keys())
    for animal, endpoint in animals.items():
        # ;; is a special case for avoiding a different bot's trigger
        # TODO some sort of general pre-response filtering
        if animal in messageText.lower().split(
        ) and not messageText.startswith(";;"):
            text = list(requests.get(baseURL + endpoint).json().values())[0]
            if "the connotation of a cat" in text:
                return "[CAT FACT HAS BEEN CENSORED]"
            return text


async def respondOnDM(messageText, messageData):
    return await respondOnText(messageText, messageData)
