import re
import random

INFO = {'name': 'diceroll', 'desc': 'runs on NdM'}


def respondOnText(messageText):
    if (found := re.findall("([0-9]+)d([0-9]+)", messageText)):
        found = list(map(int, found[0]))
        diceRolled = [random.randint(1, found[1]) for _ in range(found[0])]
        return "Rolled {} for a total of {}".format(diceRolled,
                                                    sum(diceRolled))
    return False
