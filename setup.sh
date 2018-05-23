#!/bin/bash

# clone the repostiory
git clone https://github.com/kclejeune/SouthwestBot.git

# check if homebrew is installed and install if not
if [ ! -e /usr/local/bin/brew ]; then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# install necessary dependencies
brew cask install chromedriver
brew install python
clear

# navigate to the directory and install requirements
cd ~/SouthwestBot
pip3 install -r requirements.txt
clear
echo "Installation complete. Refer to README.md for running instructions."
