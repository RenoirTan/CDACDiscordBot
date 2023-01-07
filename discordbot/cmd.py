"""
`discordbot.cmd`

This module provides functions and other definitions that the program requires
when executed from the command line.
"""


import argparse
import os

from discordbot.bot import run_bot


HELP_DESCRIPTION = "Run the discord bot that you've created."
HELP_EPILOG = """
There are 3 ways that you can pass your bot's token into your program. By
default, the program will look for the token in the environment variable
DISCORD_TOKEN, but you can override it by passing the token with any of the
following methods:

1. As a command line argument
    Add `--token <your token>` after `python -m discordbot`, like this:
    
    > python -m discordbot --token MyToKeN
    
    If the terminal spits out an error, you could try adding single or double
    quotes to your token like you would with strings in Python.

2. From a file
    Copy and paste your token into a file and run the following command:
    
    > python -m discordbot --token-file /path/to/token
    
    Replace `/path/to/token` with the location of your token file.

3. Through an environment variable
    Set DISCORD_TOKEN to the value of your token, then run:
    
    > python -m discordbot
    
    If you used a different environment variable to store your token, then run:
    
    > python -m discordbot --env NAME_OF_ENV_VAR
"""


def create_argparser():
    """
    Create an `argparse.ArgumentParser` to process command line arguments.
    """
    parser = argparse.ArgumentParser(
        description=HELP_DESCRIPTION,
        epilog=HELP_EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter # preserve indentation
    )
    parser.add_argument("-t", "--token")
    parser.add_argument("-f", "--token-file")
    parser.add_argument("-e", "--env")
    return parser


def _token_from_file(path):
    """
    Get token from a file. This function grabs the first line from the file as
    the token.
    """
    try:
        f = open(path, "r")
        token = f.readline().strip()
    except Exception as e:
        return e
    else:
        return token


def get_token(namespace):
    """
    Extract discord bot's token from an `argparse.Namespace` after the command
    line arguments have been processed by `argparse.ArgumentParser.parse_args`.
    
    Example
    -------
    >>> from discordbot.cmd import create_argparser, get_token
    >>> parser = create_argparser()
    >>> namespace = parser.parse_args()
    >>> token = get_token(namespace)
    
    Parameters
    ----------
    namespace: argparse.Namespace
        Result from the parsed ArgumentParser
    
    Returns
    -------
    Tuple[int, str]
        An error code and token string are returned, with the error code coming
        before the token string. Here's a list of error codes and their
        meanings:
        
        0: All clear
        
        1: No token found even after searching through environment variables.
        The environment variable used to find the token will be stored as the
        second element in the returned tuple (e.g. `(1, "DISCORD_TOKEN")`).
        
        2: Multiple tokens given
        
        3: Couldn't access token file. The path to the token file will be stored
        as the second element in the tuple.
    """
    # grab stuff from parsed arguments list
    token = namespace.token
    token_file = namespace.token_file
    env = namespace.env
    result = None
    
    # if --token was provided
    if token is not None:
        result = token
    
    # if --token-file was provided
    if token_file is not None:
        if result is None:
            result = _token_from_file(token_file)
            # couldn't get token from file
            if isinstance(result, Exception):
                print(result)
                return 3, token_file
        # if another token had already been passed using --token,
        # alert user that there are conflicting inputs
        else:
            return 2, ""

    # try environment variables
    envvar = "DISCORD_TOKEN" if env is None else env
    if result is None:
        result = os.environ.get(envvar)
    # not found
    if result is None:
        return 1, envvar
    
    return 0, result # success


def main():
    parser = create_argparser()
    namespace = parser.parse_args()
    status, token = get_token(namespace)
    if status == 1:
        print(f"No token found! Tried environment variable: {token}")
    elif status == 2:
        print("Multiple tokens found! Don't use --token or --token-file at the same time.")
    elif status == 3:
        print(f"Couldn't access file: {token}")
    if status != 0:
        return status
    print(f"Running bot with token: {token}")
    run_bot(token)
    return status