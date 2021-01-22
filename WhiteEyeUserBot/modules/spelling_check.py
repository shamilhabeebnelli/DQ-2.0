from textblob import TextBlob

from WhiteEyeUserBot.Configs import Config
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern="(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if Config.AUTO_SPELL_FIX != True:
        return
    input_str = event.pattern_match.group(1)
    if input_str.startwith(".", "!", "'", "/", ":", "*"):
        pass
    else:
        bm = TextBlob(input_str)
        await event.edit(bm)
