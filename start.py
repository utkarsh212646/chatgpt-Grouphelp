from telegram.ext import Updater, CommandHandler

# Define the command callback function
def start(update, context):
    user = update.message.from_user
    name = user.first_name
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hi {name}! Welcome to my bot I Am A Smart Group Management Bot. Here are some things you can do:\n\n/stats - Get statistics about the group\n/status - Get the current status of the bot\n/ban @username - Ban a user from the group\n/kick @username - Kick a user from the group")

# Create an Updater object and attach a CommandHandler to it
updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))

# Start the bot
updater.start_polling()
