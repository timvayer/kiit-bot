#!/bin/bash
cd /home/timvayer/kiit-bot || exit
git pull origin main
touch /var/www/timvayer_pythonanywhere_com_wsgi.py
