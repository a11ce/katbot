import re
import random

INFO = {'name': 'diceroll', 'desc': 'rolls on NdM or fudge on NdF'}

fudge_words = [
    "Terrible", "Poor", "Mediocre", "Fair", "Good", "Great", "Superb"
]


def respondOnText(messageText):
    if (found := re.findall("([0-9]+)d([0-9]+)", messageText)):
        found = list(map(int, found[0]))
        diceRolled = [random.randint(1, found[1]) for _ in range(found[0])]
        return "Rolled {} for a total of {}".format(diceRolled,
                                                    sum(diceRolled))
    elif (n := re.findall("([0-9]+)dF", messageText)):
        n = int(n[0])
        diceRolled = [random.randint(-1, 1) for _ in range(n)]

        fudge_offset = sum(diceRolled) + 3
        if fudge_offset < 0:
            word = "Sub-terrible"
        elif fudge_offset >= 7:
            word = "**LEGENDARY**"
        else:
            word = fudge_words[fudge_offset]

        return "`{}`\n{}!".format(
            " ".join([["-", " ", "+"][d + 1] for d in diceRolled]), word)
    return False
