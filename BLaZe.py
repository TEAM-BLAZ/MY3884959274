import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, ALIVE_NAME, USERNAME, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID
import git
import heroku3

api = API_ID
hash = API_HASH
blazea = STRING
blazeb = STRING2
blazec = STRING3
blazed = STRING4
blazee = STRING5
blazef = STRING6
blazeg = STRING7
blazeh = STRING8
blazei = STRING9
blazej = STRING10
blazek = STRING11
blazel = STRING12
blazem = STRING13
blazen = STRING14
blazeo = STRING15
blazep = STRING16
blazeq = STRING17
blazer = STRING18
blazes = STRING19
blazet = STRING20
blazeu = STRING21



bla = ""
blb = ""
blc = ""
bld = ""
ble = ""
blf = ""
blg = ""
blh = ""
bli = ""
blj = ""
blk = ""
bll = ""
blm = ""
bln = ""
blo = ""
blp = ""
blq = ""
blr = ""
bls = ""
blt = ""
blu = ""



que = {}

BLAZEA_USERS = []
for x in SUDO: 
    BLAZEA_USERS.append(x)
    
async def start_BLaZe():
    global bla
    global blb
    global blc
    global bld
    global ble
    global blf
    global blg
    global blh
    global bli
    global blj
    global blk
    global bll
    global blm
    global bln
    global blo
    global blp
    global blq
    global blr
    global bls
    global blt
    global blu
    
 

    if blazea:
        session_name = str(blazea)
        print("String 1 Found")
        bla = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 1")
            await bla.start()
            botme = await bla.get_me()
            await bla(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bla(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
            bla = "BLAZEA"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "startup"
        bla = TelegramClient(session_name, api, hash)
        try:
            await bla.start()
        except Exception as e:
            pass

    if blazeb:
        session_name = str(blazeb)
        print("String 2 Found")
        blb = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 2")
            await blb.start()
            botme = await blb.get_me()
            await blb(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blb(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 2 not Found")
        session_name = "startup"
        blb = TelegramClient(session_name, api, hash)
        try:
            await blb.start()
        except Exception as e:
            pass

    if blazec:
        session_name = str(blazec)
        print("String 3 Found")
        blc = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 3")
            await blc.start()
            botme = await blc.get_me()
            await blc(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blc(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 3 not Found")
        session_name = "startup"
        blc = TelegramClient(session_name, api, hash)
        try:
            await blc.start()
        except Exception as e:
            pass

    if blazed:
        session_name = str(blazed)
        print("String 4 Found")
        bld = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 4")
            await bld.start()
            botme = await bld.get_me()
            await bld(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bld(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 4 not Found")
        session_name = "startup"
        bld = TelegramClient(session_name, api, hash)
        try:
            await bld.start()
        except Exception as e:
            pass

    if blazee:
        session_name = str(blazee)
        print("String 5 Found")
        ble = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 5")
            await ble.start()
            botme = await ble.get_me()
            await ble(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await ble(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 5 not Found")
        session_name = "startup"
        ble = TelegramClient(session_name, api, hash)
        try:
            await ble.start()
        except Exception as e:
            pass

    if blazef:
        session_name = str(blazef)
        print("String 6 Found")
        blf = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 6")
            await blf.start()
            botme = await blf.get_me()
            await blf(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blf(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 6 not Found")
        session_name = "startup"
        blf = TelegramClient(session_name, api, hash)
        try:
            await blf.start()
        except Exception as e:
            pass

    if blazeg:
        session_name = str(blazeg)
        print("String 7 Found")
        blg = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 7")
            await blg.start()
            botme = await blg.get_me()
            await blg(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blg(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 7 not Found")
        session_name = "startup"
        blg = TelegramClient(session_name, api, hash)
        try:
            await blg.start()
        except Exception as e:
            pass

    if blazeh:
        session_name = str(blazeh)
        print("String 8 Found")
        blh = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 8")
            await blh.start()
            botme = await blh.get_me()
            await blh(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blh(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 8 not Found")
        session_name = "startup"
        blh = TelegramClient(session_name, api, hash)
        try:
            await blh.start()
        except Exception as e:
            pass

    if blazei:
        session_name = str(blazei)
        print("String 9 Found")
        bli = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 9")
            await bli.start()
            botme = await bli.get_me()
            await bli(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bli(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 9 not Found")
        session_name = "startup"
        bli = TelegramClient(session_name, api, hash)
        try:
            await bli.start()
        except Exception as e:
            pass

    if blazej:
        session_name = str(blazej)
        print("String 10 Found")
        blj = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 10")
            await blj.start()
            botme = await blj.get_me()
            await blj(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blj(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 10 not Found")
        session_name = "startup"
        blj = TelegramClient(session_name, api, hash)
        try:
            await blj.start()
        except Exception as e:
            pass

    if blazek:
        session_name = str(blazek)
        print("String 11 Found")
        blk = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 11")
            await blk.start()
            botme = await blk.get_me()
            await blk(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blk(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 11 not Found")
        session_name = "startup"
        blk = TelegramClient(session_name, api, hash)
        try:
            await blk.start()
        except Exception as e:
            pass

    if blazel:
        session_name = str(blazel)
        print("String 12 Found")
        bll = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 12")
            await bll.start()
            botme = await bll.get_me()
            await bll(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bll(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 12 not Found")
        session_name = "startup"
        bll = TelegramClient(session_name, api, hash)
        try:
            await bll.start()
        except Exception as e:
            pass

    if blazem:
        session_name = str(blazem)
        print("String 13 Found")
        blm = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 13")
            await blm.start()
            botme = await blm.get_me()
            await blm(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blm(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 13 not Found")
        session_name = "startup"
        blm = TelegramClient(session_name, api, hash)
        try:
            await blm.start()
        except Exception as e:
            pass

    if blazen:
        session_name = str(blazen)
        print("String 14 Found")
        bln = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 14")
            await bln.start()
            botme = await bln.get_me()
            await bln(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bln(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 14 not Found")
        session_name = "startup"
        bln = TelegramClient(session_name, api, hash)
        try:
            await bln.start()
        except Exception as e:
            pass

    if blazeo:
        session_name = str(blazeo)
        print("String 15 Found")
        blo = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 15")
            await blo.start()
            botme = await blo.get_me()
            await blo(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blo(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 15 not Found")
        session_name = "startup"
        blo = TelegramClient(session_name, api, hash)
        try:
            await blo.start()
        except Exception as e:
            pass

    if blazep:
        session_name = str(blazep)
        print("String 16 Found")
        blp = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 16")
            await blp.start()
            botme = await blp.get_me()
            await blp(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blp(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "startup"
        blp = TelegramClient(session_name, api, hash)
        try:
            await blp.start()
        except Exception as e:
            pass

    if blazeq:
        session_name = str(blazeq)
        print("String 17 Found")
        blq = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 17")
            await blq.start()
            botme = await blq.get_me()
            await blq(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blq(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "startup"
        blq = TelegramClient(session_name, api, hash)
        try:
            await blq.start()
        except Exception as e:
            pass

    if blazer:
        session_name = str(blazer)
        print("String 18 Found")
        blr = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 18")
            await blr.start()
            botme = await blr.get_me()
            await blr(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blr(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "startup"
        blr = TelegramClient(session_name, api, hash)
        try:
            await blr.start()
        except Exception as e:
            pass

    if blazes:
        session_name = str(blazes)
        print("String 19 Found")
        bls = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 19")
            await bls.start()
            botme = await bld.get_me()
            await bls(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bls(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "startup"
        bls = TelegramClient(session_name, api, hash)
        try:
            await bls.start()
        except Exception as e:
            pass

    if blazet:
        session_name = str(blazet)
        print("String 20 Found")
        blt = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 20")
            await blt.start()
            botme = await blt.get_me()
            await blt(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blt(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "startup"
        blt = TelegramClient(session_name, api, hash)
        try:
            await blt.start()
        except Exception as e:
            pass

    if blazeu:
        session_name = str(blazeu)
        print("String 21 Found")
        blu = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 21")
            await blu.start()
            botme = await blu.get_me()
            await blu(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blu(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 21 not Found")
        session_name = "startup"
        blu = TelegramClient(session_name, api, hash)
        try:
            await blu.start()
        except Exception as e:
            pass

    

loop = asyncio.get_event_loop()
loop.run_until_complete(start_BLaZe())    
   
async def gifspam(e, blazea):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=blazea.media.document.access_hash,
                    file_reference=blazea.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception as e:
        pass


@blb.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,spam"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\ncσммαη∂:\n\n,вs∂к <cσυηт> <мεssαgε тσ sραм>\n\n,вs∂к <cσυηт> <яερℓү тσ α мεssαgε>\n\ncσυηт мυsт вε α ιηтεgεя."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        blazea = await e.get_reply_message()
        if len(bLaZe) == 2:
            message = str(bLaZe[1])
            counter = int(bLaZe[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and blazea.media:  
            counter = int(alex[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            for _ in range(counter): 
                blazea = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, blazea)  
        elif e.reply_to_msg_id and blazea.text:
            message = blazea.text
            counter = int(alex[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None )
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,delayspam"))



async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        blazea = await e.get_reply_message()
        bLaZe = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        bLaZesexy = bLaZe[1:]
        if len(bLaZesexy) == 2:
            message = str(bLaZesexy[1])
            counter = int(bLaZesexy[0])
            sleeptime = float(bLaZe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await blazea.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and blazea.media:  
            counter = int(alexsexy[0])
            sleeptime = float(alex[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    blazea = await e.client.send_file(e.chat_id, blaze, caption=blazea.text)
                    await gifspam(e, blazea) 
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and blazea.text:
            message = blazea.text
            counter = int(alexsexy[0])
            sleeptime = float(alex[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,bigspam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        blazea = await e.get_reply_message()
        if len(bLaZe) == 2:
            message = str(bLaZe[1])
            counter = int(bLaZe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await blazea.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and blazea.media:  
            counter = int(blaze[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    blazea = await e.client.send_file(e.chat_id, blazea, caption=blazea.text)
                    await gifspam(e, blazea) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and blazea.text:
            message = blazea.text
            counter = int(bLaZe[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,bsdk"))

async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bLaZea = await e.get_reply_message()
        if len(bLaZe) == 2:
            message = str(bLaZe[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(bLaZe[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(bLaZe[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )




@bla.on(events.NewMessage(incoming=True))
@blb.on(events.NewMessage(incoming=True))
@blc.on(events.NewMessage(incoming=True))
@bld.on(events.NewMessage(incoming=True))
@ble.on(events.NewMessage(incoming=True))
@blf.on(events.NewMessage(incoming=True))
@blg.on(events.NewMessage(incoming=True))
@blh.on(events.NewMessage(incoming=True))
@bli.on(events.NewMessage(incoming=True))
@blj.on(events.NewMessage(incoming=True))
@blk.on(events.NewMessage(incoming=True))
@bll.on(events.NewMessage(incoming=True))
@blm.on(events.NewMessage(incoming=True))
@bln.on(events.NewMessage(incoming=True))
@blo.on(events.NewMessage(incoming=True))
@blp.on(events.NewMessage(incoming=True))
@blq.on(events.NewMessage(incoming=True))
@blr.on(events.NewMessage(incoming=True))
@bls.on(events.NewMessage(incoming=True))
@blt.on(events.NewMessage(incoming=True))
@blu.on(events.NewMessage(incoming=True))




async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )           
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,replybsdk"))

async def spam(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        blazea = await e.get_reply_message()
        if len(e.text) > 11:
            message = str(bLaZe[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,dreplybsdk"))


async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        blazea = await e.get_reply_message()
        if len(e.text) > 12:
            message = str(bLaZe[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        elif e.reply_to_msg_id:             
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception as f:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None )
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
    
@bla.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,ping"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,ping"))


async def ping(e):
    if e.sender_id in BLAZEA_USERS:
        start = datetime.now()
        text = "╰•★★  ℘ơŋɠ ★★•╯"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"⚔️【★𝖡𝖫𝖠𝖹𝖤 ★】 𝙁𝙄𝙂𝙃𝙏𝙀𝙍𝙎★➤➤♛ \n\n╰★╯Ɽυкσ נαяα sαвαя кαяσ...╰★╯\n`{ms}` ℳʂ [{ALIVE_NAME}](https://t.me/{USERNAME})")


@bla.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,restart"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,restart"))

async def restart(e):
    if e.sender_id in BLAZEA_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None )
        try:
            await bla.disconnect()
        except Exception as e:
            pass
        try:
            await blb.disconnect()
        except Exception as e:
            pass
        try:
            await blc.disconnect()
        except Exception as e:
            pass
        try:
            await bld.disconnect()
        except Exception as e:
            pass
        try:
            await ble.disconnect()
        except Exception as e:
            pass
            await blf.disconnect()
        except Exception as e:
            pass
        try:
            await blg.disconnect()
        except Exception as e:
            pass
        try:
            await blh.disconnect()
        except Exception as e:
            pass
        try:
            await bli.disconnect()
        except Exception as e:
            pass
        try:
            await blj.disconnect()
        except Exception as e:
            pass
            await blk.disconnect()
        except Exception as e:
            pass
        try:
            await bll.disconnect()
        except Exception as e:
            pass
        try:
            await blm.disconnect()
        except Exception as e:
            pass
        try:
            await bln.disconnect()
        except Exception as e:
            pass
        try:
            await blo.disconnect()
        except Exception as e:
            pass
            await blp.disconnect()
        except Exception as e:
            pass
        try:
            await blq.disconnect()
        except Exception as e:
            pass
        try:
            await blr.disconnect()
        except Exception as e:
            pass
        try:
            await bls.disconnect()
        except Exception as e:
            pass
        try:
            await blt.disconnect()
        except Exception as e:
            pass
        try:
            await blu.disconnect()
        except Exception as e:
            pass
                               

            
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
@blb.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blf.on(events.NewMessage(incoming=True, pattern=r",help"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,help"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,help"))


async def help(e):
    if e.sender_id in BLAZEA_USERS:
       text = "| 𝐓 𝐄 𝐀 𝐌 • ‌«[ 𝐁𝐋𝐀𝐙𝐄]»𝙁𝙄𝙂𝙃𝙏𝙀𝙍𝙎★➤➤♛✘ ๛ :\n#𝗕𝗟𝗔𝗭𝗘_𝗦𝗣𝗔𝗠𝗠𝗘𝗥\nᎪ𝚅Ꭺ𝙸ᏞᎪ𝙱Ꮮ𝙴  ᏟᎾ𝙼𝙼ᎪᏁᎠ𝚂\n\n#𝗖𝗢𝗠𝗠𝗔𝗡𝗗:\n,𝙿ᎥᏁᎶ\n,Ꮢ𝚎𝚜𝚃𝚊𝚛𝚃\n,𝚁𝙴𝙿𝙾\n,𝙰𝙻𝙸𝚅𝙴\n\n#𝗦𝗣𝗔𝗠_𝗖𝗢𝗠𝗠𝗔𝗡𝗗:\n,𝚂𝙿𝙰𝙼\n,𝙳𝙴𝙻𝙰𝚈𝚂𝙿𝙰𝙼\n,𝙱𝙸𝙶𝚂𝙿𝙰𝙼\n,𝙱𝚂𝙳𝙺\n,𝚁𝙴𝙿𝙻𝚈𝙱𝚂𝙳𝙺\n,𝙳𝚁𝙴𝙿𝙻𝚈𝙱𝚂𝙳𝙺\n\n#𝗕𝗟𝗔𝗭𝗘_𝗦𝗣𝗔𝗠𝗠𝗘𝗥\n ғσя мσяε #нεℓρ #яεgαя∂ιηg υsαgε σғ #ρℓυgιηs түρε ρℓυgιηs #ηαмεs"
    await e.reply(text, parse_mode=None, link_preview=None )

@bla.on(events.NewMessage(incoming=True, pattern=r"\,repo"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,repo"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\,repo"))



async def repo(e):
    if e.sender_id in BLAZEA_USERS:
        start = datetime.now()
        text = "★★вℓαᘔε ηε✞ሠᎾяᏦ★★"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n➤ 𝐃𝐄𝐏𝐋𝐎𝐘 𝐓𝐎 50 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓𝐒 𝐈𝐍 𝐎𝐍 𝐓𝐌𝐄...\n➤ 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 :- [#𝗧𝗛𝗘_𝗕𝗟𝗔𝗭𝗘_𝗡𝗘𝗧𝗪𝗢𝗥𝗞](https://t.me/BLAZE_SPAMMER)\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n ┏━━━━━━━━━━━━━━━━━━━━━\n ┣➤∆ 𝚅𝙴𝚁𝚈 𝙵𝙰𝚂𝚃 𝚂𝙿𝙰𝙼...\n ┣    ∆ 𝙽𝙾𝙽 𝚂𝚃𝙾𝙿 𝚂𝙿𝙰𝙼...    \n ┣ 🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰\n ┣\n ┣ ┈ ➤  🔱   [𝗥𝗘𝗣𝗢](https://github.com/TEAM-BLAZ/BLAZE-SPAMMER-ROBOT)      \n ┣      \n ┣  ┈➤  🔱   [𝗦𝗧𝗥𝗜𝗡𝗚](https://replit.com/@BLAZE-NETWORK/BLAZE-SPAMMER)\n ┣\n ┗━━━━━━━━━━━━━━━━━━━━━")
#####BLAZE OP BAKI LUND KI TOPI####
import os
blazespammer = os.environ.get("ALIVE_PIC",None)
if not blazespammer:
 blazespammer="https://telegra.ph/file/2ab64117e0f74971ddb9e.jpg"
##########COPY KRE USKI MA KA BOSDA#######

@bla.on(events.NewMessage(incoming=True, pattern=r"\,alive"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,alive"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\,alive"))

async def alive(event):
  if event.sender_id in BLAZEA_USERS:
    sed = await event.client.get_me()
    kk = sed.first_name
    k = sed.id
    s = f"[{kk}](tg://user?id={k})"
    tf = f"""
**》𝙸'𝙼 {s} 𝙼𝙴𝙼𝙱𝙴𝚁 𝙾𝙵 𝙱𝙻𝙰𝚉𝙴 𝙽𝙴𝚃𝚆𝙾𝚁𝙺《**
**☞ 𝙸'𝙼 𝙱𝙻𝙰𝚉𝙴 𝚂𝙿𝙰𝙼𝙼𝙴𝚁 𝙰𝙻𝙸𝚅𝙴.....**
**✰𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 𝙸𝚂 𝚆𝙾𝚁𝙺𝙸𝙽𝙶 𝙿𝙴𝚁𝙵𝙴𝙲𝚃𝙻𝚈..✰
📢 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 :- **[➠✧【•𝗧 𝗘 𝗔 𝗠 ✘【𝗕𝗟𝗔𝗭𝗘】] (https://t.me/BLAZE_SPAMMER)** 
**➠  𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙰𝙻𝙻 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂》** `.help` 
"""
    await event.client.send_file(event.chat_id,blazespammer,caption=tf, force_document=False, link_preview=False)
import time
from time import sleep

text = """🔰✘𓆩βƖꪖƹꫀ sρꪖꪑꪑε𝚁 ʀꪮʙʙꪮᴛ Ꭵs 𝙈𝙊𝘿𝙄𝙁𝙄𝙀𝘿...🔰"""
print(text)
print("")
print("✘𓆩βƖꪖƹꫀ sρꪖꪑꪑε𝚁 ʀꪮʙʙꪮᴛ 𝑆T𝔞R𝔱є∂ sU𝐂𝐂εS𝔣𝔲𝔩𝔩Y.")
if len(sys.argv) not in (1, 3, 4):
    try:
        bla.disconnect()
    except Exception as e:
        pass    
    try:
        blb.disconnect()
    except Exception as e:
        pass
    try:
        blc.disconnect()
    except Exception as e:
        pass
    try:
        bld.disconnect()
    except Exception as e:
        pass
    try:
        ble.disconnect()
    except Exception as e:
        pass
    try:
        blf.disconnect()
    except Exception as e:
        pass    
    try:
        blg.disconnect()
    except Exception as e:
        pass
    try:
        blh.disconnect()
    except Exception as e:
        pass
    try:
        bli.disconnect()
    except Exception as e: 
        pass
    try:
        blj.disconnect()
    except Exception as e:
        pass
    try:
        blk.disconnect()
    except Exception as e:
        pass    
    try:
        bll.disconnect()
    except Exception as e:
        pass
    try:
        blm.disconnect()
    except Exception as e:
        pass
    try:
        bln.disconnect()
    except Exception as e:
        pass
    try:
        blo.disconnect()
    except Exception as e:
        pass
    try:
        blp.disconnect()
    except Exception as e:
        pass    
    try:
        blq.disconnect()
    except Exception as e:
        pass
    try:
        blr.disconnect()
    except Exception as e:
        pass
    try:
        bls.disconnect()
    except Exception as e:
        pass
    try:
        blt.disconnect()
    except Exception as e:
        pass
    try:
        blu.disconnect()
    except Exception as e:
        pass    
    
else:
    
    try:
        bla.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blb.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blc.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bld.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ble.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blf.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blg.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blh.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bli.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blk.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bll.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blm.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bln.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blo.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blp.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blq.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blr.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bls.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blt.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blu.run_until_disconnected()
    except Exception as e:
        pass
