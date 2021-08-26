# KatBot

> A totally modular discord bot

## Use it on your server!

- Add it to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=827458123551604756&permissions=378944&scope=bot) (but no promises on uptime as of now).
- Say 'kathelp' for a list of running modules and their descriptions.

## Contributing a module

- Download with `git clone https://github.com/a11ce/katbot.git`
- Grab submodules with `git submodule update --init --recursive`.
- Make a file `secret.py` containing `discordKey = "your testing bot token"` to run your own copy of KatBot.
- Install dependencies as needed if KatBot complains.
- Run with `python3 katbot.py` and make sure your copy is working correctly.
- Read over `minimal.py` in `modules/` for an example of what your module needs. Currently, that means:
    - an info dict with a name, description, and optional help info
    - a `respondOnText` function which takes two arguments (`messageText` and `messageData`) and returns one of: 
        - A string if KatBot should respond to the given message with a single message right away
        - A list of `(responseMessage: str, delayInSeconds: int)`s if KatBot should respond with multiple spaced-out messages or delay her single response (use a 1-element list for that)
        - A dict with any of:
            - Key 'react' and value a list of emojis to add as reactions to the message
        - `None`/`False` if the module shouldn't act on the message
        - An asynchronous function (coroutine) which will be awaited upon returning
- Write your module, test it, and submit a PR!

--- 

All contributions are welcome by pull request or issue.

KatBot is licensed under GNU General Public License v3.0. See [LICENSE](../master/LICENSE) for full text.
