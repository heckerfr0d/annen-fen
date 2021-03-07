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
        elif ctx.content.lower().startswith('annen hits'):
            user = ctx.author
            v = user.voice
            if v != None:
                vc = await v.channel.connect()
                random.seed()
                patt = os.path.join('hits', random.choice(os.listdir('hits')))
                vc.play(discord.FFmpegPCMAudio(source=patt))
                while vc.is_playing():
                    await asyncio.sleep(1)
                await vc.disconnect()
            else:
                await ctx.channel.send('Eda paadan pattnne edenklum keredaa')
        elif 'anna' in ctx.content.lower():
            await ctx.channel.send('anna uyir🔥🔥')
        elif 'annen' in ctx.content.lower():
            await ctx.channel.send('annen kidu😏🔥🔥')


# This class is used to interact with the Discord WebSocket and API.
client = myClient()
# Bot login using the token
token = base64.b64decode('T0RFMU9ETTBPREkxT1RneE9ESXdPVEk0LllEeUxZdy5XQmo3T2lJWml4UzZDdmtpeS1TeDBNbTZlT28=').decode('utf-8')
client.run(token)
