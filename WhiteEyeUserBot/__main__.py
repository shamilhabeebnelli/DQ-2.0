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

import logging
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from var import Var
from WhiteEyeUserBot import bot
from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.utils import load_module, start_assistant

sed = logging.getLogger("WhiteEye")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()


import glob

path = "WhiteEyeUserBot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

if Config.ENABLE_ASSISTANTBOT == "ENABLE":
    path = "WhiteEyeUserBot/modules/assistant/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            start_assistant(shortname.replace(".py", ""))

    sed.info(
        """\n██╗    ██╗██╗  ██╗██╗████████╗███████╗███████╗██╗   ██╗███████╗    
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██╔════╝╚██╗ ██╔╝██╔════╝    
██║ █╗ ██║███████║██║   ██║   █████╗  █████╗   ╚████╔╝ █████╗      
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ██╔══╝    ╚██╔╝  ██╔══╝      
╚███╔███╔╝██║  ██║██║   ██║   ███████╗███████╗   ██║   ███████╗    
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝    """
    )
else:
    sed.info("WhiteEye Has Been Installed Sucessfully !")
    sed.info("You Can Visit @WhiteEyeOT For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
