# These are shown when the user runs kathelp
INFO = {
    'name': 'example module',
    'desc':
    'responds to a secret phrase, say \'kathelp example module\' to find it!',
    # this line is shown when the user requests more information about this module
    # optional but recommended
    'help': "the secret phrase is konstantin anna tatyana vasily olga tatyana!"
}


def respondOnText(messageText, messageData):
    # messageText is a string with the sent message
    # messageData is a dict with any other helpful data,
    #   feel free to add to it in katbot.py (search for module.respondOnText)
    if "konstantin anna tatyana vasily olga tatyana" in messageText.lower():
        return "omg you found it <@{}>".format(messageData['sender'].id)

    # below is an example of the delayed/multiple response mode
    # your module **does not have to use this feature**
    if messageText.startswith("katbot count"):
        countTo = int(messageText.split()[2])
        return [(str(num + 1), num) for num in range(countTo)]
