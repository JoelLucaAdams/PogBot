import discord
from discord import *
from discord.ext import commands
from discord.ext.commands import Context
import time
import os
import random


class Utilities(commands.Cog):
    """
    General Utilities
    """

    @commands.command()
    async def ping(self, ctx: Context):
        """
        Status check
        """
        start_time = time.time()
        message = await ctx.send('pong. `DWSPz latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms`')
        end_time = time.time()
        await message.edit(content='pong. `DWSP latency: ' + str(round(ctx.bot.latency * 1000)) + 'ms` ' +
                                   '`Response time: ' + str(int((end_time - start_time) * 1000)) + 'ms`')

    @commands.command()
    async def source(self, ctx: Context):
        """
        Print a link to the source code
        """
        await ctx.send(content='Created by `Joel Adams`\n'
                               'https://github.com/JoelLucaAdams/PogBot')

    @commands.command()
    async def pog(self, ctx: Context):
        """
        Responds with random message
        """
        await ctx.message.delete()
        pogMessages = ['you pogged?', 'Once you pog you just can\'t stop', 'Pogging bells, pogging bells, pogging all the way', 'You just tested positive for pog', 'Certified Poggers Moment™️']
        embed = Embed(title='POGGERS!', description=pogMessages[random.randint(0, len(pogMessages)-1)], color=discord.Colour.green())
        embed.set_footer(icon_url=ctx.author.avatar_url, text= f'Requested by {ctx.author.display_name}')
        await ctx.send(embed=embed)

    @commands.command()
    async def image(self, ctx: Context):
        """
        sends a random image from the great pog wars
        """
        files = os.listdir('./Poggers')
        index = random.randint(0, len(files))    
        await ctx.send(file= File(f'./Poggers/{files[index]}'))
