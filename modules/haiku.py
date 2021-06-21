# This is a hack because the servers that katbot normally runs on
# seem to automatically delete nltk-downloaded data at
# random times, so it's saved as a pickle bin instead.
import pickle
with open("modules/cmudict.pkl", 'rb') as f:
    cmudictconv = pickle.load(f)
# if you're running a local copy and are able,
# comment the above and uncomment these two lines:
# from nltk.corpus import cmudict
# cmudictconv = cmudict.dict()
# The previous two lines plus the next 3 in a repl
# were used to generate cmudict.pkl:
# import pickle
# with open("cmudict.pkl", 'wb') as f:
#   pickle.dump(cmudictconv, f)

import string

INFO = {
    'name':
    'haiku',
    'desc':
    'haiku detection',
    'help':
    'i can automatically detect and point out when you write a haiku! if i get something wrong (especially text abbreviations), please message <@298235229095723008> and let her know'
}

# words that kabot doesnt know but should
syllableOverrides = {'katbot': 2, 'katbots': 2, 'w': 1}


def syllables(word):
    word = "".join(
        [c for c in word.lower().strip() if c not in string.punctuation])

    if word in syllableOverrides:
        return syllableOverrides[word]

    return len(
        [phoneme for phoneme in cmudictconv[word][0]
         if phoneme[-1].isdigit()]) if word in cmudictconv else False


# hello to someone whom i expect may read this
#
# a haiku is not
# defined by just syllables
# except in lit class
def respondOnText(messageText, messageData):
    runningSum = 0
    runningString = ""

    for word in messageText.split():
        wordSyl = syllables(word)
        if not wordSyl:
            return

        if all([(runningSum <= threshold)
                == (runningSum + wordSyl <= threshold)
                for threshold in [5, 12, 17]]) or runningSum in [5, 12, 17]:
            runningSum += syllables(word)
            runningString += word + ("\n"
                                     if runningSum in [5, 12, 17] else " ")
        else:
            return

    return runningString if runningSum == 17 else None
