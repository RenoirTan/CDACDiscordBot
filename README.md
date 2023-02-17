# RICSS x CDAC Discord Bot (2023)

This repo contains the discord bot with the features taught in class
implemented.

1. [Setup](#setup)
2. [Todo List](#todo-list)

## Setup

Replace `MY_TOKEN` with your discord bot's token.

### Windows

```bat
REM setup environment
git clone https://github.com/RenoirTan/CDACDiscordBot
cd CDACDiscordBot
python3 -m venv venv
venv/bin/Activate.ps1
pip install --editable .

REM store token into a file
echo MY_TOKEN> .\token

REM start bot
python3 -m discordbot -f .\token
```

### MacOS or Linux

```sh
# setup environment
git clone https://github.com/RenoirTan/CDACDiscordBot
cd CDACDiscordBot
python3 -m venv venv
source venv/bin/activate
pip install --editable .

# store token into a file
echo 'MY_TOKEN' > ./token

# start bot
python3 -m discordbot -f ./token
```

### Generating `discordbot/emojis.py`

The repo should already have `emojis.py` premade already. However if it's not there or you want to recreate it, you can generate a new file if you want. If you are on macOS or Linux, just run the script at `utils/get-emojis/get-emojis.sh`. There is no script for Windows just yet.

## Todo List

- [x] Structure for a Python package (i.e. pyproject.toml etc.)
- [x] Can be executed from command line
- [x] Feature 1: Welcome Message
- [x] Feature 2: Parrot
- [x] Feature 3: Guess the Number
- [x] Feature 4: Simple Calculator
- [x] Feature 5: Circle Calculator
- [x] Feature 5a: FizzBuzz
- [x] Feature 6: Railfence Encode
- [x] Feature 7: Bubble Sort
- [x] Feature 8: Emojifier