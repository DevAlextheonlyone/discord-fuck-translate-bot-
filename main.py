import discord
import os
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
translator = Translator()

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.content.lower().startswith("translate "):
        return

    text = message.content[len("translate "):].strip()
    if not text:
        return

    try:
        translated = translator.translate(
            text,
            src="sv",
            dest="en"
        ).text

        await message.delete()
        await message.channel.send(
            f"🇸🇪 **{message.author.display_name}:** {text}\n"
            f"🇬🇧 {translated}"
        )

    except Exception as e:
        print("Translation error:", e)

client.run(os.getenv("DISCORD_TOKEN"))
