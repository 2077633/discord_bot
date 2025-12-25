import os

import discord
from dotenv import load_dotenv

load_dotenv()

# Voir le readme pour get le token.
TOKEN = os.getenv("DISCORD_TOKEN")

# Id des channels du discord
NOTIF_CHANNEL_ID_STR = os.getenv("NOTIF_CHANNEL_ID")

# User id de la personne qui recoit les messages du bot.
MY_USER_ID_STR = os.getenv("MY_USER_ID")

NOTIF_CHANNEL_ID = int(NOTIF_CHANNEL_ID_STR)
MY_USER_ID = int(MY_USER_ID_STR)

# Crée le client discord.
intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True
intents.members = True

client = discord.Client(intents=intents)

# Averti le user que le bot est connecté.
@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}.")
    await send_message(f"Bot activé")

# Detecte lorsque un user se connecte a un channel.
@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    if before.channel is None and after.channel is not None:
        await send_message(f"{member} a rejoint **{after.channel.name}**")

# Envoi un message au user_id spécifié sur discord.
async def send_message(message: str):
    owner = await client.fetch_user(MY_USER_ID)
    await owner.send(message)

client.run(TOKEN)
