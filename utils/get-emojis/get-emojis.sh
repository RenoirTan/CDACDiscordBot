#!/usr/bin/env bash

cd $(dirname $0) # Set current directory to utils/get-emojis

filepath=emojis.csv
url=https://raw.githubusercontent.com/datasets/emojis/master/data/emojis.csv

if [ -f "${filepath}" ]; then
    echo " ? Skipping download since ${filepath} already exists."
    echo " ? Please remove or rename it to download a new copy."
else
    echo "Downloading from ${url}"
    curl -o "${filepath}" "${url}"
fi

echo "Generating discordbot/emojis.py..."
# emojis_to.py prints out a python dictionary containing the emojis
# that we can pipe out to emojis.py
./emojis_to.py "${filepath}" > ../../discordbot/emojis.py
if [ $? == 0 ]; then
    echo "Done!"
else
    echo "Errors occurred!"
fi