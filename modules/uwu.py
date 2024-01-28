INFO = {'name': 'uwu enforcer', 'desc': ''}

webhookCache = {}

uwuTable = str.maketrans("lrLR", "wwWW")


async def respondOnText(messageText, messageData):
    if messageData['sender'].bot:
        return

    if messageData['channel'].id != 1090860618904506492:
        return

    uwud = uwuify(messageText)
    if uwud == messageText:
        return

    sender = messageData['sender']
    name = sender.display_name
    img = sender.avatar

    if messageData['channel'].id not in webhookCache:
        webhook = await messageData['channel'].create_webhook(
            name="uwu enforcer")
        webhookCache[messageData['channel'].id] = webhook
    webhook = webhookCache[messageData['channel'].id]
    await messageData['message'].delete()
    await webhook.send(uwud, username=name, avatar_url=img)


def uwuify(txt):
    uwud = txt.translate(uwuTable)
    uwud = uwud.replace(":regional_indicator_l:", ":regional_indicator_w:")
    uwud = uwud.replace(":regional_indicator_r:", ":regional_indicator_w:")
    uwud = uwud.replace("🇱", "🇼")
    uwud = uwud.replace("🇷", "🇼")
    return uwud
