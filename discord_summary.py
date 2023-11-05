import os
import re
from datetime import datetime, timedelta

import discord
from discord.ext import commands

from chatgpt_call import get_summary

# Constants
CONTEXT_LOOKBACK_DAYS = 3
MESSAGE_CHUNK_SIZE = 1900

# Environment variables
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']
DISCORD_SUMMARY_BOT_TOKEN = os.environ['DISCORD_SUMMARY_BOT_TOKEN']

# Bot setup
bot = commands.Bot(command_prefix='/', intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')


@bot.command()
async def summary(ctx, time_period: str = "1d"):
    time_to_look_back = parse_time_to_look_back(time_period)
    time_to_look_back_for_context = datetime.utcnow() - timedelta(days=CONTEXT_LOOKBACK_DAYS)

    for channel in ctx.guild.text_channels:
        if channel.permissions_for(ctx.guild.me).read_messages and channel.name != "summary":
            await process_channel(channel, ctx, time_to_look_back, time_to_look_back_for_context)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        # This is a generic error handler, you can customize the message as needed
        await ctx.send(error.original)
    elif isinstance(error, commands.CommandError):
        await ctx.send(str(error))


# Helper functions

def parse_time_to_look_back(time_period):
    match = re.match(r'(\d+)([dhm])$', time_period)
    if not match:
        raise ValueError("Invalid time period format. Use '<number><d/h/m>' (e.g., '1d', '6h', '30m').")

    quantity, unit = match.groups()
    quantity = int(quantity)
    now = datetime.now()

    return {
        'd': now - timedelta(days=quantity),
        'h': now - timedelta(hours=quantity),
        'm': now - timedelta(minutes=quantity)
    }.get(unit, ValueError("Invalid time unit. Use 'd' for days, 'h' for hours, or 'm' for minutes."))


async def process_channel(channel, ctx, time_to_look_back, time_to_look_back_for_context):
    channel_messages = await get_channel_messages(channel, time_to_look_back)

    if channel_messages:
        channel_context = []
        async for msg in channel.history(after=time_to_look_back_for_context, before=time_to_look_back):
            if msg.author != bot.user and not msg.content.startswith("/"):
                channel_context.append(f"{msg.author.display_name}: {msg.content}")

        response = f"**<#{channel.id}>**\n"  # This makes the channel name clickable
        response += await get_summary("\n".join(channel_context), "\n".join(channel_messages))

        response_chunks = [response[i:i + MESSAGE_CHUNK_SIZE] for i in range(0, len(response), MESSAGE_CHUNK_SIZE)]
        for chunk in response_chunks:
            await ctx.send(chunk)


async def get_channel_messages(channel, time_to_look_back):
    channel_messages = []
    async for msg in channel.history(after=time_to_look_back):
        if msg.author != bot.user and not msg.content.startswith("/"):
            channel_messages.append(f"{msg.author.display_name}: {msg.content}")
    return channel_messages


bot.run(os.environ['DISCORD_SUMMARY_BOT_TOKEN'])
