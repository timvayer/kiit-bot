#!/bin/bash

echo "🟡 $(date) — ЗАПУЩЕНО deploy.sh" >> bot.log

cd /home/clouduser/kiit-bot || exit
git pull origin main >> bot.log

echo "🟢 $(date) — pull завершено" >> bot.log

pkill -f main.py
source venv/bin/activate
nohup python3 main.py >> bot.log 2>&1 &

