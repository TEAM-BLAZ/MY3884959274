import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4, STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10, STRING11, STRING12 , STRING13 , STRING14 , STRING15 ,STRING16 , STRING17 , STRING18 , STRING19 , STRING20 , STRING21 , STRING22 , STRING23 , STRING24 , STRING25 , STRING26 , STRING27 , STRING28 , STRING29 , STRING30 , STRING31, STRING32, STRING33, STRING34, STRING35, STRING36, STRING37, STRING38, STRING39, STRING40, STRING41, STRING42, STRING43, STRING44, STRING45, STRING46, STRING47, STRING48, STRING49, STRING50
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
blazeaf = STRING32
blazeag = STRING33
blazeah = STRING34
blazeai = STRING35
blazeaj = STRING36
blazeak = STRING37
blazeal = STRING38
blazeam = STRING39
blazean = STRING40
blazeao = STRING41
blazeap = STRING42
blazeaq = STRING43
blazear = STRING44
blazeas = STRING45
blazeat = STRING46
blazeau = STRING47
blazeav = STRING48
blazeaw = STRING49
blazeax = STRING50

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
baf = ""
bag = ""
bah = ""
bai = ""
baj = ""
bak = ""
bal = ""
bam = ""
ban = ""
bao = ""
bap = ""
baq = ""
bar = ""
bas = ""
bat = ""
bau = ""
bav = ""
baw = ""
bax = ""


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
    global baf
    global bag
    global bah
    global bai
    global baj
    global bak
    global bal
    global bam
    global ban
    global bao
    global bap
    global baq
    global bar
    global bas
    global bat
    global bau
    global bav
    global baw
    global bax
 

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


    if blazeaf:
        session_name = str(blazeaf)
        print("String 32 Found")
        baf = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 32")
            await baf.start()
            botme = await baf.get_me()
            await baf(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await baf(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 32 not Found")
        session_name = "startup"
        baf = TelegramClient(session_name, api, hash)
        try:
            await baf.start()
        except Exception as e:
            pass

    if blazeag:
        session_name = str(blazeag)
        print("String 33 Found")
        bag = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 33")
            await bag.start()
            botme = await bag.get_me()
            await bag(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bag(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 33 not Found")
        session_name = "startup"
        bag = TelegramClient(session_name, api, hash)
        try:
            await bag.start()
        except Exception as e:
            pass

    if blazeah:
        session_name = str(blazeah)
        print("String 34 Found")
        bah = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 34")
            await bah.start()
            botme = await bah.get_me()
            await bah(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bah(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 34 not Found")
        session_name = "startup"
        bah = TelegramClient(session_name, api, hash)
        try:
            await bah.start()
        except Exception as e:
            pass

    if blazeai:
        session_name = str(blazeai)
        print("String 35 Found")
        bai = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 35")
            await bai.start()
            botme = await bai.get_me()
            await bai(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bai(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 35 not Found")
        session_name = "startup"
        bai = TelegramClient(session_name, api, hash)
        try:
            await bai.start()
        except Exception as e:
            pass

    if blazeaj:
        session_name = str(blazeaj)
        print("String 36 Found")
        baj = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 36")
            await baj.start()
            botme = await baj.get_me()
            await baj(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await baj(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "startup"
        baj = TelegramClient(session_name, api, hash)
        try:
            await baj.start()
        except Exception as e:
            pass

    if blazeak:
        session_name = str(blazeak)
        print("String 37 Found")
        bak = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 37")
            await bak.start()
            botme = await bak.get_me()
            await bak(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bak(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "startup"
        bak = TelegramClient(session_name, api, hash)
        try:
            await bak.start()
        except Exception as e:
            pass

    if blazeal:
        session_name = str(blazeal)
        print("String 38 Found")
        bal = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 38")
            await bal.start()
            botme = await bal.get_me()
            await bal(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bal(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "startup"
        bal = TelegramClient(session_name, api, hash)
        try:
            await bal.start()
        except Exception as e:
            pass

    if blazeam:
        session_name = str(blazeam)
        print("String 39 Found")
        bam = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 39")
            await bam.start()
            botme = await bam.get_me()
            await bam(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bam(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "startup"
        bam = TelegramClient(session_name, api, hash)
        try:
            await baclm.start()
        except Exception as e:
            pass

    if blazean:
        session_name = str(blazean)
        print("String 40 Found")
        ban = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 40")
            await ban.start()
            botme = await bad.get_me()
            await ban(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await ban(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "startup"
        ban = TelegramClient(session_name, api, hash)
        try:
            await ban.start()
        except Exception as e:
            pass

    if blazeao:
        session_name = str(blazeao)
        print("String 41 Found")
        bao = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 41")
            await bao.start()
            botme = await bao.get_me()
            await bao(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bao(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 41 not Found")
        session_name = "startup"
        bao = TelegramClient(session_name, api, hash)
        try:
            await bao.start()
        except Exception as e:
            pass
    
    if blazeap:
        session_name = str(blazeap)
        print("String 42 Found")
        bap = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 42")
            await bap.start()
            botme = await bap.get_me()
            await bap(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bap(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 42 not Found")
        session_name = "startup"
        bap = TelegramClient(session_name, api, hash)
        try:
            await bap.start()
        except Exception as e:
            pass

    if blazeaq:
        session_name = str(blazeaq)
        print("String 43 Found")
        baq = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 43")
            await baq.start()
            botme = await baq.get_me()
            await baq(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await baq(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 43 not Found")
        session_name = "startup"
        baq = TelegramClient(session_name, api, hash)
        try:
            await baq.start()
        except Exception as e:
            pass

    if blazear:
        session_name = str(blazear)
        print("String 44 Found")
        bar = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 44")
            await bar.start()
            botme = await bar.get_me()
            await bar(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bar(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 44 not Found")
        session_name = "startup"
        bar = TelegramClient(session_name, api, hash)
        try:
            await bar.start()
        except Exception as e:
            pass

    if blazeas:
        session_name = str(blazeas)
        print("String 45 Found")
        bas = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 45")
            await bas.start()
            botme = await bas.get_me()
            await bas(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bas(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 45 not Found")
        session_name = "startup"
        bas = TelegramClient(session_name, api, hash)
        try:
            await bas.start()
        except Exception as e:
            pass

    if blazeat:
        session_name = str(blazeat)
        print("String 46 Found")
        bat = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 46")
            await bat.start()
            botme = await bat.get_me()
            await bat(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bat(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 46 not Found")
        session_name = "startup"
        bat = TelegramClient(session_name, api, hash)
        try:
            await bat.start()
        except Exception as e:
            pass

    if blazeau:
        session_name = str(blazeau)
        print("String 47 Found")
        bau = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 47")
            await bau.start()
            botme = await bau.get_me()
            await bau(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bau(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 47 not Found")
        session_name = "startup"
        bau = TelegramClient(session_name, api, hash)
        try:
            await bau.start()
        except Exception as e:
            pass

    if blazeav:
        session_name = str(blazeav)
        print("String 48 Found")
        bav = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 48")
            await bav.start()
            botme = await bav.get_me()
            await bav(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bav(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 48 not Found")
        session_name = "startup"
        bav = TelegramClient(session_name, api, hash)
        try:
            await bav.start()
        except Exception as e:
            pass

    if blazeaw:
        session_name = str(blazeaw)
        print("String 49 Found")
        baw = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 49")
            await baw.start()
            botme = await baw.get_me()
            await baw(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await baw(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 49 not Found")
        session_name = "startup"
        baw = TelegramClient(session_name, api, hash)
        try:
            await baw.start()
        except Exception as e:
            pass
    
    if blazeax:
        session_name = str(blazeax)
        print("String 50 Found")
        bax = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 50")
            await bax.start()
            botme = await bax.get_me()
            await bax(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bax(functions.channels.JoinChannelRequest(channel="@THE_BLAZE_NETWORK"))           
            botid = telethon.utils.get_peer_id(botme)
            BLAZEA_USERS.append(botid)
        except Exception as e:
          
            print(e)
            pass
    else:
        print("Session 50 not Found")
        session_name = "startup"
        bax = TelegramClient(session_name, api, hash)
        try:
            await bax.start()
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

@bla.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\,bio"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\,bio"))



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
@blv.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\,spam"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\,spam"))

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
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))





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


@blb.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))


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


@blb.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.raid"))

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
@blv.on(events.NewMessage(incoming=True))
@blw.on(events.NewMessage(incoming=True))
@blx.on(events.NewMessage(incoming=True))
@bly.on(events.NewMessage(incoming=True))
@blz.on(events.NewMessage(incoming=True))
@baa.on(events.NewMessage(incoming=True))
@bab.on(events.NewMessage(incoming=True))
@bac.on(events.NewMessage(incoming=True))
@bad.on(events.NewMessage(incoming=True))
@bae.on(events.NewMessage(incoming=True))
@baf.on(events.NewMessage(incoming=True))
@bag.on(events.NewMessage(incoming=True))
@bah.on(events.NewMessage(incoming=True))
@bai.on(events.NewMessage(incoming=True))
@baj.on(events.NewMessage(incoming=True))
@bak.on(events.NewMessage(incoming=True))
@bal.on(events.NewMessage(incoming=True))
@bam.on(events.NewMessage(incoming=True))
@ban.on(events.NewMessage(incoming=True))
@bao.on(events.NewMessage(incoming=True))
@bap.on(events.NewMessage(incoming=True))
@baq.on(events.NewMessage(incoming=True))
@bar.on(events.NewMessage(incoming=True))
@bas.on(events.NewMessage(incoming=True))
@bat.on(events.NewMessage(incoming=True))
@bau.on(events.NewMessage(incoming=True))
@bav.on(events.NewMessage(incoming=True))
@baw.on(events.NewMessage(incoming=True))
@bax.on(events.NewMessage(incoming=True))



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
            

@blb.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))

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


@blb.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))








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
@blf.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.ping"))


async def ping(e):
    if e.sender_id in BLAZEA_USERS:
        start = datetime.now()
        text = "╰•★★  ℘ơŋɠ ★★•╯"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"⚔️【★𝖡𝖫𝖠𝖹𝖤 ★】 𝙁𝙄𝙂𝙃𝙏𝙀𝙍𝙎★➤➤♛ \n\n╰★╯Ɽυкσ נαяα sαвαя кαяσ...╰★╯\n`{ms}` ℳʂ [{ALIVE_NAME}](https://t.me/{USERNAME})")


@bla.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.restart"))






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
            await blu.disconnect()
        except Exception as e:
            pass
        try:
            await blv.disconnect()
        except Exception as e:
            pass
        try:
            await blw.disconnect()
        except Exception as e:
            pass
        try:
            await blx.disconnect()
        except Exception as e:
            pass
        try:
            await bly.disconnect()
        except Exception as e:
            pass
            await blz.disconnect()
        except Exception as e:
            pass
        try:
            await baa.disconnect()
        except Exception as e:
            pass
        try:
            await bab.disconnect()
        except Exception as e:
            pass
        try:
            await bac.disconnect()
        except Exception as e:
            pass
        try:
            await bad.disconnect()
        except Exception as e:
            pass
        try:
            await bae.disconnect()
        except Exception as e:
            pass
        try:
            await baf.disconnect()
        except Exception as e:
            pass
        try:
            await bag.disconnect()
        except Exception as e:
            pass
        try:
            await bah.disconnect()
        except Exception as e:
            pass
            await bai.disconnect()
        except Exception as e:
            pass
        try:
            await baj.disconnect()
        except Exception as e:
            pass
        try:
            await bak.disconnect()
        except Exception as e:
            pass
        try:
            await bal.disconnect()
        except Exception as e:
            pass
        try:
            await bam.disconnect()
        except Exception as e:
            pass
            await ban.disconnect()
        except Exception as e:
            pass
        try:
            await bao.disconnect()
        except Exception as e:
            pass
        try:
            await bap.disconnect()
        except Exception as e:
            pass
        try:
            await baq.disconnect()
        except Exception as e:
            pass
        try:
            await bar.disconnect()
        except Exception as e:
            pass
            await bas.disconnect()
        except Exception as e:
            pass
        try:
            await bat.disconnect()
        except Exception as e:
            pass
        try:
            await bau.disconnect()
        except Exception as e:
            pass
        try:
            await bav.disconnect()
        except Exception as e:
            pass
        try:
            await baw.disconnect()
        except Exception as e:
            pass
        try:
            await bax.disconnect()
        except Exception as e:
            pass
                                                               

            
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

        
@bla.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blb.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.help"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.help"))


async def help(e):
    if e.sender_id in BLAZEA_USERS:
       text = "| 𝐓 𝐄 𝐀 𝐌 • ‌«[ 𝐁𝐋𝐀𝐙𝐄]»𝙁𝙄𝙂𝙃𝙏𝙀𝙍𝙎★➤➤♛✘ ๛ :\n#𝗕𝗟𝗔𝗭𝗘_𝗦𝗣𝗔𝗠𝗠𝗘𝗥\nᎪ𝚅Ꭺ𝙸ᏞᎪ𝙱Ꮮ𝙴  ᏟᎾ𝙼𝙼ᎪᏁᎠ𝚂\n\n#𝗨𝗧𝗜𝗟𝗦_𝗖𝗢𝗠𝗠𝗔𝗡𝗗:\n.𝙿ᎥᏁᎶ\n.Ꮢ𝚎𝚜𝚃𝚊𝚛𝚃\n\n#𝙐𝙨𝙚𝙧𝙗𝙤𝙩_𝘾𝙤𝙢𝙢𝙖𝙣𝙙:\n.𝙱𝙸𝙾\n.𝙹𝙾𝙸𝙽\n.𝙿𝙹𝙾𝙸𝙽\n.𝙻𝙴𝙰𝚅𝙴\n\n#𝗦𝗣𝗔𝗠_𝗖𝗢𝗠𝗠𝗔𝗡𝗗:\n.𝚂𝙿𝙰𝙼\n.𝙳𝙴𝙻𝙰𝚈𝚂𝙿𝙰𝙼\n.𝙱𝙸𝙶𝚂𝙿𝙰𝙼\n.𝚁𝙰𝙸𝙳\n.𝚁𝙴𝙿𝙻𝚈𝚁𝙰𝙸𝙳\n.𝙳𝚁𝙴𝙿𝙻𝚈𝚁𝙰𝙸𝙳\n\n#𝗕𝗟𝗔𝗭𝗘_𝗦𝗣𝗔𝗠𝗠𝗘𝗥\n ғσя мσяε #нεℓρ #яεgαя∂ιηg υsαgε σғ #ρℓυgιηs түρε ρℓυgιηs #ηαмεs"
    await e.reply(text, parse_mode=None, link_preview=None )


@blb.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blc.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bld.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@ble.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blf.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blg.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blh.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bli.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blj.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blk.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bll.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blm.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bln.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blo.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blp.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blq.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blr.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bls.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blt.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blu.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blv.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blw.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blx.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bly.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@blz.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@baa.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bab.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bac.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bad.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bae.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@baf.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bag.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bah.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bai.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@baj.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bak.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bal.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bam.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@ban.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bao.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bap.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@baq.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bar.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bas.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bat.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bau.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bav.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@baw.on(events.NewMessage(incoming=True, pattern=r"\.repo"))
@bax.on(events.NewMessage(incoming=True, pattern=r"\.repo"))


async def repo(e):
    if e.sender_id in BLAZEA_USERS:
        start = datetime.now()
        text = "★★вℓαᘔε ηε✞ሠᎾяᏦ★★"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱ \n➤ 𝐃𝐄𝐏𝐋𝐎𝐘 𝐓𝐎 50 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓𝐒 𝐈𝐍 𝐎𝐍 𝐓𝐌𝐄...\n➤ 𝗣𝗢𝗪𝗘𝗥𝗘𝗗 𝗕𝗬 :- [#𝗧𝗛𝗘_𝗕𝗟𝗔𝗭𝗘_𝗡𝗘𝗧𝗪𝗢𝗥𝗞](https://t.me/BLAZE_SPAMMER)\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n ┏━━━━━━━━━━━━━━━━━━━━━\n ┣➤∆ 𝚅𝙴𝚁𝚈 𝙵𝙰𝚂𝚃 𝚂𝙿𝙰𝙼...\n ┣    ∆ 𝙽𝙾𝙽 𝚂𝚃𝙾𝙿 𝚂𝙿𝙰𝙼...    \n ┣ 🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰\n ┣\n ┣ ┈ ➤  🔱   [𝗥𝗘𝗣𝗢](https://github.com/TEAM-BLAZ/BLAZE-SPAMMER-ROBOT)      \n ┣      \n ┣  ┈➤  🔱   [𝗦𝗧𝗥𝗜𝗡𝗚](https://replit.com/@BLAZE-NETWORK/BLAZE-SPAMMER)\n ┣\n ┗━━━━━━━━━━━━━━━━━━━━━")



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
    try:
        blv.disconnect()
    except Exception as e:
        pass
    try:
        blw.disconnect()
    except Exception as e:
        pass
    try:
        blx.disconnect()
    except Exception as e:
        pass
    try:
        bly.disconnect()
    except Exception as e:
        pass
    try:
        blz.disconnect()
    except Exception as e:
        pass    
    try:
        baa.disconnect()
    except Exception as e:
        pass
    try:
        bab.disconnect()
    except Exception as e:
        pass
    try:
        bac.disconnect()
    except Exception as e:
        pass
    try:
        bad.disconnect()
    except Exception as e:
        pass
    try:
        bae.disconnect()
    except Exception as e:
        pass    
    try:
        baf.disconnect()
    except Exception as e:
        pass
    try:
        bag.disconnect()
    except Exception as e:
        pass
    try:
        bah.disconnect()
    except Exception as e:
        pass
    try:
        bai.disconnect()
    except Exception as e:
        pass    
    try:
        baj.disconnect()
    except Exception as e:
        pass
    try:
        bak.disconnect()
    except Exception as e:
        pass
    try:
        bal.disconnect()
    except Exception as e:
        pass
    try:
        bam.disconnect()
    except Exception as e:
        pass
    try:
        ban.disconnect()
    except Exception as e:
        pass    
    try:
        bao.disconnect()
    except Exception as e:
        pass
    try:
        bap.disconnect()
    except Exception as e:
        pass
    try:
        baq.disconnect()
    except Exception as e:
        pass
    try:
        bar.disconnect()
    except Exception as e:
        pass
    try:
        bas.disconnect()
    except Exception as e:
        pass    
    try:
        bat.disconnect()
    except Exception as e:
        pass
    try:
        bau.disconnect()
    except Exception as e:
        pass
    try:
        bav.disconnect()
    except Exception as e:
        pass
    try:
        baw.disconnect()
    except Exception as e:
        pass
    try:
        bax.disconnect()
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
    try:
        blv.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blw.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blx.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bly.run_until_disconnected()
    except Exception as e:
        pass
    try:
        blz.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baa.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bab.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bac.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bad.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bae.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baf.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bag.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bah.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bai.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baj.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bak.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bal.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bam.run_until_disconnected()
    except Exception as e:
        pass
    try:
        ban.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bao.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bap.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baq.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bar.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bas.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bat.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bau.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bav.run_until_disconnected()
    except Exception as e:
        pass
    try:
        baw.run_until_disconnected()
    except Exception as e:
        pass
    try:
        bax.run_until_disconnected()
    except Exception as e:
        pass
    
