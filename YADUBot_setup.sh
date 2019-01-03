#!/bin/sh
# Welcome Message
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[1mWelcome to the YADUBot setup script!\e[0m"
echo "\e[39mThis script will install the YADUBot and all necessary depencies.\e[0m" 
echo "\e[39mBased on your systems speed and the speed of your internet connection\e[0m" 
echo "\e[39mit may take a while.\e[0m" 
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[91mPress Enter to continue or CRTL+C to exit...\e[0m"
read _

echo "\e[39m \e[0m"
echo "\e[32mStarting setup script...\e[0m" 
sleep 2

# Update and upgrade
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[32mUpdating and upgrading the system...\e[0m" 
sleep 5
sudo apt-get update && sudo apt-get -y upgrade

# Installing depencies 
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[32mInstalling depencies...\e[0m" 
sleep 5
sudo apt-get -y install build-essential libssl-dev python-dev python3-pip

# Installing python project
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[32mInstalling necessary python projects...\e[0m" 
sleep 5
pip3 install discord
pip3 install steem

# Downloading the bot
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[32mDownloading the bot...\e[0m" 
sleep 5
mkdir yadubot
cd yadubot
wget https://raw.githubusercontent.com/astrophoto-kevin/YADUBot/master/YADUBot.py
wget https://raw.githubusercontent.com/astrophoto-kevin/YADUBot/master/start_bot.sh
sudo chmod +x start_bot.sh

# Setup finished
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
echo "\e[32mThe bot was successfully installed.\e[0m" 
echo "\e[39m \e[0m"
echo "\e[39m \e[0m"
