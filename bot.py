# BOT.py
import os
import datetime
from helper import load_webpage
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_TOKEN')

BOT = commands.Bot(command_prefix='$')

MERCHANTS = {} 

@BOT.event
async def on_ready():
    print(f'{BOT.user.name} has connected to Discord!')

@BOT.command(name='ListMerchants')
async def list_merchants(ctx):
    channel = BOT.get_channel(int(CHANNEL_ID))
    merchants = '\n'.join(map(str, MERCHANTS.items())) if MERCHANTS else "None"
    await channel.send(f'List Found Merchants: \n{merchants}')

@tasks.loop(minutes=1.0, count=None)
async def my_background_task():
    if datetime.datetime.now().minute not in range(30,40):
        MERCHANTS = {}
        return

    channel = BOT.get_channel(int(CHANNEL_ID))
    for merchant in load_webpage():
        if len(merchant) > 3:
            if (merchant_name := merchant[0]) not in MERCHANTS:
                MERCHANTS[merchant_name] = merchant
                await channel.send(f'New Merchant Found: {merchant}')

my_background_task.start()

BOT.run(TOKEN)