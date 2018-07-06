# Southwest Airlines Check in Bot

## Introduction

If you're reading this, you and I both know Southwest has a horrible check in process. If you want any hope of getting a decent seat, so help you God, you'd better hit that button exactly at the 24h mark. Natrually, the only solution is to embrace our robot overlords and their ever-superior clicking abilities.

## The Boring Stuff

*WARNING: This only works on Mac. If you're on linux, take a look at the manual installation info.*
Included with this repository is a script to do all the dirty work for you. I'd recommend you use it, but you do you.

To use it, run:

```bash
curl -s https://raw.githubusercontent.com/kclejeune/SouthwestBot/master/setup.sh | sh
```

The setup script will install everything you need and then clean up. If you use it, you can skip to The Fun Stuff.

## Manual Install (the REALLY boring stuff)

*Warning: These instructions are written with mac in mind, so they use homebrew as the package manager. If you're on linux, follow the instructions using apt-get or yum or whatever package manager you use.*

First, we'll need to make sure you have a magical tool called homebrew. It's very safe, and it'll help you manage scary things in a consistent manner.

```bash
if [ ! -e /usr/local/bin/brew ]; then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
```

Next, clone this repository.

```bash
git clone https://github.com/kclejeune/SouthwestBot.git
```

We'll install chromedriver, python3, and some additional requirements:

```bash
brew cask install chromedriver
brew install python
cd ~/SouthwestBot/
pip3 install -r requirements.txt
```

That's it! Now, check out the fun stuff.

## The Fun Stuff

Now we have everything necessary for this to work. Nice.
To run:

*If 'chromedriver' is not in your path, specify a path to your respective installation as a command line arg. If you don't know what that means, ignore this.*

```bash
python3 ~/SouthwestBot/southwest_bot.py
```

Follow the instructions in the script, don't shut down your computer, and with any luck you'll be looking at a seat somewhere hopefully other than the very back of your next southwest flight.
