from modules.tarot import tarot
import random
import re

INFO = {
    'name': 'tarot',
    'desc': 'runs on tarot draw N (see github.com/a11ce/tarot)'
}

cards = tarot.loadCards("modules/tarot/cards/cards.csv")


def respondOnText(messageText, messageData):
    if (matched := re.findall("tarot draw ([0-9]+)", messageText)):
        count = int(matched[0])
        s = "```\n"
        for _ in range(count):
            s += "{}\n\n".format(tarot.as60WidthLines(random.choice(cards)))
        return s + "\n```"
