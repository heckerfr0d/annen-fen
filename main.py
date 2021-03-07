#!/usr/bin/python3
import discord
import base64
import requests
import json
import asyncio
import os, random

class myClient(discord.Client):
  # Coroutine to login
    async def on_ready(self):
        print(f'Logged in as {client.user}'.format(client))

  # Coroutine to answer messages
    async def on_message(self, ctx):
        if ctx.author == client.user:
            return
        elif ctx.content.lower().startswith('annen mess'):
            async def get_fect(self):
                response = requests.get('https://api.chucknorris.io/jokes/random')
                fect = json.loads(response.text)
                return(fect['value'].replace('Chuck Norris', 'Annen'))
            messFect = await get_fect(self)
            await ctx.channel.send(messFect)
        elif 'anna' in ctx.content.lower():
            await ctx.channel.send('anna uyir🔥🔥')
        elif 'annen' in ctx.content.lower():
            await ctx.channel.send('annen kidu😏🔥🔥')
        elif ctx.content.lower().startswith('annen hits'):
            user = ctx.message.author
            vc = user.voice.voice_channel
            if vc != None:
                vc1 = await client.join_voice_channel(vc)
                patt = random.choice(os.listdir('hits'))
                player = vc1.create_ffmpeg_player(patt, after=lambda: print('done'))
                player.start()
                while not player.is_done():
                    await asyncio.sleep(1)
                # disconnect after the player has finished
                player.stop()
                await vc1.disconnect()
            else:
                await client.say('Eda paadan pattnne edenklum keredaa')


# This class is used to interact with the Discord WebSocket and API.
client = myClient()
# Bot login using the token
token = base64.b64decode('T0RFMU9ETTBPREkxT1RneE9ESXdPVEk0LllEeUxZdy5XQmo3T2lJWml4UzZDdmtpeS1TeDBNbTZlT28=').decode('utf-8')
client.run(token)
