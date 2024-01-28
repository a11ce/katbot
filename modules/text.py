import re
import secret
import requests
import katVault

INFO = {'name': 'text sender', 'desc': ':)'}


async def respondOnText(messageText, messageData):
    knownNums = katVault.load(blank={})

    print(messageText)
    if "katbot list known numbers" in messageText:
        return str(knownNums)

    if (matched := re.findall("katbot learnNumber <@([0-9]+)> ([0-9]+)",
                              messageText)):
        knownNums[int(matched[0][0])] = int(matched[0][1])
        katVault.save(knownNums)
        return f"ok, i can text <@{matched[0][0]}> at {matched[0][1]}"

    if (matched := re.findall("katbot text *<@([0-9]+)>", messageText)):
        rcpt = int(matched[0])
        msg = messageText.removeprefix("katbot text <@" + matched[0] +
                                       ">").strip()
        if rcpt not in knownNums:
            return "i dont know their number"
        if len(msg) == 0:
            return "please include a message"
        requests.post(
            'https://textbelt.com/text', {
                'phone': str(knownNums[rcpt]),
                'message': msg + "\n\n-katbot",
                'key': secret.textbeltKey,
            })
        return "ok"
