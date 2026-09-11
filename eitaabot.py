from rubika import Bot

auth = "hleftowpbgadchydlxwixmqhthvoesto"



def upload_file(chat_id, path):
    bot = Bot("boot", auth)
    bot.sendVideo( chat_id, path)
    return True