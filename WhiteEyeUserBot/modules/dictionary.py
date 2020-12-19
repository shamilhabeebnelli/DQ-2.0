"""Syntax: .meaning <word>"""

from PyDictionary import PyDictionary
from WhiteEyeUserBot.utils import edit_or_reply, WhiteEye_on_cmd, sudo_cmd

from WhiteEyeUserBot import CMD_HELP


@WhiteEye.on(WhiteEye_on_cmd("meaning (.*)"))
@WhiteEye.on(sudo_cmd("meaning (.*)", allow_sudo=True))
async def _(event):
    dayam = await edit_or_reply(event, "Finding Meaning.....")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    dictionary = PyDictionary()
    a = dictionary.meaning(input_str)
    b = a.get("Noun")
    kaif = ""
    for x in b:
        kaif += x + "\n"
    await dayam.edit(
        f"<b> meaning of {input_str} is:-</b>\n {kaif}",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "dictionary": "**Dictionary**\
\n\n**Syntax : **`.meaning <word>`\
\n**Usage :** Get meaning and pronunciation of a word."
    }
)
