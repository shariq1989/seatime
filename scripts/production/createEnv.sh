#!/bin/bash
# TODO
# cd ~/home || exit
# mkdir development
# sudo apt install git
# git clone git@github.com:shariq1989/seatime.git

echo "activating python env"
cd /home/development/seatime/bin/ && source activate
cd ..
echo "install pip3"
sudo apt install python3-pip
echo "install requirements"
pip3 install -r requirements.txt
