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
from telethon.tl.types import InputMessagesFilterDocument

from var import Var
from WhiteEyeUserBot import bot, client2, client3
from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.utils import load_module, load_module_dclient, start_assistant

sed = logging.getLogger("WhiteEye")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


async def lol_s(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


def multiple_client():
    if client2:
        sed.info("Starting Client 2")
        try:
            sedbruh = None
            client2.start()
            client2.loop.run_until_complete(lol_s(client2))
        except:
            sedbruh = True
            sed.info("Client 2 Failed To Load. Check Your String.")
    if client3:
        sed.info("Starting Client 3")
        try:
            lmaobruh = None
            cleint3.start
            client3.loop.run_until_complete(lol_s(client3))
        except:
            lmaobruh = True
            sed.info("Client 3 Failed To Load.")
    if not client2:
        sedbruh = True
    if not client3:
        lmaobruh = True
    return sedbruh, lmaobruh


async def get_other_plugins(Config, client_s, sed):
    try:
        a_plugins = await client_s.get_messages(
            entity=Config.LOAD_OTHER_PLUGINS_CHNNL,
            filter=InputMessagesFilterDocument,
            limit=None,
            search=".py",
        )
    except:
        sed.info("Failed To Other Modules :(")
        return
    sed.info(f"Downloading. {int(a_plugins.total)} Plugins !")
    for keky in a_plugins:
        await client_s.download_media(keky.media, "WhiteEyeUserBot/modules/")
    sed.info("Extra Plugins Downloaded.")


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        failed2, failed3 = multiple_client()
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
    else:
        bot.start()
        failed2, failed3 = multiple_client()

if Config.LOAD_OTHER_PLUGINS:
    bot.loop.run_until_complete(get_other_plugins(Config, bot, sed))

import glob

path = "WhiteEyeUserBot/modules/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            load_module(shortname.replace(".py", ""))
        except Exception as e:
            sed.info("------------------------")
            sed.info(
                "Failed To Load : "
                + str(shortname.replace(".py", ""))
                + f" Error : {str(e)}"
            )
            sed.info("------------------------")
        if failed2 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client2)
            except:
                pass
        if failed3 is None:
            try:
                load_module_dclient(shortname.replace(".py", ""), client3)
            except:
                pass

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
    sed.info("You Can Visit @WhiteEyeDevs For Any Support Or Doubts")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
