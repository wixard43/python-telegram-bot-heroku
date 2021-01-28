from telethon.sync import TelegramClient, events
import re, asyncio, random


api_id = 2922953
api_hash = "0ea7dab322f598e9a1aeb64cac8cc1ab"


global allow
allow = False


print ('Trying to connect telegram')
with TelegramClient ("untao", api_id, api_hash) as client:
    print ("Connected to telegram")
    @client.on (events.NewMessage (chats = -408117409) )
    async def withdHandler (event):
        global allow
        if '/g_withdraw' in event.raw_text:
            await event.forward_to ("@chtwrsbot")
            allow = True

    @client.on (events.NewMessage (chats = "@chtwrsbot") )
    async def recHandler (event):
        global allow
        if 'Collector of Dragonscale' in event.raw_text and allow:
            await event.forward_to (-408117409)
            allow = False

    client.run_until_disconnected ()
