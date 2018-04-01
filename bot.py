#testbot

from random import randint
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix="va-")

@bot.event
async def on_ready():
    print("READY")
    print("ID: " + bot.user.id)
    print("NAME: " + bot.user.name)

@bot.command(pass_context=True)
async def boti(ctx):
    embed = discord.Embed(title="valle-bot info", description="Current version made 2018-03-23 (Version 1.2)", color=0x42e5f4)
    embed.add_field(name="Made with :heart: in :flag_se: by VertaUser", value="Environment: discord.py")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def number(ctx):
    embed = discord.Embed(title="Random number", description=randint(0,99999), color=0x42e5f4)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def usri(ctx, user: discord.Member):
    embed = discord.Embed(title="{}s stats".format(user.name), description="I found this (i hope the info is correct. :fingers_crossed:)", color=0x21bef2)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Join date", value=user.joined_at)
    embed.add_field(name="Rank", value=user.top_role)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def rndclr(ctx):
    embed = discord.Embed(title="Random color", description=randint(0,255), color=0x42e5f4)
    await bot.say(embed=embed)


bot.run(token)
