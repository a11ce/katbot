import socket
import os
import subprocess

INFO = {'name': 'admin tools', 'desc': 'only works when called by a11ce'}


def respondOnText(messageText, messageData):
    if messageData['sender'].id == 298235229095723008:
        if messageText.startswith("katbot override"):
            if "sigkill" in messageText:
                exit()
            if "whereareyou" in messageText:
                return socket.gethostname()
            if "pid" in messageText:
                return os.getpid()
            if "remoteup" in messageText:
                os.system("modules/remoteup.sh {} {}".format(
                    os.getpid(), messageData['channel'].id))
            if "hash" in messageText:
                return str(
                    subprocess.check_output(
                        ['git', 'rev-parse', '--short', 'HEAD']))
