INFO = {'name': 'admin override', 'desc': 'only works when called by a11ce'}


def respondOnText(messageText, messageData):
    if messageData['sender'].id == 298235229095723008:
        if messageText.startswith("katbot override sigkill"):
            exit()
