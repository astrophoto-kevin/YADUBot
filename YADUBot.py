########################################################################################################################
########################################################################################################################
# Copyright information ################################################################################################
#
# YADUBot is copyrighted under the MIT LICENSE and is created by astrophoto.kevin.
# For more information see the license file at http://lizenz
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
########################################################################################################################
########################################################################################################################


########################################################################################################################
# Loading dependencies that are needed to run the code #################################################################
########################################################################################################################

import asyncio
import random
import string
import json
import gettext
from steem import Steem
from discord.ext.commands import Bot

#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################
# Loading config file and assigning variables ##########################################################################
########################################################################################################################

with open('config.json', 'r') as f:     # Open the config file "config.json" in the main directory
    config = json.load(f)               # Load and parse the config file into the config variable

    # Loading the variables that are stored in the config file into the variables that are used in the code
    # All variables that are used to interact with STEEM
    STEEM_USERNAME = config['STEEM_ACCOUNTS']['MAIN_ACCOUNT']
    STEEM_POSTING_KEY = config['STEEM_ACCOUNTS']['MAIN_POSTING_KEY']
    STEEM_VOTING_WEIGHT = config['STEEM_ACCOUNTS']['MAIN_VOTING_WEIGHT']
    STEEM_USERNAME_2ND = config['STEEM_ACCOUNTS']['2ND_ACCOUNT']
    STEEM_POSTING_KEY_2ND = config['STEEM_ACCOUNTS']['2ND_POSTING_KEY']
    STEEM_VOTING_WEIGHT_2ND = config['STEEM_ACCOUNTS']['2ND_VOTING_WEIGHT']

    # All variables that are used to interact with discord
    BOT_NAME = config['DISCORD_SETTINGS']['BOT_NAME']
    BOT_DESCRIPTION = config['DISCORD_SETTINGS']['BOT_DESCRIPTION']
    DISCORD_TOKEN = config['DISCORD_SETTINGS']['DISCORD_TOKEN']

    # All variables that are used to control the bot
    LANGUAGE = config['MAIN_SETTINGS']['LANGUAGE']
    COMMAND_PREFIX = config['MAIN_SETTINGS']['COMMAND_PREFIX']
    BOT_IS_VOTING = config['MAIN_SETTINGS']['BOT_IS_VOTING']
    BOT_IS_VOTING_2ND_ACCOUNT = config['MAIN_SETTINGS']['BOT_IS_VOTING_2ND_ACCOUNT']
    BOT_IS_COMMENTING = config['MAIN_SETTINGS']['BOT_IS_COMMENTING']
    BOT_COMMENT_FILE = config['MAIN_SETTINGS']['BOT_COMMENT_FILE']
    BOT_IS_RESTEEMING = config['MAIN_SETTINGS']['BOT_IS_RESTEEMING']

f.close()       # Close the config file

#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################
# Initialize the bot ###################################################################################################
########################################################################################################################

# Load the language files with gettext and translate the strings
language = gettext.translation('base', localedir='locales', languages=[LANGUAGE])   # Specify the files for gettext
language.install()      # Translate into prior selected language

# Define "discord" as discord bot
discord = Bot(description=BOT_DESCRIPTION, command_prefix=COMMAND_PREFIX)


# Define "steem" as the connection to the STEEM blockchain
steem = Steem(nodes=["https://api.steemit.com",
                     "https://api.steem.house",
                     "https://rpc.curiesteem.com"],
              keys=[STEEM_POSTING_KEY])

# Define "steem" as the connection to the STEEM blockchain, but only voting with a 2nd account is enabled
if BOT_IS_VOTING_2ND_ACCOUNT is True:
    steem2nd = Steem(nodes=["https://api.steemit.com",
                            "https://api.steem.house",
                            "https://rpc.curiesteem.com"],
                     keys=[STEEM_POSTING_KEY_2ND])
#else:
#    pass # Do nothing if the vote with the 2nd account is disabled

#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################
# Checking discord for new messages ####################################################################################
########################################################################################################################

@discord.event      # On every event that is triggered by the discord API
async def on_message(message):  # Run following code if the trigger was because of a new message

    if message.content.startswith(discord.command_prefix):  # If the message starts with the command prefix run the
        await command(message, message.content)             # "command" function and submit the content to the function

#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################
# Commands of the bot ##################################################################################################
########################################################################################################################

async def command(msg,text):

    # Load the message text into the text variable
    text = str(text)
    text = text[1:]

    #*******************************************************************************************************************
    # Command hallo ****************************************************************************************************
    #*******************************************************************************************************************

    if text.lower().startswith('hello'):    # If the message starts with "hello", answer

        # Send hello message
        await discord.send_message(msg.channel, _("Hello Master, I'm awaiting your commands. :robot:"))

    #*******************************************************************************************************************


    #*******************************************************************************************************************
    # Command help *****************************************************************************************************
    #*******************************************************************************************************************

    elif text.lower().startswith('help'):   # If the message starts with "help", answer with the help text.

        # Send help message
        help_message = await discord.send_message(msg.channel, _("Commands and their arguments:\n") \
                + COMMAND_PREFIX + "hello\n"\
                + COMMAND_PREFIX + "upvote <link to post>\n"\
                + COMMAND_PREFIX + "help\n\n"\
                + _("This message will be deleted after 10 seconds."))

        await asyncio.sleep(10)                         # Wait 10 seconds
        await discord.delete_message(help_message)      # and delete the message

    #*******************************************************************************************************************


    #*******************************************************************************************************************
    # Command upvote ***************************************************************************************************
    #*******************************************************************************************************************

    elif text.lower().startswith('upvote'): # If the message starts with "upvote", start the upvote routine.
        try:
            link = text.split(' ')[1]       # remove "upvote" from the string
            post = link.split('@')[1]       # remove all the domain to get the permlink

            # Send messages to show that the upvote routine started
            await discord.send_message(msg.channel, _("I'm trying to upvote this post."))   #
            await discord.send_message(msg.channel, _("Getting post information..."))


            #-----------------------------------------------------------------------------------------------------------
            # Upvote the post ------------------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_VOTING is True:
                try:

                    # Vote on the selected post with the main account
                    steem.commit.vote(post, STEEM_VOTING_WEIGHT, account=STEEM_USERNAME, )

                    # Send message that voting with the main accound was OK
                    await discord.send_message(msg.channel, _("I have successfully upvoted this Post. :white_check_mark:"))

                except:

                    # Send message that voting with the main accound failed
                    await discord.send_message(msg.channel, _("I was not able to upvote this post! :x:"))

            else:
                pass
            #-----------------------------------------------------------------------------------------------------------


            #-----------------------------------------------------------------------------------------------------------
            # Upvote from 2nd account ----------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_VOTING_2ND_ACCOUNT is True:
                try:

                    # Vote on the selected post with the second account
                    steem2nd.commit.vote(post, STEEM_VOTING_WEIGHT_2ND, account=STEEM_USERNAME_2ND, )

                    # Send message that voting with the second accound was OK
                    await discord.send_message(msg.channel, _("2nd Account: I have successfully upvoted this Post."
                                                              " :white_check_mark:"))

                except:

                    # Send message that voting with the second accound failed
                    await discord.send_message(msg.channel, _("2nd Account: I was not able to upvote this post! :x:"))

            else:
                pass
            #-----------------------------------------------------------------------------------------------------------


            #-----------------------------------------------------------------------------------------------------------
            # Comment the upvoted post ---------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_COMMENTING is True:
                try:
                    COMMENT_PERMLINK = "yadubot" + "".join(random.choices(string.digits, k=16)) # Generate a identifier
                    POST_AUTHOR = '@' + post.split('/')[0]      # Extract the username out of the permlink
                    
                    
                    #---------------------------------------------------------------------------------------------------
                    # Replace the &AUTHOR placeholder in the comment file with the name of the post author -------------
                    #---------------------------------------------------------------------------------------------------
                    with open(BOT_COMMENT_FILE, 'r') as myfile:             # Open the comment file
                        BOT_COMMENT = myfile.read().replace('\n', '')       # Remove line feeds
                        BODY = BOT_COMMENT.replace("&AUTHOR", POST_AUTHOR)  # Replace "&AUTHOR" with the name of the author
                    #---------------------------------------------------------------------------------------------------

                    # Comment on the post with the previous loaded text
                    steem.commit.post(title='', body=BODY, author=STEEM_USERNAME, permlink=COMMENT_PERMLINK,
                                      reply_identifier=post)

                    # Send message that commenting the post was OK
                    await discord.send_message(msg.channel, _("I have successfully placed my comment on this Post."
                                                              " :white_check_mark:"))

                except:

                    # Send message that commenting the post failed
                    await discord.send_message(msg.channel, _("I was not able to comment on this post! :x:"))

            else:
                pass

            #-----------------------------------------------------------------------------------------------------------


            #-----------------------------------------------------------------------------------------------------------
            # Resteem the upvoted post ---------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_RESTEEMING is True:
                try:

                    # Resteem the post
                    steem.commit.resteem(post, account=STEEM_USERNAME)

                    # Send message that the resteem was OK
                    await discord.send_message(msg.channel, _("I have successfully resteemed this Post."
                                                              " :white_check_mark:"))

                except:

                    # Send message that the resteem was failed
                    await discord.send_message(msg.channel, _("I was not able to resteem this post! :x:"))

            else:
                pass

            #-----------------------------------------------------------------------------------------------------------


            #-----------------------------------------------------------------------------------------------------------
            # Message that the bot has done its work -------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------

            await discord.send_message(msg.channel, _("I've been working through all the tasks."
                                                          " :white_check_mark:"))

            #-----------------------------------------------------------------------------------------------------------

    #*******************************************************************************************************************


    #*******************************************************************************************************************
    # Error in command *************************************************************************************************
    #*******************************************************************************************************************

        except IndexError:

            # Send message that there was an error in the argument
            index_error = await discord.send_message(msg.channel, _("The used argument is wrong or doesn't exist.\nUse ") \
                                                     + COMMAND_PREFIX + _("help to see how arguments are used.\n\n") \
                                                     + _("This message will be deleted after 10 seconds."))

            await asyncio.sleep(10)                     # Wait 10 seconds
            await discord.delete_message(index_error)   # and delete the message

            return 0

    else:

        # Send message that there was an error in the command
        command_error = await discord.send_message(msg.channel, _("This command doesn't exist.\nUse ") \
                                                   + COMMAND_PREFIX + _("help to see the available commands.\n\n") \
                                                   + _("This message will be deleted after 10 seconds."))

        await asyncio.sleep(10)                         # Wait 10 seconds
        await discord.delete_message(command_error)     # and delete the message

    #*******************************************************************************************************************

#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################
# Starting the bot and writing some lines to the prompt ################################################################
########################################################################################################################

@discord.event      # On every event that is triggered by the discord API
async def on_ready():       # Run following code if the trigger was because the discord client is ready

    # Write a little help tho the shell and show the link to connect the bot to the discord server
    print("")
    print("")
    print("###########################################################################################################")
    print("")
    print(_("Bot is running and waiting for your instructions."))
    print(_("Type ") + COMMAND_PREFIX + _("hello to test it. Type ") + COMMAND_PREFIX + _("help to see the available commands."))
    print("")
    print("https://discordapp.com/oauth2/authorize?discord_id=" + discord.user.id + "&scope=bot&permissions=8")
    print(_("Copy this link to a browser of your choise and connect the bot to your discord server."))
    print("")
    print("###########################################################################################################")

    # If everything is loaded up and ready, start the bot/client
    discord.run(DISCORD_TOKEN)

#-----------------------------------------------------------------------------------------------------------------------
