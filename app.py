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

    if message.content.startswith('d!serverinfo'):
        
			user = message.author.name
        
			horario = datetime.datetime.now().strftime("%H:%M:%S")
        
			serverinfo_embed = discord.Embed(title="\n", description="Abaixo est· as informaÁoes principais do servidor!", color=0x000000)
			serverinfo_embed.set_thumbnail(url=message.server.icon_url)
			serverinfo_embed.set_footer(text="{} ï {}".format(user, horario))
			serverinfo_embed.add_field(name=":trident:Nome:", value=message.server.name, inline=True)
			serverinfo_embed.add_field(name=":high_brightness:Dono:", value=message.server.owner.mention)
			serverinfo_embed.add_field(name=":id:ID:", value=message.server.id, inline=True)
			serverinfo_embed.add_field(name=":fleur_de_lis:Cargos:", value=len(message.server.roles), inline=True)
			serverinfo_embed.add_field(name=":high_brightness:Canais de texto:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.text]), inline=True)
			serverinfo_embed.add_field(name=":high_brightness:Canais de voz:", value=len([message.channel.mention for channel in message.server.channels if channel.type==discord.ChannelType.voice]), inline=True)
			serverinfo_embed.add_field(name=":family_mwbb:Membros:", value=len(message.server.members), inline=True)
			serverinfo_embed.add_field(name=":robot:Bots:", value=len([user.mention for user in message.server.members if user.bot]), inline=True)        
			serverinfo_embed.add_field(name=":calendar_spiral:Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"), inline=True)
			serverinfo_embed.add_field(name=":map:Regi„o:", value=str(message.server.region).title(), inline=True)
			await client.send_message(message.channel,embed=serverinfo_embed)

    if message.content.startswith('d!userinfo'):       
            
            user = message.mentions[0]
            
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            
            userinfo_embed = discord.Embed(title="\n", description="Abaixo est· as informaÁoes do usuario!", color=0x000000)
            userinfo_embed.set_thumbnail(url=message.author.avatar_url)
            userinfo_embed.set_footer(text="{} ï {}".format(user, horario))            
            userinfo_embed.add_field(name=":trident:Nome:", value=user.name, inline=True)
            userinfo_embed.add_field(name=":id:ID:", value=user.id, inline=True)
            userinfo_embed.add_field(name=":fleur_de_lis:Cargos:", value=len(user.roles), inline=True)
            userinfo_embed.add_field(name=":high_brightness:Status:", value=user.status, inline=True)
            userinfo_embed.add_field(name=':video_game:Jogando:', value=user.game, inline=True)                    
            userinfo_embed.add_field(name=":calendar_spiral:Criou a conta em:", value=user.created_at.strftime("%d %b %Y %H:%M"), inline=True) 
            userinfo_embed.add_field(name=":calendar_spiral:Entrou no servirdor em:", value=user.joined_at.strftime("%d %b %Y %H:%M"), inline=True)        
            await client.send_message(message.channel, embed=userinfo_embed)
		except:
		    user = message.author.name
		    
			horario = datetime.datetime.now().strftime("%H:%M:%S")
            
            userinfo_embed = discord.Embed(title="\n", description="Abaixo est· as informaÁoes do usuario!", color=0x000000)
            userinfo_embed.set_thumbnail(url=message.author.avatar_url)
            userinfo_embed.set_footer(text="{} ï {}".format(user, horario))            
            userinfo_embed.add_field(name=":trident:Nome:", value=message.author.name, inline=True)
            userinfo_embed.add_field(name=":id:ID:", value=message.author.id, inline=True)
            userinfo_embed.add_field(name=":fleur_de_lis:Cargos:", value=len(message.author.roles), inline=True)
            userinfo_embed.add_field(name=":high_brightness:Status:", value=message.author.status, inline=True)
            userinfo_embed.add_field(name=':video_game:Jogando:', value=message.author.game, inline=True)                    
            userinfo_embed.add_field(name=":calendar_spiral:Criou a conta em:", value=message.author.created_at.strftime("%d %b %Y %H:%M"), inline=True) 
            userinfo_embed.add_field(name=":calendar_spiral:Entrou no servirdor em:", value=message.author.joined_at.strftime("%d %b %Y %H:%M"), inline=True)        
            await client.send_message(message.channel, embed=userinfo_embed)

    if message.channel == client.get_channel('467041118178246657'):
            await client.add_reaction(message, "üëç")
            await client.add_reaction(message, "üëé")
    
    
    if message.content.lower().startswith('d!moeda'):
      choice = random.randint(1,2)
      if choice == 1:
          await client.add_reaction(message, 'üòÅ')
      if choice == 2:
          await client.add_reaction(message, 'üëë')
          
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
            


client.run('NDY3NzE3MzU2OTk1NjA4NTg2.DiurQA.4PZ7BLNTz98UDiVGpq3bz0spNCc')