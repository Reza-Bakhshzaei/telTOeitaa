from rubika import Bot

auth = "u0GOux0964339f923160b7fd0addb826"



def upload_file(chat_id, path):
    bot = Bot("boot", auth)
    bot.sendVideo( chat_id, path)
    return True