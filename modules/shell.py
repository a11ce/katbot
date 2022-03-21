import subprocess

INFO = {'name': 'shell', 'desc': 'ssh except bad'}


async def respondOnText(messageText, messageData):
    if messageData['sender'].id == 298235229095723008:
        if messageText.startswith("k$"):
            cmd = messageText[2:].strip()
            return f"```\n{subprocess.run(cmd.split(), stdout=subprocess.PIPE).stdout.decode('utf-8')}\n```"
