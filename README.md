# Southwest Airlines Check in Bot
## Introduction:
If you're reading this, you and I both know Southwest has a horrible check in process. If you want any hope of getting a decent seat, so help you God, you'd better hit that button exactly at the 24h mark. Natrually, the only solution is to embrace our robot overlords and their ever-superior clicking abilities.
    
## The Boring Stuff:
First things first, clone the repository.
```bash
git clone https://github.com/kclejeune/SouthwestBot.git
```
Included with this repository is a script to do all the dirty work for you. To use it, run:
```bash
bash ~/SouthwestBot/setup.sh
```
The setup script will install everything you need and then clean up. If you use it, you can skip to The Fun Stuff.
## If you don't use the script, the following instructions will perform the same steps.
This script requires python 3 and chromedriver. For linux, look at the dependencies; you can figure out the rest with sudo apt. For mac, use homebrew to install these. If you're on a mac and you don't have homebrew, get it:
```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/ Homebrew/install/master/install)"
```
Now we can install chromedriver and python.
```bash
brew cask install chromedriver
brew install python
```
Now, we've installed chromedriver and python respectively.  
We'll need some additional things to run this, so use:
```bash
pip3 install -r requirements.txt
```
## The Fun Stuff:
Now we have everything necessary for this to work. Nice.
To run:
```bash
cd ~/SouthWestBot/
python3 southwest_bot.py
```
Follow the instructions in the script, don't shut down your computer, and you'll be looking at a seat somewhere hopefully other than the very back of your next southwest flight.


