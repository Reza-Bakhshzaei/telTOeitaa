from pyrogram import Client, filters
from crawle.crawler import get_results
from crawle.videoDownloader import download_video_from_link
import os

api_id = 14381680
api_hash = "e062fd165636c6a327fa0be3b8ec3276"
bot_token="8853175264:AAHdgnySYvv0SURpwZ3T5dUMz7G8y7aq_4w"
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message()
async def answer(client, message):
    print(message)



app.run()
    
