import re

INFO = {'name': 'sayAs', 'desc': ''}


async def respondOnText(messageText, messageData):
    if messageData['sender'].bot:
        return

    if (matched := re.findall("k!as +(?:([^\s`]+)|`([^`]+)`) +(.+)",
                              messageText)):
        await messageData['message'].delete()
        name = matched[0][0] if matched[0][0] else matched[0][1]
        txt = matched[0][2]
        img = None

        if (tagged := re.findall("<@([0-9]+)>", name)):
            member = messageData['message'].guild.get_member(int(tagged[0]))
            name = member.display_name
            img = member.avatar

        webhook = await messageData['channel'].create_webhook(name=name)
        await webhook.send(txt, username=name, avatar_url=img)
        await webhook.delete()
