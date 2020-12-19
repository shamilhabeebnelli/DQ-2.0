#    Copyright (C) @WhiteEyeOT 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


#    Copyright (C) @WhiteEyeOT 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import os.path

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd, sudo_cmd

sedpath = "./kaif/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)


@WhiteEye.on(WhiteEye_on_cmd("savepass ?(.*)"))
@WhiteEye.on(sudo_cmd("savepass ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    ujwal = input_str.split(":")
    usermail = ujwal[0]
    passwd = ujwal[1]
    webo = ujwal[2]
    if os.path.exists("./kaif/info.pablo"):
        file = open("./kaif/info.pablo", "a")
    else:
        file = open("./kaif/info.pablo", "x")
        file.close()
        file = open("./kaif/info.pablo", "a")

    userName = usermail
    password = passwd
    website = webo

    usrnm = "UserName: " + userName + "\n"
    pwd = "Password: " + password + "\n"
    web = "Website: " + website + "\n"

    file.write("---------------------------------\n")
    file.write(usrnm)
    file.write(pwd)
    file.write(web)
    file.write("---------------------------------\n")
    file.write("\n")
    file.close
    await event.edit(
        f"<b><u>Password Saved Successfully</b></u>",
        parse_mode="HTML",
    )


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"viewpass"))
async def hi(event):
    if event.fwd_from:
        return
    file = open("./kaif/info.pablo", "r")
    content = file.read()
    file.close()
    await event.edit(
        f"<b><u>Here are your Saved Passwords</u></b>\n<code>{content}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "password_helper": "**Password Helper**\
\n\n**Syntax : **`.savepass email:password:website`\
\n**Usage :** Saves the email, password and website.\
\n\n**Syntax : **`.viewpass`\
\n**Usage :** View all your saved emails and passwords.\
\n\n**Example : **`.savepass myemail@gmail.com:mypassword:netflix.com`\
\nThis above syntax is saving my Netflix account email and password."
    }
)
