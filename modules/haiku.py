from nltk.corpus import cmudict
import string
cmudictconv = cmudict.dict()

INFO = {'name': 'haiku', 'desc': 'haiku detection'}


def syllables(word):
    word = "".join([c for c in word.lower() if c not in string.punctuation])
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

    for word in messageText.split(" "):
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
