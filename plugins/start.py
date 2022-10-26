"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

from os import environ
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply, CallbackQuery
from pyrogram.errors import FloodWait
import humanize
from helper.txt import mr
from helper.database import insert 
from helper.utils import not_subscribed 

FLOOD = int(environ.get("FLOOD", "10"))
START_PIC = environ.get("START_PIC", "")

@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    buttons = [[ InlineKeyboardButton(text="📢 Jᴏɪɴ Mʏ Uᴘᴅᴀᴛᴇ Cʜᴀɴɴᴇʟ 📢", url=client.invitelink) ]]
    text = "**Sᴏʀʀʏ Dᴜᴅᴇ Yᴏᴜʀ Nᴏᴛ Jᴏɪɴᴅ Mʏ Cʜᴀɴɴᴇʟ 😔. Pʟᴇᴀsᴇ Jᴏɪɴ Mʏ Cʜᴀɴɴᴇʟ Tᴏ Usᴇ Tʜɪs Bᴏᴛ 🙏 **"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    insert(int(message.chat.id))
    await message.reply_photo(
       photo=START_PIC,
       caption=f"""👋 Hᴀɪ {message.from_user.mention} \nIᴍ A Sɪᴍᴘʟᴇ Fɪʟᴇ Rᴇɴᴀᴍᴇ + Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ Cᴏᴠᴇʀᴛᴇʀ Bᴏᴛ Wɪᴛʜ Pᴇʀᴍᴀɴᴇɴᴛ Tʜᴜᴍʙɴᴀɪʟ & Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ! """,
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton("👼 Dᴇᴠs 👼", callback_data='dev')
           ],[
           InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs', url='https://t.me/CS_TeamTG'),
           InlineKeyboardButton('🍂 Sᴜᴘᴘᴏʀᴛ', url='https://t.me/CS_TeamTG')
           ],[
           InlineKeyboardButton('🍃 Aʙᴏᴜᴛ', callback_data='about'),
           InlineKeyboardButton('ℹ️ Hᴇʟᴘ', callback_data='help')
           ]]
          )
       )
    return


@Client.on_message(filters.private & (filters.document | filters.audio | filters.video))
async def rename_start(client, message):
    file = getattr(message, message.media.value)
    filename = file.file_name
    filesize = humanize.naturalsize(file.file_size) 
    fileid = file.file_id
    try:
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 Sᴛᴀʀᴛ Rᴇɴᴀᴍᴇ 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.x)
        text = f"""**__What do you want me to do with this file.?__**\n\n**File Name** :- `{filename}`\n\n**File Size** :- `{filesize}`"""
        buttons = [[ InlineKeyboardButton("📝 Sᴛᴀʀᴛ Rᴇɴᴀᴍᴇ 📝", callback_data="rename") ],
                   [ InlineKeyboardButton("✖️ Cᴀɴᴄᴇʟ ✖️", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    buttons  = [
            [
                InlineKeyboardButton('🛠️ ʜᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('🛡️ ᴀʙᴏᴜᴛ', callback_data='about')
            ],
            [
                InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴏʟᴏᴘᴇʀs', url='https://t.me/ddrabit')
            ]
            ]
    text = f"👋🏻 Hᴇʟʟᴏ {query.from_user.mention}\n\nIᴍ ᴀɴ ᴀwsᴏᴍᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴇɴᴀɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ\n\nPʀᴇss ʜᴇʟᴘ ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ...\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: [LᴀL](https://t.me/ddrabit)"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋🏻 Hᴇʟʟᴏ {query.from_user.mention}\n\nIᴍ ᴀɴ ᴀwsᴏᴍᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴇɴᴀɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ\n\nPʀᴇss ʜᴇʟᴘ ᴛᴏ sᴇᴇ ᴀʟʟ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ᴀɴᴅ ʜᴏᴡ ᴛʜᴇʏ ᴡᴏʀᴋ...\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: [LᴀL](https://t.me/ddrabit)""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("", callback_data='dev')                
                ],[
                InlineKeyboardButton('🛠️ ʜᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('🛡️ ᴀʙᴏᴜᴛ', callback_data='about')
                ],[
                InlineKeyboardButton('', callback_data='about'),
                InlineKeyboardButton('👨‍💻 ᴅᴇᴠᴏʟᴏᴘᴇʀs', url='https://t.me/ddrabit')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=mr.HELP_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("😬 Sᴏᴜʀᴄᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("💥 CS - Tᴇᴀᴍ Cʜᴀɴɴᴇʟ 💥", url='https://t.me/CS_TeamTG')
               ],[
               InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close"),
               InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "arun")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("😬 Sᴏᴜʀᴄᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("💥 CS - Tᴇᴀᴍ Cʜᴀɴɴᴇʟ 💥", url="https://t.me/CS_TeamTG")
               ],[
               InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close"),
               InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "dev":
        await query.message.edit_text(
            text=mr.DEV_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("😬 Sᴏᴜʀᴄᴇ", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("💥 CS - Tᴇᴀᴍ Cʜᴀɴɴᴇʟ 💥", url="https://t.me/CS_TeamTG")
               ],[
               InlineKeyboardButton("🔒 Cʟᴏsᴇ", callback_data = "close"),
               InlineKeyboardButton("◀️ Bᴀᴄᴋ", callback_data = "start")
               ]]
            )
        )
    elif data == "close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            await query.message.delete()





