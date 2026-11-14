import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot("!", intents=intents)

@bot.event
async def on_ready():
    print("Bot On")

@bot.event
async def on_message(msg:discord.Message):
    canal = bot.get_channel(1555946350967787600)
    await bot.process_commands()
    if msg.author.bot:
        return
    await msg.reply("a")

@bot.event
async def on_guild_channel_create(canal:discord.abc.GuildChannel):
    await canal.send(f"O canal {canal.name} foi criado!")

@bot.event
async def on_member_join(member:discord.Member):
    canal = bot.get_channel(1555946350967787600)
    await canal.send(f"{member.display_name} entrou no servidor")

@bot.event
async def on_member_remove(member:discord.member):
    canal = bot.get_channel(1555946350967787600)
    await canal.send(f"{member.display_name} saiu do servidor\nAté logo!")

@bot.command()
async def ola(ctx:commands.Context):
   usuario = ctx.author
   await ctx.send(f"Olá {usuario.display_name}.")
    
@bot.command()
async def enviar_embed(ctx:commands.Context):
    my_embed = discord.Embed(title='Hello, World', description='Descrição massa :D')

    my_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCkYZjAsXyFgG-ic2Pi0o3Cmgxsqo4BRH-xMB0L_lxyg&s=10")

    imagem_arquivo = discord.File('imagens/imagem.jpg',filename='imagem.jpg')
    my_embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSYZHTUx5mY5SfEB6DgLK5DD_d5lfhv7ouuCnFmSILbA&s=10")

    await ctx.reply(embed=my_embed)
    
bot.run(DISCORD_TOKEN)