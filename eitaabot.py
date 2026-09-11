from rubika import Bot

def upload_file(chat_id, path):
    bot = Bot("boot", "hleftowpbgadchydlxwixmqhthvoesto")
    bot.sendVideo( chat_id, path)
    return True