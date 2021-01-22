from telethon.events import ChatAction
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd


async def get_full_user(event):
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`User ID Is Required")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Something Went Wrong", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj


@WhiteEye.on(WhiteEye_on_cmd(pattern="gban ?(.*)"))
async def gspider(WhiteEyeUserBot):
    lol = WhiteEyeUserBot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        WhiteEye = await lol.reply("Gbanning This User !")
    else:
        WhiteEye = await lol.edit("Wait Processing.....")
    me = await WhiteEyeUserBot.client.get_me()
    await WhiteEye.edit(f"Global Ban Is Coming ! Wait And Watch You Nigga")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await WhiteEyeUserBot.get_chat()
    a = b = 0
    if WhiteEyeUserBot.is_private:
        user = WhiteEyeUserBot.chat
        reason = WhiteEyeUserBot.pattern_match.group(1)
    else:
        WhiteEyeUserBot.chat.title
    try:
        user, reason = await get_full_user(WhiteEyeUserBot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await WhiteEye.edit(f"**Something W3NT Wrong 🤔**")
    if user:
        if user.id == 1263617196:
            return await WhiteEye.edit(
                f"**Didn't , Your Father Teach You ? That You Cant Gban Dev**"
            )
        try:
            from WhiteEyeUserBot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await WhiteEyeUserBot.client(BlockRequest(user))
        except:
            pass
        testWhiteEyeUserBot = [
            d.entity.id
            for d in await WhiteEyeUserBot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testWhiteEyeUserBot:
            try:
                await WhiteEyeUserBot.client.edit_permissions(
                    i, user, view_messages=False
                )
                a += 1
                await WhiteEye.edit(f"**GBANNED // Total Affected Chats **: `{a}`")
            except:
                b += 1
    else:
        await WhiteEye.edit(f"**Reply to a user !!**")
    try:
        if gmute(user.id) is False:
            return await WhiteEye.edit(f"**Error! User probably already gbanned.**")
    except:
        pass
    return await WhiteEye.edit(
        f"**WhiteEye Gbanned [{user.first_name}](tg://user?id={user.id}) And Added To SpamWatch In The Chats Where Me Is Admin/Owner : {a} **"
    )


@WhiteEye.on(WhiteEye_on_cmd(pattern="ungban ?(.*)"))
async def gspider(WhiteEyeUserBot):
    lol = WhiteEyeUserBot
    sender = await lol.get_sender()
    me = await lol.client.get_me()
    if not sender.id == me.id:
        WhiteEye = await lol.reply("`Wait Let Me Process`")
    else:
        WhiteEye = await lol.edit("One Min ! ")
    me = await WhiteEyeUserBot.client.get_me()
    await WhiteEye.edit(f"Trying To Ungban User !")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await WhiteEyeUserBot.get_chat()
    a = b = 0
    if WhiteEyeUserBot.is_private:
        user = WhiteEyeUserBot.chat
        reason = WhiteEyeUserBot.pattern_match.group(1)
    else:
        WhiteEyeUserBot.chat.title
    try:
        user, reason = await get_full_user(WhiteEyeUserBot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await WhiteEye.edit("Someting Went Wrong 🤔")
    if user:
        if user.id == 1263617196:
            return await WhiteEye.edit("**You Cant Ungban A Dev !**")
        try:
            from WhiteEyeUserBot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await WhiteEyeUserBot.client(UnblockRequest(user))
        except:
            pass
        testWhiteEyeUserBot = [
            d.entity.id
            for d in await WhiteEyeUserBot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testWhiteEyeUserBot:
            try:
                await WhiteEyeUserBot.client.edit_permissions(
                    i, user, send_messages=True
                )
                a += 1
                await WhiteEye.edit(f"**UNGBANNING // AFFECTED CHATS - {a} **")
            except:
                b += 1
    else:
        await WhiteEye.edit("**Reply to a user !!**")
    try:
        if ungmute(user.id) is False:
            return await WhiteEye.edit("**Error! User probably already ungbanned.**")
    except:
        pass
    return await WhiteEye.edit(
        f"**UNGBANNED // USER - [{user.first_name}](tg://user?id={user.id}) CHATS : {a} **"
    )


@WhiteEye.on(ChatAction)
async def handler(rkG):
    if rkG.user_joined or rkG.user_added:
        try:
            from WhiteEyeUserBot.modules.sql_helper.gmute_sql import is_gmuted

            guser = await rkG.get_user()
            gmuted = is_gmuted(guser.id)
        except:
            return
        if gmuted:
            for i in gmuted:
                if i.sender == str(guser.id):
                    chat = await rkG.get_chat()
                    admin = chat.admin_rights
                    creator = chat.creator
                    if admin or creator:
                        try:
                            await client.edit_permissions(
                                rkG.chat_id, guser.id, view_messages=False
                            )
                            await rkG.reply(
                                f"**Gbanned User Joined!!** \n"
                                f"**Victim Id**: [{guser.id}](tg://user?id={guser.id})\n"
                                f"**Action **  : `Banned`"
                            )
                        except:
                            rkG.reply("`No Permission To Ban`")
                            return


CMD_HELP.update(
    {
        "gban_gmute": "**Gban_Gmute**\
\n\n**Syntax : **`.gban <reply to a user / mention their ID>`\
\n**Usage :** bans the user in every group where you are admin.\
\n\n**Syntax : **`.ungban <reply to a user / mention their ID>`\
\n**Usage :** unbans the user in every group where you are admin."
    }
)
