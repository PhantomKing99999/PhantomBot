""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks

async def isQuestion(self, ctx):
    return ctx.channel.id == self.questionschannel

async def isVerify(self, ctx):
    return ctx.channel.id == self.verifychannel

async def isOutput(self, ctx):
    return ctx.channel.id == self.outputchannel


# Here we name the cog and create a new class for the cog.
class Questions(commands.Cog, name="questions"):
    def __init__(self, bot):
        self.bot = bot
        self.questionschannel: int
        self.verifychannel: int
        self.outputchannel: int

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
            name = "setquestion",
            description = "Sets the channel to the channel that accepts questions",
    )

    @checks.not_blacklisted()
    @checks.is_owner()

    async def setquestion(self, context: Context):
        self.questionchannel = context.channel.id

    
    @commands.hybrid_command(
            name = "setverify",
            description = "Aets the channel to the channel that is used to verify questions",
    )

    @checks.not_blacklisted()
    @checks.is_owner()

    async def setquestion(self, context: Context):
        self.verifychannel = context.channel.id


    @commands.hybrid_command(
            name = "setoutput",
            description = "Sets the channel to the channel that outputs questions",
    )

    @checks.not_blacklisted()
    @checks.is_owner()

    async def setquestion(self, context: Context):
        self.outputchannel = context.channel.id
    
    
    @commands.hybrid_command(
        name="question",
        description="Submits a question",
    )
    # This will only allow non-blacklisted members to execute the command
    @checks.not_blacklisted()
    # This will only allow owners of the bot to execute the command -> config.json
    #@checks.is_owner()
    @commands.check(isQuestion)

    @app_commands.describe(
        question="Enter the question you want to be asked"
    )

    async def question(self, context: Context, question: str):
        channel = self.bot.get_channel(self.verifychannel)
        embed = discord.Embed(
                description=f"**{context.author}'s** asked **'{question}'**!",
                color=0x9C84EF,
            )
        await channel.send(embed = embed)


# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot):
    await bot.add_cog(Questions(bot))
