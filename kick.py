# Define the kick function to handle the /kick command
def kick(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="User kicked.")
