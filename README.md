# RICSS x CDAC Discord Bot (2023)

This repo contains the discord bot with the features taught in class
implemented.

1. [Setup](#setup)
2. [Todo List](#todo-list)

## Setup

**IMPORTANT!!**
In the examples below, replace `MY_TOKEN` with your discord bot's token.

### Windows (Powershell)

```bat
REM setup environment
git clone https://github.com/RenoirTan/CDACDiscordBot
cd CDACDiscordBot
python3 -m venv venv
venv\bin\Activate.ps1
pip install --editable .

# store your token in a file called secrets.py
echo token="MY_TOKEN" > .\discordbot\secrets.py

REM start bot
python3 discordbot\bot.py
```

### MacOS or Linux (Bash or Zsh)

```sh
# setup environment
git clone https://github.com/RenoirTan/CDACDiscordBot
cd CDACDiscordBot
python3 -m venv venv
source venv/bin/activate
pip install --editable .

# store your token in a file called secrets.py
echo 'token="MY_TOKEN"' > ./discordbot/secrets.py

# start bot
python3 discordbot/bot.py
```

### Generating `discordbot/emojis.py`

The repo should already have `emojis.py` premade already. However if it's not there or you want to recreate it, you can generate a new file if you want. If you are on macOS or Linux, just run the script at `utils/get-emojis/get-emojis.sh`. There is no script for Windows just yet.

## Todo List

- [x] Structure for a Python package (i.e. pyproject.toml etc.)
- [x] Can be executed from command line
- [x] Feature 1: Ping
- [x] Feature 2: Calculator
- [x] Feature 3: Guess the Number
- [x] Feature 4: Parrot
- [x] Feature 5: FizzBuzz
- [x] Feature 6: Bubble Sort
- [x] Feature 7: Railfence Encode
- [x] Feature 8: Emojifier