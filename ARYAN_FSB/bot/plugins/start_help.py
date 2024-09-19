# https://github.com/aryansharma-exe

from ARYAN_FSB.bot import StreamBot
from ARYAN_FSB.vars import Var
import logging
logger = logging.getLogger(__name__)
from ARYAN_FSB.bot.plugins.stream import MY_PASS
from ARYAN_FSB.utils.human_readable import humanbytes
from ARYAN_FSB.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from ARYAN_FSB.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                      
@StreamBot.on_message(filters.command('start') & filters.private)
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{m.from_user.first_name}](tg://user?id={m.from_user.id}) Started !!"
        )
    usr_cmd = m.text.split("_")[-1]
    if usr_cmd == "/start":
        await m.reply_photo(
            photo="https://telegra.ph/file/408cb83e4758dc21af386.jpg",
            caption="**ʜᴇʟʟᴏ...⚡\n\nɪᴀᴍ ᴀ sɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛᴏ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ.**\n\n**ᴜsᴇ /help ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛsɪʟs\n\nsᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴛᴏ sᴇᴇ ᴍʏ ᴘᴏᴡᴇʀᴢ...**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs 📢", url="https://t.me/raven_codes"), InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ 🛠️", url="https://t.me/ravencodes_support")],
                    [InlineKeyboardButton("🥷 ᴏᴡɴᴇʀ 🥷", url="https://t.me/im_brainobot"), InlineKeyboardButton("🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🧑‍💻", url="https://t.me/im_brainobot")],
                    [InlineKeyboardButton("🌐 ɢɪᴛʜᴜʙ 🌐", url="https://github.com/aryansharma-exe")]
                ]
            ),
            
        )
    else:

        get_msg = await b.get_messages(chat_id=Var.BIN_CHANNEL, ids=int(usr_cmd))

        file_size = None
        if get_msg.video:
            file_size = f"{humanbytes(get_msg.video.file_size)}"
        elif get_msg.document:
            file_size = f"{humanbytes(get_msg.document.file_size)}"
        elif get_msg.audio:
            file_size = f"{humanbytes(get_msg.audio.file_size)}"

        file_name = None
        if get_msg.video:
            file_name = f"{get_msg.video.file_name}"
        elif get_msg.document:
            file_name = f"{get_msg.document.file_name}"
        elif get_msg.audio:
            file_name = f"{get_msg.audio.file_name}"

        stream_link = "https://{}/{}".format(Var.FQDN, get_msg.id) if Var.ON_HEROKU or Var.NO_PORT else \
            "http://{}:{}/{}".format(Var.FQDN,
                                     Var.PORT,
                                     get_msg.id)

        msg_text = "**ᴛᴏᴜʀ ʟɪɴᴋ ɪs ɢᴇɴᴇʀᴀᴛᴇᴅ...⚡\n\n📧 ғɪʟᴇ ɴᴀᴍᴇ :-\n{}\n {}\n\n💌 ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ :- {}\n\n♻️ ᴛʜɪs ʟɪɴᴋ ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ ᴀɴᴅ ᴡᴏɴ'ᴛ ɢᴇᴛ ᴇxᴘɪʀᴇᴅ ♻️\n\n<b>☣️ ᴘᴏᴡᴇʀᴇᴅ ʙʏ :- @Filmy_Men</b>**"
        await m.reply_text(            
            text=msg_text.format(file_name, file_size, stream_link),
            
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✨ ᴅᴏᴡɴʟᴏᴀᴅ ɴᴏᴡ ✨", url=stream_link2)]])
        )


@StreamBot.on_message(filters.command('helper') & filters.private)
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
              
    await message.reply_photo(
            photo="https://telegra.ph/file/408cb83e4758dc21af386.jpg",
            caption="**┣⪼ sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴛʜᴇɴ ɪ ᴡɪʟʟ ʏᴏᴜ ᴀ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋ  ᴏғ ɪᴛ.\n\n┣⪼ ᴛʜɪs ʟɪɴᴋ ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴏʀ ᴛᴏ sᴛʀᴇᴀᴍ ᴜsɪɴɢ ᴇxᴛᴇʀɴᴀʟ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀs ᴛʜʀᴏᴜɢʜ ᴍʏ sᴇʀᴠᴇʀs.\n\n┣⪼ ғᴏʀ sᴛʀᴇᴀᴍɪɴɢ ᴊᴜsᴛ ᴄᴏᴘʏ ᴛʜᴇ ʟɪɴᴋ ᴀɴᴅ ᴘᴀsᴛᴇ ɪᴛ ɪɴ ʏᴏᴜʀ ᴠɪᴅᴇᴏ ᴘʟᴀʏᴇʀ ᴛᴏ sᴛᴀʀᴛ sᴛʀᴇᴀᴍɪɴɢ ᴏᴠᴇʀ ᴛʜᴇ ᴡᴇʙ.\n\n┣⪼ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ :- /helper\n\n\nᴅᴏɴ'ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴄʜᴇᴄᴋᴏᴜᴛ ʀᴇᴘᴏ ᴏɴ ɢɪᴛʜᴜʙ ᴀɴᴅ ɢɪᴠᴇ ᴀ ꜱᴛᴀʀ ⭐**", 
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                   [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs 📢", url="https://t.me/raven_codes"), InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ 🛠️", url="https://t.me/ravencodes_support")],
                    [InlineKeyboardButton("🥷 ᴏᴡɴᴇʀ 🥷", url="https://t.me/im_brainobot"), InlineKeyboardButton("🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🧑‍💻", url="https://t.me/im_brainobot")],
                    [InlineKeyboardButton("🌐 ɢɪᴛʜᴜʙ 🌐", url="https://github.com/aryansharma-exe")]

                ]
            ),
            
        )

@StreamBot.on_message(filters.command('aryan') & filters.private)
async def about_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started !!"
        )
    await message.reply_photo(
            photo="https://telegra.ph/file/62e1af11def24c6cf54a7.jpg",
            caption="""<b>sᴏᴍᴇ ʜɪᴅᴅᴇɴ ᴅᴇᴛᴀɪʟs😜</b>

<b>╭━━━━〔ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ〕</b>
┃
┣⪼<b>ɴᴀᴍᴇ : <a href='https://telegram.me/im_brainobot'>R a v e n  C o d e s</a></b>
┣⪼<b>ꜱᴇʀᴠᴇʀ : ᴋᴏʏᴇʙ</b>
┣⪼<b>ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ</b>
┣⪼<b>ɢɪᴛʜᴜʙ : <a href='https://github.com/aryansharma-exe'>ᴀʀʏᴀɴꜱʜᴀʀᴍᴀ-ᴇxᴇ </a></b>
┃
<b>╰━━━━〔ᴘʟᴇᴀꜱᴇ sᴜᴘᴘᴏʀᴛ〕</b>""",
  
        
        reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs 📢", url="https://t.me/raven_codes"), InlineKeyboardButton("🛠️ sᴜᴘᴘᴏʀᴛ 🛠️", url="https://t.me/ravencodes_support")],
                    [InlineKeyboardButton("🥷 ᴏᴡɴᴇʀ 🥷", url="https://t.me/im_brainobot"), InlineKeyboardButton("🧑‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ 🧑‍💻", url="https://t.me/im_brainobot")],
                    [InlineKeyboardButton("🌐 ɢɪᴛʜᴜʙ 🌐", url="https://github.com/aryansharma-exe")]
                ]
            ),
            
        )
