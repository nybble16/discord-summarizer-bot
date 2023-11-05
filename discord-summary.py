import asyncio
import concurrent.futures
import discord
import functools
import openai
from datetime import datetime, timedelta
from discord.ext import commands
import os

openai.api_key = os.environ['OPENAI_API_KEY']
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@functools.lru_cache(maxsize=100)
async def get_summary(messages_context, messages_in_channel):
    print("Getting summary for: " + messages_in_channel[:50])

    # Define the synchronous function for the API call
    def synchronous_api_call():
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "assistant",
                    "content": f"Oto kontekst rozmowy na czacie: \n\n{'-' * 10}\n{messages_context}\n{'-' * 10}\n\n>>> Poniżej znajduje się kontynuacja, i tę kontynuację chciałbym abyś streścił znając powyższy kontekst: \n\n\n{messages_in_channel}"
                }
            ]
        )
        return completion.choices[0].message.content

    # Run the synchronous function in a separate thread
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = await asyncio.get_event_loop().run_in_executor(executor, synchronous_api_call)

    return result


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.command()
async def summary(ctx, time_period: str = "1d"):
    if time_period == "debug":
        time_to_look_back = datetime.utcnow() - timedelta(hours=6)
    elif time_period == "6h":
        time_to_look_back = datetime.utcnow() - timedelta(hours=6)
    elif time_period == "1d":
        time_to_look_back = datetime.utcnow() - timedelta(days=1)
    else:
        await ctx.send("Invalid time period. Please use either '6h' or '1d'.")
        return

    time_to_look_back_for_context = datetime.utcnow() - timedelta(days=3)

    for channel in ctx.guild.text_channels:
        # not summary channel
        if channel.permissions_for(ctx.guild.me).read_messages and channel.name != "summary":
            channel_messages = []
            async for msg in channel.history(after=time_to_look_back):
                if msg.author != bot.user and not msg.content.startswith("/"):
                    channel_messages.append(f"{msg.author.display_name}: {msg.content}")

            if channel_messages:
                channel_context = []
                async for msg in channel.history(after=time_to_look_back_for_context, before=time_to_look_back):
                    if msg.author != bot.user and not msg.content.startswith("/"):
                        channel_context.append(f"{msg.author.display_name}: {msg.content}")

                response = f"**<#{channel.id}>**\n"  # This makes the channel name clickable
                response += await get_summary("\n".join(channel_context), "\n".join(channel_messages))

                response_chunks = [response[i:i + 1900] for i in range(0, len(response), 1900)]
                if time_period == "debug":
                    print(response_chunks)
                else:
                    for chunk in response_chunks:
                        await ctx.send(chunk)


bot.run(os.environ['DISCORD_SUMMARY_BOT_TOKEN'])