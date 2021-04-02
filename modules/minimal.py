# These are shown when the user runs kathelp
INFO = {'name': 'example module', 'desc': 'responds to a secret phrase'}


def respondOnText(messageText, messageData):
    # messageText is a string with the sent message
    # messageData is a dict with any other helpful data,
    #   feel free to add to it in katbot.py (search for module.respondOnText)
    if "konstantin anna tatyana vasily olga tatyana" in messageText.lower():
        return "omg you found it <@{}>".format(messageData['sender'].id)
