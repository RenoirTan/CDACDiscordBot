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

## Todo List

- [x] Structure for a Python package (i.e. pyproject.toml etc.)
- [x] Can be executed from command line
- [x] Feature 1: Welcome Message
- [x] Feature 2: Parrot
- [x] Feature 3: Guess the Number
- [x] Feature 4: Simple Calculator
- [x] Feature 5: Circle Calculator
- [ ] Feature 6: Railfence Encode
- [ ] Feature 7: Bubble Sort
- [ ] Feature 8: Emojifier