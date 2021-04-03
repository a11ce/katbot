import requests

INFO = {'name': 'animal facts', 'desc': ':)'}

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

baseURL = "https://and-here-is-my-code.glitch.me/facts/"


def respondOnText(messageText, messageData):
    for animal, endpoint in animals.items():
        if animal in messageText.lower():
            text = list(requests.get(baseURL + endpoint).json().values())[0]
            if "the connotation of a cat" in text:
                return "[CAT FACT HAS BEEN CENSORED]"
            return text
