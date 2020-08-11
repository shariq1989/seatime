#!/bin/bash
cd ~/Documents/Development/SeaTime/django/frontend || exit
echo "pulling latest code"
git pull
echo "starting Vue application"
npm run serve
