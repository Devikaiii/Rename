from pyrogram import Client, filters
from helper.database import find, delthumb, addthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client,message):
    thumb = find(int(message.chat.id))[0]
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        text = "`No Saved Thumbnail Found.`"
        await message.reply_text(text=text, reply_to_message_id=message.id) 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client,message):
    delthumb(int(message.chat.id))
    text = "**Previous Thumbnail Deleted Successfully ✅**"
    await message.reply_text(text=text, reply_to_message_id=message.id)
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id , file_id)
    text = "**ᴄᴜꜱᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ꜱᴀᴠᴇᴅ. ✅️**\n\n__ᴛʜɪꜱ ᴛʜᴜᴍʙɴᴀɪʟ ᴡɪʟʟ ʙᴇ ᴩᴇʀᴍᴇɴᴀɴᴛ ꜰᴏʀ ᴀʟʟ ꜰᴜᴛᴜʀᴇ ᴜᴩʟᴏᴀᴅꜱ.__"
    await message.reply_text(text=text, reply_to_message_id=message.id,)
	
