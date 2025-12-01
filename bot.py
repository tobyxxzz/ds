import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv
from typing import Union
from keep_alive import start

load_dotenv()

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

EMBED_COLOR = 0xFFFF00

RESOURCES = {
    "volcano": {
        "title": "Volcano",
        "url": "https://volcano.wtf/"
    },
    "delta": {
        "title": "Delta",
        "url": "https://deltaexploits.gg/"
    },
    "xeno": {
        "title": "Xeno",
        "url": "https://www.xeno.onl/"
    },
    "fluxus": {
        "title": "Fluxus",
        "url": "https://www.mediafire.com/file/6dynt8mfxyamioo/FluxusZ+64bits+V2.0.5.apk/file"
    },
    "deltadesync": {
        "title": "Delta Desync",
        "url": "https://www.mediafire.com/file/6wm1elae9o26o2c/DeltaDesyncWorks.apk/file"
    }
}

def create_embed(resource_key: str, user: Union[discord.User, discord.Member]) -> discord.Embed:
    resource = RESOURCES[resource_key]
    
    embed = discord.Embed(
        title=resource['title'],
        description=f"Obter link do executor {resource['title']}",
        color=EMBED_COLOR,
        timestamp=datetime.now()
    )
    
    embed.add_field(
        name="Link",
        value=f"[Clique aqui para acessar]({resource['url']})",
        inline=False
    )
    
    embed.set_footer(
        text=f"Solicitado por {user.display_name}",
        icon_url=user.display_avatar.url
    )
    
    return embed


@bot.event
async def on_ready():
    if bot.user is None:
        return
    print(f"{'='*50}")
    print(f"Bot conectado como: {bot.user}")
    print(f"ID do Bot: {bot.user.id}")
    print(f"Servidores conectados: {len(bot.guilds)}")
    print(f"{'='*50}")
    
    try:
        synced = await bot.tree.sync()
        print(f"Comandos slash sincronizados: {len(synced)}")
    except Exception as e:
        print(f"Erro ao sincronizar comandos: {e}")
    
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="por comandos | /help"
        )
    )


@bot.tree.command(name="volcano", description="Obter link do Volcano Executor")
async def volcano(interaction: discord.Interaction):
    try:
        embed = create_embed("volcano", interaction.user)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Ocorreu um erro ao processar o comando. Tente novamente.",
            ephemeral=True
        )
        print(f"Erro no comando /volcano: {e}")


@bot.tree.command(name="delta", description="Obter link do Delta Executor")
async def delta(interaction: discord.Interaction):
    try:
        embed = create_embed("delta", interaction.user)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Ocorreu um erro ao processar o comando. Tente novamente.",
            ephemeral=True
        )
        print(f"Erro no comando /delta: {e}")


@bot.tree.command(name="xeno", description="Obter link do Xeno Executor")
async def xeno(interaction: discord.Interaction):
    try:
        embed = create_embed("xeno", interaction.user)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Ocorreu um erro ao processar o comando. Tente novamente.",
            ephemeral=True
        )
        print(f"Erro no comando /xeno: {e}")


@bot.tree.command(name="fluxus", description="Obter link do Fluxus Z APK")
async def fluxus(interaction: discord.Interaction):
    try:
        embed = create_embed("fluxus", interaction.user)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Ocorreu um erro ao processar o comando. Tente novamente.",
            ephemeral=True
        )
        print(f"Erro no comando /fluxus: {e}")


@bot.tree.command(name="deltadesync", description="Obter link do Delta Desync APK")
async def deltadesync(interaction: discord.Interaction):
    try:
        embed = create_embed("deltadesync", interaction.user)
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Ocorreu um erro ao processar o comando. Tente novamente.",
            ephemeral=True
        )
        print(f"Erro no comando /deltadesync: {e}")


@bot.tree.command(name="help", description="Ver todos os comandos disponíveis")
async def help_command(interaction: discord.Interaction):
    try:
        embed = discord.Embed(
            title="Lista de Comandos",
            description="Aqui estao todos os comandos disponiveis:",
            color=EMBED_COLOR,
            timestamp=datetime.now()
        )
        
        commands_list = [
            ("/volcano", "Obter link do executor Volcano"),
            ("/delta", "Obter link do executor Delta"),
            ("/xeno", "Obter link do executor Xeno"),
            ("/fluxus", "Obter link do executor Fluxus"),
            ("/deltadesync", "Obter link do executor Delta Desync"),
            ("/help", "Ver esta lista de comandos")
        ]
        
        for cmd, desc in commands_list:
            embed.add_field(name=cmd, value=desc, inline=False)
        
        embed.set_footer(
            text=f"Solicitado por {interaction.user.display_name}",
            icon_url=interaction.user.display_avatar.url
        )
        
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        await interaction.response.send_message(
            f"❌ Ocorreu um erro ao processar o comando. Tente novamente.",
            ephemeral=True
        )
        print(f"Erro no comando /help: {e}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    print(f"Erro de comando: {error}")


@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        await interaction.response.send_message(
            f"⏳ Aguarde {error.retry_after:.2f} segundos antes de usar este comando novamente.",
            ephemeral=True
        )
    else:
        await interaction.response.send_message(
            "❌ Ocorreu um erro ao processar o comando. Tente novamente mais tarde.",
            ephemeral=True
        )
        print(f"Erro de app command: {error}")


def main():
    token = os.getenv("DISCORD_TOKEN")
    
    if not token:
        print("="*50)
        print("ERRO: Token do Discord não encontrado!")
        print("")
        print("Configure o token DISCORD_TOKEN nos Secrets:")
        print("1. Vá para a aba 'Secrets' no Replit")
        print("2. Adicione uma nova secret:")
        print("   - Key: DISCORD_TOKEN")
        print("   - Value: Seu token do bot Discord")
        print("")
        print("Para obter o token:")
        print("1. Acesse https://discord.com/developers/applications")
        print("2. Selecione ou crie uma aplicação")
        print("3. Vá em 'Bot' no menu lateral")
        print("4. Copie o token do bot")
        print("="*50)
        return
    
    try:
        print("Iniciando o bot...")
        start()
        bot.run(token)
    except discord.LoginFailure:
        print("="*50)
        print("ERRO: Token inválido!")
        print("Verifique se o token está correto nos Secrets.")
        print("="*50)
    except Exception as e:
        print(f"Erro ao iniciar o bot: {e}")


if __name__ == "__main__":
    main()
