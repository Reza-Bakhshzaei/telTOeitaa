from rubika import Bot

auth = "u0GOux0964339f923160b7fd0addb826"



async def upload_file(chat_id, path):
    try:
        bot = await Bot("boot", auth)
        await bot.sendVideo( chat_id, path)
        return True
    except Exception as e:
        return str(e)