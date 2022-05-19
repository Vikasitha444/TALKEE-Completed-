#!/usr/bin/python3.9
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.
#with webhook

"""
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic inline bot example. Applies different text transformations.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler

import logging
from uuid import uuid4
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update
from telegram.ext import Updater, InlineQueryHandler, CommandHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
import os
import re




api_key = "5326418386:AAE6mqA63CxvOZtvBz4Ki6CQ6HTZWWjVMeY";
my_chat_id = 378984038




# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')
    update.message.reply_text("Most of the time I'm not replying to private chats. Add me to a group.")


def echo(update,context):


#1) message(Ob) --> message_id

    message_id = update.message.message_id


#2) message(Ob) --> from --> User(Ob)
    user_id = update.message.from_user.id
    is_bot = update.message.from_user.is_bot
    first_name = update.message.from_user.first_name
    last_name = update.message.from_user.last_name
    username = update.message.from_user.username
    language_code = update.message.from_user.language_code
    can_join_groups = update.message.from_user.can_join_groups
    can_read_all_group_messages = update.message.from_user.can_read_all_group_messages
    supports_inline_queries = update.message.from_user.supports_inline_queries


#3) message(Ob) --> sender_chat --> Chat(Ob)
    chat_id = update.message.chat.id
    chat_type = update.message.chat.type
    title = update.message.chat.title
    username = update.message.chat.username
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name

    #Chat(Ob) --> Photo,bio and others
    #To get photos and user sensitive data, we have to use getChat methord
    getChat = context.bot.getChat(chat_id) #Eneble the getChat Methord

    #Chat(Ob) --> photo --> ChatPhoto(Ob)
    if(getChat.photo): #Some users doesn't have a photo
        small_file_id = getChat.photo.small_file_id
        big_file_unique_id = getChat.photo.big_file_unique_id
        big_file_id = getChat.photo.big_file_id
        small_file_unique_id = getChat.photo.small_file_unique_id


    bio = getChat.bio
    has_private_forwards = getChat.has_private_forwards
    description = getChat.description
    invite_link = getChat.invite_link

    #Chat(Ob) --> pinned_message --> Message(Ob)
    if(getChat.pinned_message): #only for supergroups
        message_id_pinned_message = getChat.pinned_message.message_id
        text_pinned_message = getChat.pinned_message.text





    #Chat(Ob) --> permissions --> ChatPermissions(Ob)
    if(getChat.permissions): #This is only working in a group
        can_send_messages = getChat.permissions.can_send_messages
        can_send_media_messages = getChat.permissions.can_send_media_messages
        can_send_polls = getChat.permissions.can_send_polls
        can_add_web_page_previews = getChat.permissions.can_add_web_page_previews
        can_change_info = getChat.permissions.can_change_info
        can_invite_users = getChat.permissions.can_invite_users
        can_pin_messages = getChat.permissions.can_pin_messages


    slow_mode_delay = getChat.slow_mode_delay
    message_auto_delete_time = getChat.message_auto_delete_time
    has_protected_content = getChat.has_protected_content
    sticker_set_name = getChat.sticker_set_name
    can_set_sticker_set = getChat.can_set_sticker_set
    linked_chat_id = getChat.linked_chat_id


    location = getChat.location




    received_text = update.message.text
    if(chat_id != my_chat_id): #Prevent sending a reply for my chat again
        getChat = context.bot.getChat(user_id)

        group_title = context.bot.getChat(chat_id).title
        bio = getChat.bio
        username = getChat.username
        chat_type = getChat.type
        first_name = getChat.first_name
        message_sent_by_user = f"<b>🔔 {first_name} 🔔</b>\n{group_title}\n\n{received_text}\n\n<tg-spoiler>Name:-{first_name}\nUsername:-@{username}\nchat:-{chat_id}d~\nmessage:-{message_id}e~\nuser:-{user_id}k~\n</tg-spoiler>"
        context.bot.sendMessage(my_chat_id,message_sent_by_user,parse_mode='HTML')

    else:
        I_replyed_message_id = update.message.reply_to_message.message_id
        My_message = update.message.text
        users_message = update.message.reply_to_message.text

        start = 'message:-'
        end = 'e~'
        s = users_message
        user_message_id_number = (s[s.find(start)+len(start):s.rfind(end)])

        start = 'chat:-'
        end = 'd~'
        s = users_message
        user_chat_id_number = (s[s.find(start)+len(start):s.rfind(end)])




        print("user_chat_id_number ",user_chat_id_number)
        print("user_message_id_number ",user_message_id_number)
        #print(I_replyed_message_id,My_message,users_chat_id)

        context.bot.sendChatAction(user_chat_id_number,'typing')
        context.bot.copyMessage(user_chat_id_number,my_chat_id, message_id,reply_to_message_id = user_message_id_number)








def getinfo(update,context):
    user_id = update.message.from_user.id

    try:#Checks if the user mentioned a message (reply to a message)
        update.message.reply_to_message.text
    except AttributeError:
        context.bot.sendMessage(my_chat_id,'❌ You have to mention a message')

    I_replyed_message_text = update.message.reply_to_message.text
    start = 'user:-'; end = 'k~'
    s = I_replyed_message_text
    user_id_number = (s[s.find(start)+len(start):s.rfind(end)])

    getChat = context.bot.getChat(user_id_number)

    bio = getChat.bio
    has_private_forwards = getChat.has_private_forwards
    description = getChat.description
    invite_link = getChat.invite_link
    username = getChat.username
    chat_type = getChat.type
    first_name = getChat.first_name

    caption = "<b>First Name</b>: {}\n<b>Username</b>: <b><i>@{}</i></b>\n<b>Type</b>: {}\n<b>Has private forwards</b>: {}\n<b>Description</b>: {}\n<b>Invite link</b>: {}\n<b>Bio</b>: {}\n".\
    format(first_name,username,chat_type,has_private_forwards,description,invite_link,bio)

    user_profile_photo = context.bot.getUserProfilePhotos(user_id_number)

    if (user_profile_photo.total_count != 0): #check if user has a photo
        users_newst_photo =  user_profile_photo.photos[-1][-1].file_id
        context.bot.sendChatAction(my_chat_id,'upload_photo')
        context.bot.sendPhoto(my_chat_id,users_newst_photo,caption,parse_mode='HTML')
    else:
        context.bot.sendChatAction(my_chat_id,'typing')
        context.bot.sendMessage(my_chat_id,caption,parse_mode='HTML')


def groupinfo(update,context):
    I_replyed_message_text = update.message.reply_to_message.text
    I_replyed_message_id = update.message.reply_to_message.message_id

    start = 'chat:-'; end = 'd~'
    s = I_replyed_message_text
    user_chat_id_number = (s[s.find(start)+len(start):s.rfind(end)])

    getChat = context.bot.getChat(user_chat_id_number)


    group_title = getChat.title
    group_id = getChat.id
    group_type = getChat.type
    has_private_forwards = getChat.has_private_forwards
    description = getChat.description
    invite_link = getChat.invite_link

    #Chat(Ob) --> pinned_message --> Message(Ob)
    if(getChat.pinned_message): #only for supergroups
        message_id_pinned_message = getChat.pinned_message.message_id
        text_pinned_message = getChat.pinned_message.text





    #Chat(Ob) --> permissions --> ChatPermissions(Ob)
    if(getChat.permissions): #This is only working in a group
        can_send_messages = getChat.permissions.can_send_messages
        can_send_media_messages = getChat.permissions.can_send_media_messages
        can_send_polls = getChat.permissions.can_send_polls
        can_add_web_page_previews = getChat.permissions.can_add_web_page_previews
        can_change_info = getChat.permissions.can_change_info
        can_invite_users = getChat.permissions.can_invite_users
        can_pin_messages = getChat.permissions.can_pin_messages


    slow_mode_delay = getChat.slow_mode_delay
    message_auto_delete_time = getChat.message_auto_delete_time
    has_protected_content = getChat.has_protected_content
    sticker_set_name = getChat.sticker_set_name
    can_set_sticker_set = getChat.can_set_sticker_set
    linked_chat_id = getChat.linked_chat_id

    caption = "<b>group_title</b>: {}\n<b>group_id</b>: {}\n<b>group_type</b>: {}\n<b>has_private_forwards</b>: {}\n<b>description</b>: {}\n<b>invite_link</b>: {}\n".\
    format(group_title,group_id,group_type,has_private_forwards,description,invite_link)

    context.bot.sendChatAction(my_chat_id,'typing')
    context.bot.sendMessage(my_chat_id,caption,parse_mode='HTML',reply_to_message_id=I_replyed_message_id)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')



def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(api_key)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("getinfo", getinfo))
    dispatcher.add_handler(CommandHandler("groupinfo", groupinfo))
    #dispatcher.add_handler(CommandHandler(Filters.commands, help_command))
    dispatcher.add_handler(MessageHandler(Filters.all, echo))


    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()







if __name__ == '__main__':
    main()