import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30 , STRING31
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from Utils import RAID, RRAID

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
blazev = STRING22
blazew = STRING23
blazex = STRING24
blazey = STRING25
blazez = STRING26
blazeaa = STRING27
blazeab = STRING28
blazeac = STRING29
blazead = STRING30
blazeae = STRING31

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
blv = ""
blw = ""
blx = ""
bly = ""
blz = ""
baa = ""
bab = ""
bac = ""
bad = ""
bae = ""

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
    global blv
    global blw
    global blx
    global bly
    global blz
    global baa
    global bab
    global bac
    global bad
    global bae
 

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

    if blazev:
        session_name = str(blazev)
        print("String 22 Found")
        blv = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 22")
            await blv.start()
            botme = await blv.get_me()
            await blv(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blv(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 22 not Found")
        session_name = "startup"
        blv = TelegramClient(session_name, api, hash)
        try:
            await blv.start()
        except Exception as e:
            pass

    if blazew:
        session_name = str(blazew)
        print("String 23 Found")
        blw = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 23")
            await blw.start()
            botme = await blw.get_me()
            await blw(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blw(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 23 not Found")
        session_name = "startup"
        blw = TelegramClient(session_name, api, hash)
        try:
            await blw.start()
        except Exception as e:
            pass

    if blazex:
        session_name = str(blazex)
        print("String 24 Found")
        blx = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 24")
            await blx.start()
            botme = await blx.get_me()
            await blx(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blx(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 24 not Found")
        session_name = "startup"
        blx = TelegramClient(session_name, api, hash)
        try:
            await blx.start()
        except Exception as e:
            pass


    if blazey:
        session_name = str(blazey)
        print("String 25 Found")
        bly = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 25")
            await bly.start()
            botme = await bly.get_me()
            await bly(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bly(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 25 not Found")
        session_name = "startup"
        bly = TelegramClient(session_name, api, hash)
        try:
            await bly.start()
        except Exception as e:
            pass

    if blazez:
        session_name = str(blazez)
        print("String 26 Found")
        blz = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 26")
            await blz.start()
            botme = await blz.get_me()
            await blz(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await blz(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 26 not Found")
        session_name = "startup"
        blz = TelegramClient(session_name, api, hash)
        try:
            await blz.start()
        except Exception as e:
            pass

    if blazeaa:
        session_name = str(blazeaa)
        print("String 27 Found")
        baa = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 27")
            await baa.start()
            botme = await baa.get_me()
            await baa(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await baa(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 27 not Found")
        session_name = "startup"
        baa = TelegramClient(session_name, api, hash)
        try:
            await baa.start()
        except Exception as e:
            pass

    if blazeab:
        session_name = str(blazeab)
        print("String 28 Found")
        bab = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 28")
            await bab.start()
            botme = await bab.get_me()
            await bab(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bab(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 28 not Found")
        session_name = "startup"
        bab = TelegramClient(session_name, api, hash)
        try:
            await bab.start()
        except Exception as e:
            pass

    if blazeac:
        session_name = str(blazeac)
        print("String 29 Found")
        bac = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 29")
            await bac.start()
            botme = await bac.get_me()
            await bac(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bac(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 29 not Found")
        session_name = "startup"
        bac = TelegramClient(session_name, api, hash)
        try:
            await bac.start()
        except Exception as e:
            pass

    if blazead:
        session_name = str(blazead)
        print("String 30 Found")
        bad = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 30")
            await bad.start()
            botme = await bad.get_me()
            await bad(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bad(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 30 not Found")
        session_name = "startup"
        bad = TelegramClient(session_name, api, hash)
        try:
            await bad.start()
        except Exception as e:
            pass

    if blazeae:
        session_name = str(blazeae)
        print("String 31 Found")
        bae = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 31")
            await bae.start()
            botme = await bae.get_me()
            await bae(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bae(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "startup"
        bae = TelegramClient(session_name, api, hash)
        try:
            await bae.start()
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

@bla.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.bio"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗼\n\nCommand:\n\n.bio <Message to set Bio of Userbot accounts>"
    if e.sender_id in BLAZEA_USERS:
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)     
        if len(e.text) > 5:
            bio = str(bLaZe[0])
            text = "Changing Bio"
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.account.UpdateProfileRequest(about=bio))
                await event.edit("Succesfully Changed Bio...... bLaZe Spam Bot")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )



@bla.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.join"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.bio"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.bio"))



async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in BLAZEA_USERS:
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = bLaZe[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
           
@bla.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in BLAZEA_USERS:
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = bLaZe[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("Succesfully Joined")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@bla.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.leave"))


async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in BLAZEA_USlERS:
        bLaZe = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = bLaZe[0]
            bc = int(bc)
            text = "BLaZe TeAm Leaving...."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
@bla.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.spam"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
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
            
@bla.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))


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

@bla.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))


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

@bla.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.bio"))


async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in BLAZEA_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        bLaZe = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        blazea = await e.get_reply_message()
        if len(bLaZe) == 2:
            message = str(bLaZe[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(BLaZe[0])
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
            
@bla.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))

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

@bla.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))


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
    
@bla.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.ping"))

async def ping(e):
    if e.sender_id in BLAZEA_USERS:
        start = datetime.now()
        text = "╰•★★  ℘ơŋɠ ★★•╯"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🔰【★𓆩βƖꪖƹꫀ★】✘ sρꪖꪑꪑε𝚁 \n\n╰•★★  ℘ơŋɠ ★★•╯\n╔═╗╔═╗╔═╦╗╔══╗\n║╬║║║║║║║║║╔═╣\n║╔╝║║║║║║║║╚╗║\n╚╝─╚═╝╚╩═╝╚══╝\n`{ms}` 𝗺𝘀")

@bla.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.restart"))



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
        

            
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
@bla.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.help"))


async def help(e):
    if e.sender_id in BLAZEA_USERS:
       text = "𝗔𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀\n\n𝙐𝙩𝙞𝙡𝙨 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.ping\n.restart\n\n𝙐𝙨𝙚𝙧𝙗𝙤𝙩 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.bio\n.join\n.pjoin\n.leave\n\n𝙎𝙥𝙖𝙢 𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
       await e.reply(text, parse_mode=None, link_preview=None )

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
