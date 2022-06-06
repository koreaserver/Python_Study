import discord
from discord_buttons_plugin import *
from discord.ext import commands
import asyncio
import re
import requests
from bs4 import BeautifulSoup

TOKEN = 'TOKEN'

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='~')
buttons = ButtonsClient(bot)

@bot.event
async def on_ready():
  print(f'{bot.user} 실행')

@bot.command()
async def 판매(ctx, product, price):
  await ctx.send('@here {}님께서 {}을 {}원에 판매중입니다.'.format(ctx.author.display_name, product, price))

  await buttons.send(
    content = "거래방을 만드시겠습니까?",
    channel = ctx.channel.id,
    components = [
      ActionRow([
        Button(
          label="예", 
          style=ButtonType().Success,
          custom_id="button_create_trade_room"
        )
      ])
    ]
  )

@buttons.click
async def button_create_trade_room(ctx):
  await ctx.reply('거래방이 만들어졌습니다.')

bot.run(TOKEN)