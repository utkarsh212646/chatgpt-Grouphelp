from telegram.ext import Updater, CommandHandler

# Define the command callback function
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hi! How can I help you today?")

# Create an Updater object and attach a CommandHandler to it
updater = Updater(token='YOUR_TOKEN', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('hi', start))

# Start the bot
updater.start_polling()
