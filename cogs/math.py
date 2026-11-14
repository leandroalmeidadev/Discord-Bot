import discord
from discord.ext import commands
from discord import app_commands

class Math(commands.Cog):
    def __init__(self, client:commands.Bot):
        self.client: commands.Bot = client

    @app_commands.command(
        name="soma",
        description="Somar dois numeros"
    )
    @app_commands.describe(
    num1="Primeiro número",
    num2="Segundo número"
    )
    async def soma(self,interaction:discord.Interaction,num1:int,num2:int):
        somar_numero = num1 + num2
        await interaction.response.send_message(f"A soma dos dois números é {somar_numero}")

async def setup(client:commands.Bot) -> None:
    await client.add_cog(Math(client))