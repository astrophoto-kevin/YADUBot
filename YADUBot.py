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
# Loading dependecies of the bot #######################################################################################
########################################################################################################################

import asyncio
import random
import string
from steem import Steem
from discord.ext.commands import Bot

#-----------------------------------------------------------------------------------------------------------------------



########################################################################################################################
# Settings of the bot ##################################################################################################
########################################################################################################################

BOT_NAME = ""                                                                   # The name of your bot
BOT_DESCRIPTION = ""                                                            # A short description
COMMAND_PREFIX = "$"                                                            # Chat prefix to mark a command
SHOW_INVITE_LINK = True                                                         # Show the discord invite link in the command prompt when the bot is running
LANGUAGE = "DE"                                                                 # Language of the messages from the bot . Possible choice DE and EN
DISCORD_TOKEN = ""                                                              # Your Security token that was created from discord
STEEM_USERNAME = ""                                                             # Username of your STEEM account. Without '@'
STEEM_POSTING_KEY = ""                                                          # Private Posting Key of your STEEM account
STEEM_VOTING_WEIGHT = +100                                                      # Voting Power for the Upvote
STEEM_USERNAME_2ND = ""                                                         # Username of your the 2nd STEEM account. Without '@'
STEEM_POSTING_KEY_2ND = ""                                                      # Private Posting Key of the 2nd STEEM account
STEEM_VOTING_WEIGHT_2ND = +50                                                   # Voting Power for the 2nd upvote
BOT_IS_VOTING = True                                                            # Enable / disable upvotes
BOT_IS_VOTING_2ND_ACCOUNT = True                                                # Enable / disable upvote with a second STEEM account
BOT_IS_COMMENTING = True                                                        # Enable / disable commenting by the bot
BOT_IS_RESTEEMING = True                                                        # Enable / disable resteeming by the bot
BOT_COMMENT_IS_FILE = True                                                      # Text of the comment is saved in a file
BOT_COMMENT = ""                                                                # Text of the comment that is posted by the bot
BOT_COMMENT_FILE = "my.comment"                                                 # If the comment text is saved in a file you can enter the filename here

#-----------------------------------------------------------------------------------------------------------------------



########################################################################################################################
# Initialize the bot ###################################################################################################
########################################################################################################################

discord = Bot(description=BOT_DESCRIPTION, command_prefix=COMMAND_PREFIX)

steem = Steem(nodes=["https://api.steemit.com", "https://api.steem.house", "https://rpc.curiesteem.com"], keys=[STEEM_POSTING_KEY])

if BOT_IS_VOTING_2ND_ACCOUNT == True:
    steem2nd = Steem(nodes=["https://api.steemit.com", "https://api.steem.house", "https://rpc.curiesteem.com"], keys=[STEEM_POSTING_KEY_2ND])
else:
    DO_NOTHING = "Just relaxing"

#-----------------------------------------------------------------------------------------------------------------------



########################################################################################################################
# Help and error messages ##############################################################################################
########################################################################################################################

HELP_MESSAGE_EN = str("Commands and their arguments:\n" + COMMAND_PREFIX + "hello\n" + COMMAND_PREFIX + "upvote\n" + COMMAND_PREFIX + "help\n")
HELP_MESSAGE_DE = str("Befehle und ihre Argumente:\n" + COMMAND_PREFIX + "hello\n" + COMMAND_PREFIX + "upvote\n" + COMMAND_PREFIX + ".help\n")
ERROR_MESSAGE_EN = str("The command doesn't exist or you have the wrong arguments.")
ERROR_MESSAGE_DE = str("Der Befehl existiert nicht oder es wurden die falschen Argumente benutzt.")

#-----------------------------------------------------------------------------------------------------------------------



########################################################################################################################
# Checking discord for new messages ####################################################################################
########################################################################################################################

@discord.event
async def on_message(message):

    if message.content.startswith(
            discord.command_prefix):
        await command(message, message.content)

#-----------------------------------------------------------------------------------------------------------------------



########################################################################################################################
# Commands of the bot ##################################################################################################
########################################################################################################################

async def command(msg,text):

    text = str(text)
    text = text[1:]

    #*******************************************************************************************************************
    # Command hallo ****************************************************************************************************
    #*******************************************************************************************************************

    if text.lower().startswith('hello'):
        if LANGUAGE == "EN":
            await discord.send_message(msg.channel, "Hello Master, I'm awaiting your commands. :robot:")
        elif LANGUAGE == "DE":
            await discord.send_message(msg.channel, "Hallo Meister, ich warte auf deine Befehle. :robot:")

    #*******************************************************************************************************************



    #*******************************************************************************************************************
    # Command help *****************************************************************************************************
    #*******************************************************************************************************************

    elif text.lower().startswith('help'):
        if LANGUAGE == "EN":
            await discord.send_message(msg.channel, HELP_MESSAGE_EN)
        elif LANGUAGE == "DE":
            await discord.send_message(msg.channel, HELP_MESSAGE_DE)

    #*******************************************************************************************************************



    #*******************************************************************************************************************
    # Command upvote ***************************************************************************************************
    #*******************************************************************************************************************

    elif text.lower().startswith('upvote'):
        try:
            link = text.split(' ')[1]
            post = link.split('@')[1]

            if LANGUAGE == "EN":
                await discord.send_message(msg.channel, "I'm trying to upvote this post.")
                await discord.send_message(msg.channel, "Getting post information...")
            elif LANGUAGE == "DE":
                await discord.send_message(msg.channel, "Ich versuche diesen Post upzuvoten.")
                await discord.send_message(msg.channel, "Hole Informationen über den Post...")

            #-----------------------------------------------------------------------------------------------------------
            # Upvote the post ------------------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_VOTING == True:
                try:
                    steem.commit.vote(post, STEEM_VOTING_WEIGHT, account=STEEM_USERNAME, )
                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Post upvoted. :white_check_mark:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Post wurde upgevoted. :white_check_mark:")

                except:
                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Error when upvoting the post! :x:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Fehler beim upvoten des Posts! :x:")

            else:
                DO_NOTHING = "Just relaxing"
            #-----------------------------------------------------------------------------------------------------------



            #-----------------------------------------------------------------------------------------------------------
            # Upvote from 2nd account ----------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_VOTING_2ND_ACCOUNT == True:
                try:
                    steem2nd.commit.vote(post, STEEM_VOTING_WEIGHT_2ND, account=STEEM_USERNAME_2ND, )
                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Post upvoted with 2nd account. :white_check_mark:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Post wurde mit 2. Account upgevoted. :white_check_mark:")

                except:
                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "2nd Account: Error when upvoting the post! :x:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "2. Account: Fehler beim upvoten des Posts! :x:")

            else:
                DO_NOTHING = "Just relaxing"
            #-----------------------------------------------------------------------------------------------------------



            #-----------------------------------------------------------------------------------------------------------
            # Comment the upvoted post ---------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_COMMENTING == True:
                try:
                    COMMENT_PERMLINK = "yadubot" + "".join(random.choices(string.digits, k=16))
                    POST_AUTHOR = '@' + post.split('/')[0]
                    
                    
                    if BOT_COMMENT_IS_FILE == True:
                        #---------------------------------------------------------------------------------------------------
                        # Replace the &AUTHOR placeholder in the comment file with the name of the post author -------------
                        #---------------------------------------------------------------------------------------------------
                        with open(BOT_COMMENT_FILE, 'r') as myfile:
                            BOT_COMMENT = myfile.read().replace('\n', '')
                        BODY = BOT_COMMENT.replace("&AUTHOR", POST_AUTHOR)
                        #---------------------------------------------------------------------------------------------------
                    elif BOT_COMMENT_IS_FILE == False:
                        BODY = BOT_COMMENT               
                    

                    steem.commit.post(title='', body=BODY, author=STEEM_USERNAME, permlink=COMMENT_PERMLINK,reply_identifier=post)

                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Post successfully commented. :white_check_mark:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Post erfolgreich kommentiert. :white_check_mark:")

                except:
                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Error commenting the post! :x:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Fehler beim kommentieren des Posts! :x:")

            else:
                DO_NOTHING = "Just relaxing"

            #-----------------------------------------------------------------------------------------------------------



            #-----------------------------------------------------------------------------------------------------------
            # Resteem the upvoted post ---------------------------------------------------------------------------------
            #-----------------------------------------------------------------------------------------------------------
            if BOT_IS_RESTEEMING == True:
                try:
                    steem.commit.resteem(post, account=STEEM_USERNAME)

                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Post successfully resteemed. :white_check_mark:")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Post erfolgreich resteemed. :white_check_mark:")

                except:
                    if LANGUAGE == "EN":
                        await discord.send_message(msg.channel, "Error resteeming the post!")
                    elif LANGUAGE == "DE":
                        await discord.send_message(msg.channel, "Fehler beim resteemen des Posts!")

            else:
                DO_NOTHING = "Just relaxing"

            #-----------------------------------------------------------------------------------------------------------

    #*******************************************************************************************************************



    #*******************************************************************************************************************
    # Error in command *************************************************************************************************
    #*******************************************************************************************************************

        except IndexError:
            if LANGUAGE == "EN":
                index_error = await discord.send_message(msg.channel, ERROR_MESSAGE_EN)
            elif LANGUAGE == "DE":
                index_error = await discord.send_message(msg.channel, ERROR_MESSAGE_DE)
            else:
                index_error = ""

            await asyncio.sleep(10)
            await discord.delete_message(index_error)

            return 0

    else:
        if LANGUAGE == "EN":
            command_error = await discord.send_message(msg.channel, ERROR_MESSAGE_EN)
        elif LANGUAGE == "DE":
            command_error = await discord.send_message(msg.channel, ERROR_MESSAGE_DE)
        else:
            command_error = ""

        await asyncio.sleep(10)
        await discord.delete_message(command_error)

    #*******************************************************************************************************************

#-----------------------------------------------------------------------------------------------------------------------



########################################################################################################################
# Starting the bot and writing some lines to the prompt ################################################################
########################################################################################################################

@discord.event
async def on_ready():
    if LANGUAGE == "EN":
        print("")
        print("")
        print("#############################################################################################################")
        print("")
        print("Bot is running and waiting for your instructions.")
        print("Type " + COMMAND_PREFIX + "hello to test it. Type " + COMMAND_PREFIX + "help to see the available commands.")
        print("")
        print("Link to connect to discord: https://discordapp.com/oauth2/authorize?discord_id=" + discord.user.id + "&scope=bot&permissions=8")
        print("")
        print("#############################################################################################################")
    elif LANGUAGE == "DE":
        print("")
        print("")
        print("#############################################################################################################")
        print("")
        print("Der Bot ist bereit und wartet auf Instruktionen.")
        print("Tippe " + COMMAND_PREFIX + "hello um ihn zu testen. Tippe " + COMMAND_PREFIX + "help um die verfügbaren Kommandos zu sehen.")
        print("")
        print("Link um mit discord zu verbinden: https://discordapp.com/oauth2/authorize?discord_id=" + discord.user.id + "&scope=bot&permissions=8")
        print("")
        print("#############################################################################################################")


discord.run(DISCORD_TOKEN)

#-----------------------------------------------------------------------------------------------------------------------
