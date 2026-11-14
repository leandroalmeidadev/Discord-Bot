#-------------------------------------------------------------------------------------------------------------------------------------------------
#Versão antiga
# import discord
# from discord.ext import commands

# intents = discord.Intents.all()
# bot = commands.Bot("!", intents=intents)

# @bot.event
# async def on_ready():
#     print("Bot On")

# # @bot.event
# # async def on_message(msg:discord.Message):
# #     canal = bot.get_channel(1555946350967787600)
# #     await bot.process_commands()
# #     if msg.author.bot:
# #         return
# #     await msg.reply("a")

# @bot.event
# async def on_guild_channel_create(canal:discord.abc.GuildChannel):
#     await canal.send(f"O canal {canal.name} foi criado!")

# @bot.event
# async def on_member_join(member:discord.Member):
#     canal = bot.get_channel(1555946350967787600)
#     await canal.send(f"{member.display_name} entrou no servidor")

# @bot.event
# async def on_member_remove(member:discord.member):
#     canal = bot.get_channel(1555946350967787600)
#     await canal.send(f"{member.display_name} saiu do servidor\nAté logo!")

# @bot.command()
# async def ola(ctx:commands.Context):
#    usuario = ctx.author
#    await ctx.send(f"Olá {usuario.display_name}.")

# @bot.command()
# async def enviar_embed(ctx:commands.Context):
#     my_embed = discord.Embed(title='Hello, World', description='Descrição massa :D')

#     my_embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTCkYZjAsXyFgG-ic2Pi0o3Cmgxsqo4BRH-xMB0L_lxyg&s=10")

#     # imagem_arquivo = discord.File('imagens/imagem.jpg',filename='imagem.jpg')
#     my_embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTSYZHTUx5mY5SfEB6DgLK5DD_d5lfhv7ouuCnFmSILbA&s=10")

#     await ctx.reply(embed=my_embed)
# bot.run("MTU1NTkxMDY5ODczODAwMDEzNA.Gy_2vN.kXpUFO2cEVJCpbJxuyh6lJmGbH9t7mhzT6OZyI")
#Versão antiga
#-------------------------------------------------------------------------------------------------------------------------------------------------
import discord
from discord import app_commands
from discord.ext import commands

from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
DISCORD_TOKEN= os.getenv("DISCORD_TOKEN")

if not DISCORD_TOKEN:
    raise ValueError("Token n encontrado no arquivo .env")

class MeuBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(
            command_prefix="+",
            intents = intents
        )
        #Função da proxima linha n é mais necessaria pois agora é: MeuBot(commands.Bot)
        # self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.load_extension("cogs.math")
        print("Cog carregado com sucesso")

        await self.tree.sync()

    async def on_ready(self):
        print(f"O Bot {self.user} foi inicializado")


bot = MeuBot()

#Excluir depois
# @bot.tree.command(name="soma",description="Somar")
# @app_commands.describe(
#     num1="Primeiro número",
#     num2="Segundo número"
# )
# async def soma_numero(interaction:discord.Interaction, num1:int, num2:int):
#     somar_numero = num1 + num2
#     await interaction.response.send_message(f"A soma dos dois números é {somar_numero}")

@bot.tree.command(name="olá-mundo",description="First command")
async def olamundo(interaction:discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}", ephemeral=True)

bot.run(DISCORD_TOKEN)