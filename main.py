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
        activityvar = discord.Activity(type=discord.ActivityType.custom,state="Coco Cola Pepsi Seyuj Annen Sesky")
        await client.change_presence(activity=activityvar)

  # Coroutine to answer messages
    async def on_message(self, ctx):
        if ctx.author == client.user:
            return
        elif ctx.content.lower().startswith('annen mess'):
            async def get_fect(self):
                response = requests.get('https://api.chucknorris.io/jokes/random')
                fect = json.loads(response.text)
                truFect = fect['value'].replace('Chuck Norris', 'Annen').replace('Chuck', 'Annen').replace('Norris', 'Annen')
                return(truFect)
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
        elif ctx.content.lower().startswith('anna roast'):
            data = requests.get('https://evilinsult.com/generate_insult.php?lang=en&amp;type=json').content.decode()
            mentioned = ctx.author
            for user in ctx.mentions:
                mentioned = user
            await ctx.delete()
            await ctx.channel.send(mentioned.mention+' '+data)
        elif 'anna' in ctx.content.lower():
            await ctx.add_reaction('💪')
            for emoji in ctx.guild.emojis:
                await ctx.add_reaction(str(emoji))
        elif 'annen' in ctx.content.lower():
            await ctx.add_reaction('🔥')


# This class is used to interact with the Discord WebSocket and API.
client = myClient()
# Bot login using the token
token = base64.b64decode('T0RFMU9ETTBPREkxT1RneE9ESXdPVEk0LllEeUxZdy5XQmo3T2lJWml4UzZDdmtpeS1TeDBNbTZlT28=').decode('utf-8')
client.run(token)
