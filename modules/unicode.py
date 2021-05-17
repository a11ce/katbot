import random

INFO = {
    'name':
    'unicoder',
    'desc':
    'responds to messages containing "katbot" and "unicode" with a bunch of weirdly-rendering characters'
}

diac = [
    "\u0300", "\u0020", "\u0301", "\u0302", "\u032C", "\u032D", "\u0303",
    "\u033E", "\u0304", "\u0305", "\u0320", "\u0331", "\u0332", "\u0333",
    "\u033F", "\u0347", "\u0335", "\u0336", "\u035E", "\u035F", "\u0337",
    "\u0338", "\u0306", "\u0311", "\u032E", "\u032F", "\u0310", "\u0351",
    "\u0357", "\u0352", "\u0339", "\u0307", "\u0308", "\u0344", "\u030A",
    "\u0323", "\u0324", "\u0325", "\u0358", "\u0309", "\u0321", "\u0322",
    "\u0327", "\u0328", "\u0345", "\u030F", "\u030B", "\u030C", "\u030D",
    "\u030E", "\u0312", "\u0313", "\u0314", "\u0315", "\u031B", "\u0326",
    "\u0316", "\u0317", "\u0319", "\u0318", "\u031A", "\u0349", "\u031D",
    "\u031E", "\u031F", "\u031C", "\u0329", "\u032A", "\u033A", "\u0346",
    "\u032B", "\u033C", "\u0330", "\u0334", "\u0360", "\u034A", "\u034B",
    "\u034C", "\u033B", "\u0348", "\u034D", "\u034E", "\u0362", "\u0350",
    "\u0354", "\u0355", "\u0356", "\u0359", "\u035A", "\u035B", "\u035C",
    "\u035D", "\u0361", "\u0340", "\u0341", "\u0342", "\u0343"
]
bad = [
    "\u202e",
    "\u202d",
    "\u0629",
    "\u0619",
    "\u06D5",
]


def getChars(n):
    s = ""
    for _ in range(n):
        arr = random.choice([diac, bad])
        #arr = bad
        s += (random.choice(arr))
    return s


def respondOnText(messageText, messageData):
    if "unicode" in messageText.lower() and "katbot" in messageText.lower():
        return getChars(1999)
