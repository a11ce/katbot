import re
import subprocess

INFO = {
    'name': 'racket evaluator',
    'desc': 'start your message with katrkt and include a code block',
    'help': 'start your message with katrkt and include a code block'
}


async def respondOnText(messageText, messageData):
    if messageText.startswith("katrkt"):
        matched = re.findall("```\n((?s:.*))\n```", messageText)
        if len(matched) == 1:
            with open("modules/racket-eval/in.rkt", "w") as inp:
                inp.write(matched[0])
            subprocess.run(["racket", "modules/racket-eval.rkt"])
            with open("modules/racket-eval/out.txt", "r") as outp:
                return "this module is **very experimental**. please avoid running potentially destructive programs. if you feel a need to poke at the edges of the (Racket) sandbox, you may do so by attempting to gather information about the environment. (n.b. i'm not even on a11ce's computer!)\n> " + "> ".join(
                    outp.readlines())

        elif len(matched) == 0:
            return "where is the code (use triple backticks pls) :("
        else:
            return "one at a time pls my brain is small"
