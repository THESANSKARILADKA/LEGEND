#stickery alive by @hellboi_atul
# credits @xaditya (telebot) && RAM (JARVIS)

import os
import requests
import time
from PIL import Image
from io import BytesIO
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
from datetime import datetime

ALIVE_PHOTTO = os.environ.get("ALIVE_PHHOTO" , None)

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "This user"

@borg.on(admin_cmd(outgoing=True, pattern="allive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**🅢🅐🅝🅢🅚🅐🅡🅘 🅤🅢🅔🅡🅑🅞🅣 🅘🅢 🅞🅝🅛🅘🅝🅔**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 15.0\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.8.5\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/dark_cobra_support)\n"
        pm_caption += "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/dark_cobra_support_group)\n"
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ sᴀɴsᴋᴀʀɪ ʟᴀᴅᴋᴀ ](https://t.me/Thesanskari_ladka)\n"
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Dark_cobra_support_group)"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PIC,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/2f25e6c3b9fa244bee26f.jpg")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"**🇸 🇦 🇳 🇸 🇰 🇦 🇷 🇮  🇺 🇸 🇪 🇷 🇧 🇴 🇹  🇮 🇸  🇴 🇳 🇱 🇮 🇳 🇪**\n"
                      f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
                      "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 15.0\n"
                      "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.8.5\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/dark_cobra_support)\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/dark_cobra_support_group)\n"
                      "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/hellboi-atul)\n"
                      "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ ᔑᗩᑎᔑᏦᗩᖇᏆ ᏞᗩᗞᏦᗩ ](https://t.me/THESANSKARI_LADKA)\n"
                               
        await alive.delete()
