#!/usr/bin/env fish
cd ..
kill $argv[1]
git pull
python3.8 katbot.py &
disown $last_pid
