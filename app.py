import discord
import asyncio
import random
import time

client = discord.Client()

@client.event
async def on_ready():
    print ( 'DARK BOT' )  

@client.event
async def on_message(message):


    if message.channel == client.get_channel('467041118178246657'):
            await client.add_reaction(message, "👍")
            await client.add_reaction(message, "👎")
    

    if message.content.lower().startswith('d!moeda'):
      choice = random.randint(1,2)
      if choice == 1:
          await client.add_reaction(message, '😁')
      if choice == 2:
          await client.add_reaction(message, '👑')
          
    if message.content.lower().startswith('d!ping'):
        timep = time.time()
        emb = discord.Embed(title = 'Aguarde...', color = 0x000000)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        pingm1 = discord.Embed(title = 'Pong!', description = ':ping_pong: Ping - %.01f segundos' % ping, color=0x000000)
        await client.edit_message(pingm0, embed=pingm1)

    if message.content.lower().startswith('d!avatar'):
        try:
            usuario = message.mentions[0]
            avatarembed = discord.Embed(
                title="",
                color=0x000000,
                description="**[Clique aqui]("+ usuario.avatar_url +") para baixar o avatar de {}!**".format(usuario.name))
            avatarembed.set_author(name=message.author.name)
            avatarembed.set_image(url=usuario.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)
        except:
            avatarembed = discord.Embed(
                title="",
                color=0x000000,
                description="**[Clique aqui]("+ message.author.avatar_url +") para baixar seu avatar!**")
            avatarembed.set_author(name=message.author.name)
            avatarembed.set_image(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=avatarembed)

client.run('NDY3NzE3MzU2OTk1NjA4NTg2.DivZAg.lXlm1r4HFK1Z2nDcCfPknWc-0jk')