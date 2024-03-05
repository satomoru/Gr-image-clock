import asyncio
import datetime
from telethon import TelegramClient, events
from telethon.tl import functions
from PIL import Image, ImageDraw, ImageFont

api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

client = TelegramClient('session_name', api_id, api_hash)

client.start()

async def change_group_profile_image():
    while True:
        now = datetime.datetime.now()

        image = Image.new('RGB', (500, 500), color='white')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('path_to_font_file', size=50)  
        text = now.strftime('%H:%M:%S')
        text_width, text_height = draw.textsize(text, font=font)
        text_position = ((500 - text_width) // 2, (500 - text_height) // 2)
        draw.text(text_position, text, fill='black', font=font)
       
        image_path = 'new_profile_image.jpg'
        image.save(image_path, 'JPEG')
        
        group = await client.get_entity('YOUR_GROUP_USERNAME')
        
        result = await client.upload_file(image_path)
        await client(functions.photos.UploadProfilePhotoRequest(file=result))
        
        await asyncio.sleep(1)

client.loop.run_until_complete(change_group_profile_image())

client.run_until_disconnected()
