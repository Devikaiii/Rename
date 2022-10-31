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
    buttons = [[ InlineKeyboardButton(text="📢 Join Channel", url=client.invitelink) ]]
    text = "**Join our Updates Chanel To Use This Bot.**"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
           
@Client.on_message(filters.private & filters.command(["hence"]))
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
        text = f"""**File Name**: `{filename}`\n\n**File Size**: `{filesize}`"""
        buttons = [[ InlineKeyboardButton("✍️ 𝗥𝗘𝗡𝗔𝗠𝗘", callback_data="rename") ],
                   [ InlineKeyboardButton("❌ 𝗖𝗔𝗡𝗖𝗘𝗟 ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
        await sleep(FLOOD)
    except FloodWait as e:
        await sleep(e.x)
        text = f"""**File Name**: `{filename}`\n\n**File Size**: `{filesize}`"""
        buttons = [[ InlineKeyboardButton("✍️ 𝗥𝗘𝗡𝗔𝗠𝗘", callback_data="rename") ],
                   [ InlineKeyboardButton("❌ 𝗖𝗔𝗡𝗖𝗘𝗟 ❌", callback_data="cancel") ]]
        await message.reply_text(text=text, reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        pass

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton('🛠️ ʜᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('🛡️ ᴀʙᴏᴜᴛ', callback_data='about')
            ],
            [
                InlineKeyboardButton('🧞‍♂️ ᴅᴇᴠᴏʟᴏᴘᴇʀ', url='https://t.me/ddrabit/19')
            ]
            ]
    text = f"👋🏻 Hᴇʟʟᴏ {message.from_user.mention}\n\nIᴍ ᴀɴ ᴀwsᴏᴍᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴇɴᴀɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ\n\nPʀᴇss ʜᴇʟᴘ ᴛᴏ sᴇᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs...\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: [LᴀL](https://t.me/ddrabit)"
    await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))

@Client.on_callback_query()
async def cb_handler(client, query: CallbackQuery):
    data = query.data 
    if data == "start":
        await query.message.edit_text(
            text=f"""👋🏻 Hᴇʟʟᴏ {query.from_user.mention}\n\nIᴍ ᴀɴ ᴀwsᴏᴍᴇ ʀᴇɴᴀᴍᴇ ʙᴏᴛ ᴡɪᴛʜ ᴘᴇʀᴍᴇɴᴀɴᴛ ᴛʜᴜᴍʙɴᴀɪʟ sᴜᴘᴘᴏʀᴛ\n\nPʀᴇss ʜᴇʟᴘ ᴛᴏ sᴇᴇ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs...\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: [LᴀL](https://t.me/ddrabit)""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton('🛠️ ʜᴇʟᴘ', callback_data='help'),
                InlineKeyboardButton('🛡️ ᴀʙᴏᴜᴛ', callback_data='about')
                ],[
                InlineKeyboardButton('🧞‍♂️ ᴅᴇᴠᴏʟᴏᴘᴇʀ', url='https://t.me/ddrabit/19')
                ]]
                )
            )
        return
    elif data == "help":
        await query.message.edit_text(
            text=f"Hey {query.from_user.mention}\n\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ʜᴇʟᴘ ᴍᴇɴᴜ.\n\nᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴꜱ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴇ ᴜsᴀɢᴇs ᴏꜰ sᴘᴇᴄꜰɪᴄ ᴍᴏᴅᴜʟᴇs..",
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("ʀᴇɴᴀᴍᴇ", callback_data = "rname"),
               InlineKeyboardButton("ᴛʜᴜᴍʙɴᴀɪʟ", callback_data = 'thembnail'),
               InlineKeyboardButton("ᴄᴀᴘᴛɪᴏɴ", callback_data = "cuscap")
               ],[
               InlineKeyboardButton("« Back", callback_data = "start")
               ]]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=mr.ABOUT_TXT.format(client.mention),
            disable_web_page_preview = True,
            reply_markup=InlineKeyboardMarkup( [[
               #⚠️ don't change source code & source link ⚠️ #
               InlineKeyboardButton("", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("", url="https://t.me/CS_TeamTG")
               ],[
               InlineKeyboardButton("", callback_data = "close"),
               InlineKeyboardButton("« Back", callback_data = "start")
               ]]
            )
        )
    elif data == "rname":
        await query.message.edit_text(
            text=mr.RNAME_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("", url="https://t.me/CS_TeamTG")
               ],[
               InlineKeyboardButton("", callback_data = "close"),
               InlineKeyboardButton("« Back", callback_data = "help")
               ]]
            )
        )
    elif data == "thembnail":
        await query.message.edit_text(
            text=mr.THUMB_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("", url="https://t.me/CS_TeamTG")
               ],[
               InlineKeyboardButton("", callback_data = "close"),
               InlineKeyboardButton("« Back", callback_data = "help")
               ]]
            )
        )
    elif data == "cuscap":
        await query.message.edit_text(
            text=mr.CUS_TXT,
            reply_markup=InlineKeyboardMarkup( [[
               InlineKeyboardButton("", url="https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT")
               ],[
               InlineKeyboardButton("", url="https://t.me/CS_TeamTG")
               ],[
               InlineKeyboardButton("", callback_data = "close"),
               InlineKeyboardButton("« Back", callback_data = "help")
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





