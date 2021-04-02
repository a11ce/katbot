import re
import random

INFO = {
    'name': 'diceroll',
    'desc': 'rolls on r{N}d{M}, where M can be "F" for fudge'
}

fudge_words = [
    "Terrible", "Poor", "Mediocre", "Fair", "Good", "Great", "Superb"
]


def respondOnText(messageText, messageData):
    # matches: number of dice, dice size or F, addition with sign, possible opposition modifier
    if (matched :=
            re.findall("r([0-9]+)d([0-9]+|F)((?:\+|\-)[0-9]+)?(\-[0-9+])?",
                       messageText)):
        matched = matched[0]
        if matched[1] == "F":
            diceRolled = [
                random.randint(-1, 1) for _ in range(int(matched[0]))
            ]
            rolledSum = sum(diceRolled)
            fudge_offset = sum(diceRolled) + (int(matched[2]) if matched[2]
                                              else 0) + (int(matched[3])
                                                         if matched[3] else 0)
            if fudge_offset < -3:
                word = "Sub-terrible"
            elif fudge_offset > 3:
                word = "**LEGENDARY**"
            else:
                word = fudge_words[fudge_offset + 3]
            return "`{}`\n{}! ({}{}{})".format(
                " ".join([["-", " ", "+"][d + 1] for d in diceRolled]), word,
                sum(diceRolled), matched[2], matched[3])

        else:
            diceRolled = [
                random.randint(1, int(matched[1]))
                for _ in range(int(matched[0]))
            ]
            total = sum(diceRolled) + (int(matched[2]) if matched[2] else 0)
            return "`{}`\n**{}** ({}{})".format(" ".join(map(str, diceRolled)),
                                                total, sum(diceRolled),
                                                matched[2])
