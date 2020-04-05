#!/bin/bash
cd ~/Documents/Development/SeaTime/django/frontend
echo "pulling latest code"
git pull
echo "starting Vue application"
npm run serve
