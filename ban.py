# Define the ban function to handle the /ban command
def ban(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="User Sucessfully Banned.")
