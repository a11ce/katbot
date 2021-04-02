from modules.tarot import tarot
import random

INFO = {
    'name': 'tarot',
    'desc': 'runs on tarot draw N (see github.com/a11ce/tarot)'
}

cards = tarot.loadCards("modules/tarot/cards/cards.csv")


def respondOnText(messageText, messageData):
    if "tarot draw" in messageText:
        count = int(messageText.split("tarot draw")[1].split()[0])
        s = "```\n"
        for _ in range(count):
            s += "{}\n\n".format(tarot.as60WidthLines(random.choice(cards)))
        return s + "\n```"
