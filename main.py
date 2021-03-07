import discord
import base64
import requests
import json


class myClient(discord.Client):
  # Coroutine to login
    async def on_ready(self):
        print(f'Howdy 👋 ! Logged in as {client.user}'.format(client))

  # Coroutine to answer messages
    async def on_message(self, ctx):
        if ctx.author == client.user:
            return
        elif ctx.content.startswith('annen mess'):
            async def get_joke(self):
                response = requests.get('https://api.chucknorris.io/jokes/random')
                joke = json.loads(response.text)
                return(joke['value'].replace('Chuck Norris', 'Annen'))
            the_joke = await get_joke(self)
            await ctx.channel.send(the_joke)
        elif 'anna' in ctx.content.lower() or 'annen' in ctx.content.lower():
            await ctx.channel.send('🔥🔥🔥')


# This class is used to interact with the Discord WebSocket and API.
client = myClient()
# Bot login using the token
token = base64.b64decode('T0RFMU9ETTBPREkxT1RneE9ESXdPVEk0LllEeUxZdy5XQmo3T2lJWml4UzZDdmtpeS1TeDBNbTZlT28=').decode('utf-8')
print(token)
client.run(token)
