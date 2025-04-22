import openai
import secret

client = openai.OpenAI(api_key=secret.openAIkey)

INFO = {'name': '1825', 'desc': 'name a channel 1825'}

webhookCache = {}


async def respondOnText(messageText, messageData):
    if messageText.startswith("k!clean-webhooks"):
        for w in await messageData['message'].guild.webhooks():
            await w.delete()
        global webhookCache
        webhookCache = {}
        return "done"

    if messageData['sender'].bot:
        return
    if messageData['message'].channel.name != "1825":
        return
        
    await messageData['message'].delete()

    print(messageText)
    
    translated = translate(messageText)
    sender = messageData['sender']
    name = sender.display_name
    img = sender.avatar

    if messageData['channel'].id not in webhookCache:
        webhook = await messageData['channel'].create_webhook(
            name="backup system")
        webhookCache[messageData['channel'].id] = webhook
    webhook = webhookCache[messageData['channel'].id]
    await webhook.send(translated, username=name, avatar_url=img)


def translate(txt):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":
                "system",
                "content": [{
                    "type":
                    "text",
                    "text":
                    "Translate the given message to stereotypical 19th century English. You are translating single messages in a chatroom.\n\nRespond only with the translated message. If the message is empty or a single link, return it unchangemd."
                }]
            },
            {
                "role": "user",
                "content": [{
                    "type": "text",
                    "text": txt
                }]
            },
        ],
        response_format={"type": "text"},
        temperature=1,
        max_completion_tokens=2048,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        store=False)
    return response.choices[0].message.content
