from var.token import Token_Eitaa
from eitaa import Eitaa

async def upload_file(chat_id, caption, path):
    try:
        client = Eitaa(Token_Eitaa)
        caption = caption if caption else "no caption"
        client.send_file(chat_id, caption, path)
        return True
    except Exception as e:
        return str(e)