from rubika import Bot
bot = Bot("boot", "hleftowpbgadchydlxwixmqhthvoesto")

def upload_file(chat_id, path):
    bot.sendVideo( chat_id, path)
    return True