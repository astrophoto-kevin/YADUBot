# YADUBot

**YADUBot** is copyrighted under the MIT LICENSE and is created by **astrophoto.kevin**.
For more information see the [LICENSE file](https://github.com/astrophoto-kevin/YADUBot/blob/master/LICENSE)!

I needed a Discord bot for my **ASTROSteem** curation service which is looking for valuable astronomical and astrophotographical content on the STEEM blockchain.

**YADUBot** is a bot that runs in a discord server. It can be used from every user on your discord server, that has the necessary privileges. This means that user management and permissions are made in discord. 
It was made to meet the needs of **ASTROSteem**. However, it can easily be extended with your own functions. I have commented on the code to keep it as easy as possible.
Also, the output of the bot was made in **2 languages**. English and German. You can easily update the languages or add another one.
**YADUBot** also supports voting from a 2nd account. This was implemented because in my trail on [steemauto.com](https://steemauto.com/) I was always below the threshold for an automatic upvote, but I still want to upvote every post that is curated by **ASTROSteem**, even if my Voting Power is below this threshold.

&nbsp;
## What does YADUBot mean?

**YADUBot** is only the acronym for **Y**et **A**nother **D**iscord **U**pvote **Bot**. I'm really not creative namewise. 

&nbsp;
## What skills does the bot have?

**YADUBot** can do the following things:

- Upvoting a STEEM post from its main STEEM account
- Upvoting a STEEM post from a second STEEM account
- Replying to the upvoted post with a comment (larger comments can be stored in a file)
- Resteem the upvoted post
- Output messages in English or German 

&nbsp;
## Commands

**YADUBot** understands the following commands:

- **$hello**
- **$help**
- **$upvote**

The prefix that identifies a command can be freely chosen. It is set to **"$"** by default.

**$hello**
The bot will respond to this command with a short message to show its readiness. 


**$help**
The bot will respond to this command with a short message to show its available commands. 


**$upvote**
The link to the post to be upvoted is entered here as an argument.
For example: 
> $upvote https://steemit.com/introduceyourself/@astrosteem/hello-steem-i-am-astrosteem  

The bot then executes its upvote routine.

&nbsp;
## Bot settings

At the beginning of the Python script, the following settings can be made for the bot. The following examples are for the ASTROSteem bot and must be adapted to your own.

**BOT_NAME = "ASTROSteem-VotingBot"**  
The name of your bot

**BOT_DESCRIPTION = "ASTROSteem-VotingBot"**   
A short description

**COMMAND_PREFIX = "$"**  
Chat prefix to mark a command

**SHOW_INVITE_LINK = True**  
Show the discord invite link in the command prompt when the bot is running

**LANGUAGE = "DE"**  
Language of the messages from the bot . Possible choice DE and EN

**DISCORD_TOKEN = "JDN23535H5W5LÖWJJ35325562FJWFH6463FH6W"**  
Your Security token that was created from discord

**STEEM_USERNAME = "astrosteem"**  
Username of your STEEM account. Without '@'

**STEEM_POSTING_KEY = "SA325366OEGJSD44I6346436HGI36SEGHR7S7K7373O5DSHG"**  
Private Posting Key of your STEEM account

**STEEM_VOTING_WEIGHT = +100**  
Voting Power for the Upvote

**STEEM_USERNAME_2ND = "astrophoto.kevin"**  
Username of your the 2nd STEEM account. Without '@'

**STEEM_POSTING_KEY_2ND = "SGJ235325OJHRJHGHD3663U4SGJ6H43664KFDJSGDHN"**  
Private Posting Key of the 2nd STEEM account

**STEEM_VOTING_WEIGHT_2ND = +50**  
Voting Power for the 2nd upvote

**BOT_IS_VOTING = True**  
Enable / disable upvotes

**BOT_IS_VOTING_2ND_ACCOUNT = True**  
Enable / disable upvote with a second STEEM account

**BOT_IS_COMMENTING = True**  
Enable / disable commenting by the bot

**BOT_IS_RESTEEMING = True**  
Enable / disable resteeming by the bot

**BOT_COMMENT_IS_FILE = True**  
Text of the comment is saved in a file

**BOT_COMMENT = ""**  
Text of the comment that is posted by the bot

**BOT_COMMENT_FILE = "astrosteem.comment"**  
If the comment text is saved in a file you can enter the filename here

&nbsp;
### **Don't bother. The above keys are of course fictitious and will not work :-)**

&nbsp;
## Setup
You can download a little setup script here:
https://raw.githubusercontent.com/astrophoto-kevin/YADUBot/master/YADUBot_setup.sh

The script is for a freshly installed Ubuntu 18.04 LTS Server and can be downloaded with the following command.
> wget https://raw.githubusercontent.com/astrophoto-kevin/YADUBot/master/YADUBot_setup.sh

You need to make the script executable.
> sudo chmod +x YADUBot_setup.sh

And start it with
> ./YADUBot_setup.sh

The script will try to download all the necessary files, system updates, prerequisites and try to install it. Some parts of the script are using "sudo" so you will be prompted to enter your password if it is needed.  

**Please note, that the bot won't start if you have not set the correct discord and STEEM keys.**
**You can set the setting in your favorite editor, e.g. for nano with typing:**

> nano YADUBot.py

After all settings are made the bot can be started with the start script.

> ./start_bot.sh


&nbsp;
### If you want it the manual way
The following packages must be installed.

- **Python 3.6**
- **build-essential**
- **libssl-dev**
- **python-dev**
- **python3-pip**

Also, the following Python3 projects need to be installed.

- **steem**
- **discord**

If all these dependencies are installed, **YADUBot** should work fine.

&nbsp;
## Conclusion
**I hope you have a lot of fun with the bot and it helps you and your community.**
As you can imagine it was a lot of work to develop it. Also, further developments will take a lot of time. It would be a great help if you could tell me about bugs. So I can fix the corresponding parts of the code. Also, it would be great if you will let me know about your improvement suggestions. If you want to send me some donations you can do this in the following ways.  
STEEM: astrophoto.kevin  
BTC: 1LSYjLcet6bkuJASeMm9XNu2U9gvHCgZTc  
Dash: XbxAe19Y2tcu91ttB9smqEnaVezqEB2eRT
