import os
import re
import urllib
import json
from math import ceil
from re import findall
import requests
from youtube_search import YoutubeSearch
from search_engine_parser import GoogleSearch
from WhiteEyeUserBot.functions import _ytdl, fetch_json, _deezer_dl, all_pro_s
from urllib.parse import quote
import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import VideosSearch
from WhiteEyeUserBot import ALIVE_NAME, CMD_HELP, CMD_LIST, client2 as client1, client3 as client2, bot as client3
from WhiteEyeUserBot.modules import inlinestats
from pornhub_api import PornhubApi
from telethon.tl.types import BotInlineResult, InputBotInlineMessageMediaAuto, DocumentAttributeImageSize, InputWebDocument, InputBotInlineResult
from telethon.tl.functions.messages import SetInlineBotResultsRequest
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
    WARN_PIC = "https://telegra.ph/file/63d2f8bcdae4da2ec5e7e.jpg"
else:
    WARN_PIC = PMPERMIT_PIC
LOG_CHAT = Config.PRIVATE_GROUP_ID
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "WhiteEye"


@tgbot.on(events.InlineQuery)
async def inline_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    builder = event.builder
    result = None
    query = event.text
    if event.query.user_id in o and query.startswith("WhiteEye"):
        rev_text = query[::-1]
        buttons = paginate_help(0, CMD_HELP, "helpme")
        result = builder.article(
            "© WhiteEyeUserBot Help",
            text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
            buttons=buttons,
            link_preview=False,
        )
        await event.answer([result])
    elif event.query.user_id in o and query == "stats":
        result = builder.article(
            title="Stats",
            text=f"**Showing Stats For {DEFAULTUSER}'s WhiteEyeUserBot** \nNote --> Only Owner Can Check This \n(C) @WhiteEyeDevs",
            buttons=[
                [custom.Button.inline("Show Stats ?", data="terminator")],
                [Button.url("Repo 🇮🇳", "https://github.com/WhiteEye-Org/WhiteEyeUserBot")],
                [Button.url("Join Channel ❤️", "t.me/WhiteEyeDevs")],
            ],
        )
        await event.answer([result])
    elif event.query.user_id in o and query.startswith("**Hello"):
        result = builder.photo(
            file=WARN_PIC,
            text=query,
            buttons=[
                    [
                        custom.Button.inline("❌ Spamming", data="wannaspam"),
                        custom.Button.inline("📝 Chatting", data="casualbitching"),
                    ],
                    [
                        custom.Button.inline("❓ Doubt", data="askme"),
                        custom.Button.inline("🛑 Others", data="others"),
                    ],
                ],
            )
        await event.answer([result]
    
@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(current_page_number + 1, CMD_HELP, "helpme")
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_popp_up_alert = "Please get your own WhiteEyeUserBot, and don't use mine!"
        await event.answer(reply_popp_up_alert, cache_time=0, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
async def on_plug_in_callback_query_handler(event):
    if event.query.user_id == bot.uid:
        await event.edit(
            "Menu Closed!!",
        )
    else:
        reply_pop_up_alert = "Please get your own WhiteEyeuserbot from @WhiteEyeDevs "
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    )
)
async def on_plug_in_callback_query_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:  # pylint:disable=E0602
        current_page_number = int(event.data_match.group(1).decode("UTF-8"))
        buttons = paginate_help(
            current_page_number - 1, CMD_HELP, "helpme"  # pylint:disable=E0602
        )
        # https://t.me/TelethonChat/115200
        await event.edit(buttons=buttons)
    else:
        reply_pop_up_alert = "Please get your own WhiteEyeUserBot, and don't use mine!"
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

@tgbot.on(
    events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    )
)
async def on_plug_in_callback_query_handler(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if not event.query.user_id in o:
        sedok = "Who The Fuck Are You? Get Your Own WhiteEyeUserBot."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    plugin_name, page_number = event.data_match.group(1).decode("UTF-8").split("|", 1)
    if plugin_name in CMD_HELP:
        help_string = f"**💡 PLUGIN NAME 💡 :** `{plugin_name}` \n{CMD_HELP[plugin_name]}"
    reply_pop_up_alert = help_string
    reply_pop_up_alert += "\n\n**(C) @WhiteEyeDevs** ".format(plugin_name)
    if len(reply_pop_up_alert) >= 4096:
        crackexy = "`Pasting Your Help Menu.`"
        await event.answer(crackexy, cache_time=0, alert=True)
        out_file = reply_pop_up_alert
        url = "https://del.dog/documents"
        r = requests.post(url, data=out_file.encode("UTF-8")).json()
        url = f"https://del.dog/{r['key']}"
        await event.edit(
            f"Pasted {plugin_name} to {url}",
            link_preview=False,
            buttons=[[custom.Button.inline("Go Back", data=f"backme_{page_number}")]],
        )
    else:
        await event.edit(
            message=reply_pop_up_alert,
            buttons=[[custom.Button.inline("Go Back", data=f"backme_{page_number}")]],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"terminator")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        text = inlinestats
        await event.answer(text, alert=True)
    else:
        txt = "You Can't View My Masters Stats"
        await event.answer(txt, alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wannaspam")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    text1 = "**You Have Chosed A Probhited Option. Therefore, You Have Been Blocked By WhiteEye. 💢**"
    await event.edit(text1)
    await borg(functions.contacts.BlockRequest(event.query.user_id))
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Choose Probhited Option, So Has Been Blocked !** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(
        LOG_CHAT,
        message=PM_E)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"casualbitching")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Ok. Please Wait Until My Master Approves. Don't Spam Or Try Anything Stupid. \nThank You For Contacting Me.")
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Wanted To Talk To You.** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(
        LOG_CHAT,
        message=PM_E)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"askme")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Ok, Wait. You can Ask After Master Approves You. Kindly, Wait.")
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Wanted To Ask You Something** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(
        LOG_CHAT,
        message=PM_E)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"others")))
async def rip(event):
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id in o:
        sedok = "Master, You Don't Need To Use This."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.get_chat()
    him_id = event.query.user_id
    await event.edit("Ok, Wait. You can Ask After Master Approves You. Kindly, Wait.")
    PM_E = f"**#PMEVENT** \nUser ID : {him_id} \n**This User Wanted To Talk To You.** \n[Contact Him](tg://user?id={him_id})"
    await borg.send_message(
        LOG_CHAT,
        message=PM_E)

def paginate_help(page_number, loaded_modules, prefix):
    number_of_rows = 8
    number_of_cols = 2
    helpable_modules = []
    for p in loaded_modules:
        if not p.startswith("_"):
            helpable_modules.append(p)
    helpable_modules = sorted(helpable_modules)
    modules = [
        custom.Button.inline(
            "{} {} {}".format("🇮🇳", x, "🇮🇳"), data="us_plugin_{}|{}".format(x, page_number)
        )
        for x in helpable_modules
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "Previous", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("❌Close", data="close"),
                custom.Button.inline(
                    "Next", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs

                     
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"backme_(.*)")))
async def sed(event):
    sedm = int(event.data_match.group(1).decode("UTF-8"))
    o = await all_pro_s(Config, client1, client2, client3)
    if event.query.user_id not in o:
        sedok = "Who The Fuck Are You? Get Your Own Friday."
        await event.answer(sedok, cache_time=0, alert=True)
        return
    await event.answer("Back", cache_time=0, alert=False)
    # This Is Copy of Above Code. (C) @SpEcHiDe
    buttons = paginate_help(sedm, CMD_HELP, "helpme")
    sed = f"""WhiteEyeUserBot Userbot Modules Are Listed Here !\n
For More Help or Support Visit @WhiteEyeDevs \nCurrently Loaded Plugins: {len(CMD_LIST)}"""
    await event.edit(message=sed, buttons=buttons)                           
