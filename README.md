# Southwest Airlines Check in Bot
## Introduction:
If you're reading this, you and I both know Southwest has a horrible check in process. If you want any hope of getting a decent seat, so help you God, you'd better hit that button exactly at the 24h mark. Luckily for you, this does it for you.  Good luck. You should probably just pay for priority check in. It's like $15.
    
## Prerequisites
This script requires python 3 and chromedriver. For linux, look at the dependencies; you can figure out the rest with sudo apt. For mac, use homebrew to install these. If you're on a mac and you don't have homebrew, get it:

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/ Homebrew/install/master/install)"
```
Next, clone this repository:

`git clone https://github.com/kclejeune/SouthwestBot.git`

Now we can install chromedriver and python.

`brew cask install chromedriver`
`brew install python`

Now, we've installed chromedriver and python respectively.  
We'll need some additional things to run this, so use:

`pip3 install -r requirements.txt`

## Usage:
Now we have everything necessary for this to work. Nice.
To run:
```bash
cd ~/SouthWestBot/
python3 southwest_bot.py
```
Follow the instructions in the script, don't shut down your computer, and you'll be looking at a seat somewhere hopefully other than the very back of your next southwest flight.


