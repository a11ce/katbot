#!/usr/bin/env fish
kill $argv[1]
git pull
python3.9 katbot.py $argv[2] &
disown $last_pid
