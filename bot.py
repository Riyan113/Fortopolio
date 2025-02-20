import discord
import openai

# Token dari Discord Developer Portal
DISCORD_TOKEN = "MTM0MjEzNTc1MjM5NzQyNjgwMA.GshACD.bUnHnzllS2CxUK-48tJ_G90KGwCiLvDT4U79ZI"
OPENAI_API_KEY = "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"

# Konfigurasi OpenAI
openai.api_key = OPENAI_API_KEY

# Inisialisasi bot
intents = discord.Intents.default()
intents.messages = True  # Supaya bot bisa membaca pesan
bot = discord.Client(intents=intents)
@bot.event
async def on_ready():
    print(f'Bot {bot.user} sudah online!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message.content}]
    )
    await message.channel.send(response["choices"][0]["message"]["content"])

bot.run(DISCORD_TOKEN)
