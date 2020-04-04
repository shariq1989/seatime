#!/bin/bash
echo "pulling latest code"
git pull
echo "starting Vue application"
cd ~/Documents/Development/SeaTime/django/frontend && npm run serve
