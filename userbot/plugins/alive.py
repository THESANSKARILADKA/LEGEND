import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/2f25e6c3b9fa244bee26f.jpg"
pm_caption = "**𝚂𝙰𝙽𝚂𝙺𝙰𝚁𝙸 𝚄𝚂𝙴𝚁𝙱𝙾𝚃 𝙸𝚂 𝙾𝙽𝙻𝙸𝙽𝙴**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/Dark_cobra_support_group)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [𝐒𝐀𝐍𝐒𝐊𝐀𝐑𝐈 𝐁𝐎𝐓MIT LICENSE](https://github.com/THESANSKARILADKA/SANSKARI-USERBOT/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [sᴀɴsᴋᴀʀɪ ʟᴀᴅᴋᴀ](https://github.com/THESANSKARILADKA)\n"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
