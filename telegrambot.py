from pyrogram import Client, filters
from eitaabot import upload_file
import os

api_id = 14381680
api_hash = "e062fd165636c6a327fa0be3b8ec3276"
bot_token="8853175264:AAHdgnySYvv0SURpwZ3T5dUMz7G8y7aq_4w"
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message()
async def answer(client, message):
    print(message)
    if message.document or message.video:
        name = message.document.file_name if message.document else message.video.file_name
        # id = message.document.file_id if message.document else message.video.file_id
        await message.replay("Start Download......")
        await message.download(name)
        await message.replay("End Download!!!!!!")
        await message.replay("Start Upload.......")
        res = await upload_file("@Reza_B_Z", None, name)
        if res:
            await message.replay("End Upload!!!!!!")
        else:
            await message.reply(res)





app.run()
    
