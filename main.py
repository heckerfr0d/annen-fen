#!/usr/bin/python3
import discord
import requests
import json
import os, random

class myClient(discord.Client):
  # Coroutine to login
    async def on_ready(self):
        print(f'Logged in as {client.user}'.format(client))
        await client.change_presence(activity=discord.Streaming(name="Coco Cola Pepsi Seyuj Annen Sesky", url="https://www.youtube.com/watch?v=_olVbRl-fJU"))

  # Coroutine to answer messages
    async def on_message(self, ctx):

        # recursion baad
        if ctx.author == client.user:
            return

        elif ctx.content.lower().startswith('anna ithenth my'):
            embed = discord.Embed(title="Annen Fen 😎️", description="Born of Annen's mess", color=ctx.author.color)
            embed.add_field(name="annen mess", value="Exhilarating tales from the Legends of Annen", inline=False)
            embed.add_field(name="annen hits", value='Mesmerizing "hiphop songs" in Annen\'s original voice', inline=False)
            embed.add_field(name="anna roast @loser", value="Equivalent to saying anna theerthekk (brutally destroy the loser)", inline=False)
            await ctx.channel.send(embed=embed)

        # annen mess ka baap
        elif ctx.content.lower().startswith('annen mess'):
            await ctx.add_reaction('🔥')
            async def get_fect(self):
                response = requests.get('https://api.chucknorris.io/jokes/random')
                fect = json.loads(response.text)
                truFect = fect['value'].replace("Chuck Norris'", "Annen's").replace("Norris'", "Annen's").replace('Chuck Norris', 'Annen').replace('Chuck', 'Annen').replace('Norris', 'Annen')
                return(truFect)
            messFect = await get_fect(self)
            embed = discord.Embed(title="🔥 Annen 🔥", description=messFect, color=ctx.author.color)
            await ctx.channel.send(embed=embed)

        # harimuraleeeeeeeeravammmm
        elif ctx.content.lower().startswith('annen hits'):
            await ctx.add_reaction('😍')
            if not ctx.author.voice:
                await ctx.channel.send('Eda paadan pattnne edenklum keredaa')
            else:
                if not client.voice_clients or client.voice_clients[0].channel != ctx.author.voice.channel:
                    vc = await ctx.author.voice.channel.connect()
                else:
                    vc = client.voice_clients[0]
                random.seed()
                patt = os.path.join('hits', random.choice(os.listdir('hits')))
                vc.play(discord.FFmpegPCMAudio(source=patt))
                while vc.is_playing():
                    try:
                        msg = await client.wait_for('message', timeout=3.0)
                        if msg.content.lower().startswith("anna next"):
                            patt = os.path.join('hits', random.choice(os.listdir('hits')))
                            vc.stop()
                            vc.play(discord.FFmpegPCMAudio(source=patt))
                    except:
                        pass
                await vc.disconnect()

        # krual annen
        elif ctx.content.lower().startswith('anna roast'):
            data = requests.get('https://evilinsult.com/generate_insult.php?lang=en&amp;type=json').content.decode()
            mentioned = ctx.author
            for user in ctx.mentions:
                mentioned = user
            await ctx.delete()
            await ctx.channel.send(mentioned.mention+' '+data)

        # annen mind aakkum 😌️
        elif 'anna' in ctx.content.lower():
            await ctx.add_reaction('💪')
        elif 'annen' in ctx.content.lower():
            await ctx.add_reaction('🔥')


# This class is used to interact with the Discord WebSocket and API.
client = myClient()
# Bot login using the token
token = os.getenv('ANNEN')
client.run(token)
