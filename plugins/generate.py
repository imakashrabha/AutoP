# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import traceback
from pyrogram.types import Message
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from config import API_ID, API_HASH
from plugins.database import db

SESSION_STRING_SIZE = 351

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["logout"]))
async def logout(client, message):
    user_data = await db.get_session(message.from_user.id)  
    if user_data is None:
        return 
    await db.set_session(message.from_user.id, session=None)  
    await message.reply("𝖫𝗈𝗀𝗈𝗎𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒")

@Client.on_message(filters.private & ~filters.forwarded & filters.command(["login"]))
async def main(bot: Client, message: Message):
    user_data = await db.get_session(message.from_user.id)
    if user_data is not None:
        await message.reply("𝖸𝗈𝗎𝗋 𝖠𝗋𝖾 𝖠𝗅𝗋𝖾𝖺𝖽𝗒 𝖫𝗈𝗀𝗀𝖾𝖽 𝖨𝗇. 𝖥𝗂𝗋𝗌𝗍 /logout 𝖸𝗈𝗎𝗋 𝖮𝗅𝖽 𝖲𝖾𝗌𝗌𝗂𝗈𝗇. 𝖳𝗁𝖾𝗇 𝖣𝗈 𝖫𝗈𝗀𝗂𝗇.")
        return 
    user_id = int(message.from_user.id)
    phone_number_msg = await bot.ask(chat_id=user_id, text="<b>𝖯𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗇𝖽 𝗒𝗈𝗎𝗋 𝗉𝗁𝗈𝗇𝖾 𝗇𝗎𝗆𝖻𝖾𝗋 𝗐𝗁𝗂𝖼𝗁 𝗂𝗇𝖼𝗅𝗎𝖽𝖾𝗌 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝖼𝗈𝖽𝖾</b>\n𝖤𝗑𝖺𝗆𝗉𝗅𝖾: <code>+13124562345, +9171828181889</code>")
    if phone_number_msg.text=='/cancel':
        return await phone_number_msg.reply('𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝖼𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽')
    phone_number = phone_number_msg.text
    client = Client(":memory:", API_ID, API_HASH)
    await client.connect()
    await phone_number_msg.reply("𝖲𝖾𝗇𝖽𝗂𝗇𝗀 𝖮𝖳𝖯...")
    try:
        code = await client.send_code(phone_number)
        phone_code_msg = await bot.ask(user_id, "𝖯𝗅𝖾𝖺𝗌𝖾 𝖼𝗁𝖾𝖼𝗄 𝖿𝗈𝗋 𝖺𝗇 𝖮𝖳𝖯 𝗂𝗇 𝗈𝖿𝖿𝗂𝖼𝗂𝖺𝗅 𝗍𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝖺𝖼𝖼𝗈𝗎𝗇𝗍. 𝖨𝖿 𝗒𝗈𝗎 𝗀𝗈𝗍 𝗂𝗍, 𝗌𝖾𝗇𝖽 𝖮𝖳𝖯 𝗁𝖾𝗋𝖾 𝖺𝖿𝗍𝖾𝗋 𝗋𝖾𝖺𝖽𝗂𝗇𝗀 𝗍𝗁𝖾 𝖻𝖾𝗅𝗈𝗐 𝖿𝗈𝗋𝗆𝖺𝗍.\n\n𝖨𝖿 𝖮𝖳𝖯 𝗂𝗌 `12345`, 𝗉𝗅𝖾𝖺𝗌𝖾 𝗌𝖾𝗇𝖽 𝗂𝗍 𝖺𝗌 `1 2 3 4 5`.\n\n𝖤𝗇𝗍𝖾𝗋 /cancel 𝗍𝗈 𝖼𝖺𝗇𝖼𝖾𝗅 𝖳𝗁𝖾 𝖯𝗋𝗈𝖼𝖼𝖾𝗌", filters=filters.text, timeout=600)
    except PhoneNumberInvalid:
        await phone_number_msg.reply('`PHONE_NUMBER` 𝗂𝗌 𝗂𝗇𝗏𝖺𝗅𝗂𝖽')
        return
    if phone_code_msg.text=='/cancel':
        return await phone_code_msg.reply('𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝖼𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽 !')
    try:
        phone_code = phone_code_msg.text.replace(" ", "")
        await client.sign_in(phone_number, code.phone_code_hash, phone_code)
    except PhoneCodeInvalid:
        await phone_code_msg.reply('𝖮𝖳𝖯 𝗂𝗌 𝗂𝗇𝗏𝖺𝗅𝗂𝖽.')
        return
    except PhoneCodeExpired:
        await phone_code_msg.reply('𝖮𝖳𝖯 𝗂𝗌 𝖾𝗑𝗉𝗂𝗋𝖾𝖽.')
        return
    except SessionPasswordNeeded:
        two_step_msg = await bot.ask(user_id, '𝖸𝗈𝗎𝗋 𝖺𝖼𝖼𝗈𝗎𝗇𝗍 𝗁𝖺𝗌 𝖾𝗇𝖺𝖻𝗅𝖾𝖽 𝗍𝗐𝗈-𝗌𝗍𝖾𝗉 𝗏𝖾𝗋𝗂𝖿𝗂𝖼𝖺𝗍𝗂𝗈𝗇. 𝖯𝗅𝖾𝖺𝗌𝖾 𝗉𝗋𝗈𝗏𝗂𝖽𝖾 𝗍𝗁𝖾 𝗉𝖺𝗌𝗌𝗐𝗈𝗋𝖽.\n\n𝖤𝗇𝗍𝖾𝗋 /cancel 𝗍𝗈 𝖼𝖺𝗇𝖼𝖾𝗅 𝖳𝗁𝖾 𝖯𝗋𝗈𝖼𝖼𝖾𝗌', filters=filters.text, timeout=300)
        if two_step_msg.text=='/cancel':
            return await two_step_msg.reply('𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝖼𝖺𝗇𝖼𝖾𝗅𝗅𝖾𝖽')
        try:
            password = two_step_msg.text
            await client.check_password(password=password)
        except PasswordHashInvalid:
            await two_step_msg.reply('𝗂𝗇𝗏𝖺𝗅𝗂𝖽 𝗉𝖺𝗌𝗌𝗐𝗈𝗋𝖽')
            return
    string_session = await client.export_session_string()
    await client.disconnect()
    if len(string_session) < SESSION_STRING_SIZE:
        return await message.reply('𝗂𝗇𝗏𝖺𝗅𝗂𝖽 𝗌𝖾𝗌𝗌𝗂𝗈𝗇 𝗌𝗋𝗂𝗇𝗀')
    try:
        user_data = await db.get_session(message.from_user.id)
        if user_data is None:
            uclient = Client(":memory:", session_string=string_session, api_id=API_ID, api_hash=API_HASH)
            await uclient.connect()
            await db.set_session(message.from_user.id, session=string_session)
    except Exception as e:
        return await message.reply_text(f"𝖤𝖱𝖱𝖮𝖱 𝖨𝖭 𝖫𝖮𝖦𝖨𝖭 `{e}`")
    await bot.send_message(message.from_user.id, "𝖠𝖼𝖼𝗈𝗎𝗇𝗍 𝖫𝗈𝗀𝗂𝗇 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒.\n\n𝖨𝖿 𝖸𝗈𝗎 𝖦𝖾𝗍 𝖠𝗇𝗒 𝖤𝗋𝗋𝗈𝗋 𝖱𝖾𝗅𝖺𝗍𝖾𝖽 𝖳𝗈 𝖠𝖴𝖳𝖧 𝖪𝖤𝖸 𝖳𝗁𝖾𝗇 /logout 𝖿𝗂𝗋𝗌𝗍 𝖺𝗇𝖽 /login 𝖺𝗀𝖺𝗂𝗇")
