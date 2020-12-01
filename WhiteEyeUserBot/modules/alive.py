#    WhiteEye - UserBot
#    Copyright (C) 2020 WhiteEye

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
# you may not use this file except in compliance with the License.

"""Check if WhiteEyeUserBot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from uniborg.util import WhiteEye_on_cmd, sudo_cmd

from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP, Lastupdate
from WhiteEyeUserBot.Configs import Config


# Functions
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


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "👑 WhiteEye IS: WORKING 👑\n\n"
pm_caption += "✯ **SYSTEMS STATS**\n"
pm_caption += "✯ **Telethon Version:** `1.15.0` \n"
pm_caption += "✯ **Python:** `3.7.4` \n"
pm_caption += f"✯ **Uptime** : `{uptime}` \n"
pm_caption += "✯ **Database Status:**  `Functional`\n"
pm_caption += "✯ **Current Branch** : `master`\n"
pm_caption += f"✯ **My Boss** : {DEFAULTUSER} \n"
pm_caption += "✯ **Heroku Database** : `AWS - Working Properly`\n\n"
pm_caption += "✯**[Join Our Channel]**(https://t.me/WhiteEyeOT)\n"
pm_caption += "✯ **License** : [GNU General Public License v3.0](https://github.com/whiteeye-org/WhiteEyeUserBot/blob/main/LICENSE)\n"
pm_caption += "✯ **Copyright** : By [WhiteEyeUserBotOwner](https://t.me/mrdayamzaidi)\n"
pm_caption += (
    "[🇮🇳 Deploy WhiteEyeUserBot 🇮🇳](https://whiteeye-org.github.io/WhiteEyeUserBot/)\n"
)


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"online"))
@WhiteEye.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def WhiteEye(alive):
    await alive.get_chat()
    """ For .online command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.online`\
\n**Usage :** Check if UserBot is Alive"
    }
)
