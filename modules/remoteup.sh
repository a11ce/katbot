#!/usr/bin/env fish
kill $argv[1]
git pull
python3.8 katbot.py $argv[2] &
disown $last_pid
