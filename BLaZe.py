import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from Config import STRING, SUDO, BIO_MESSAGE, API_ID, API_HASH, STRING2, STRING3, STRING4 ,STRING5, STRING6, STRING7, STRING8 ,STRING9, STRING10 
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

    if blazea:
        session_name = str(blazea)
        print("String 1 Found")
        bla = TelegramClient(StringSession(session_name), api, hash)
        try:
            print("Booting Up The Client 1")
            await bla.start()
            botme = await bla.get_me()
            await bla(functions.channels.JoinChannelRequest(channel="@BLAZE_SPAMMER"))
            await bla(functions.channels.JoinChannelRequest(channel="@BLAZE_ZONE"))           
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
