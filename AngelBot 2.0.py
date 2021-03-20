import discord
from discord.ext import commands
import random
import gspread

#intents = discord.Intents.default()
bot = commands.Bot(command_prefix = 'a!')
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Angel Bot 2.0 is ready!")

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello! ᕙ(^▿^-ᕙ)")
    
    @commands.command()
    async def ily(self, ctx, *, user: discord.Member=None):
        if(user == None):
            await ctx.send("I love you too, " + ctx.author.display_name + "! o(〃＾▽＾〃)o")
        else:
            await ctx.send("I love you, " + user.nick + "! o(〃＾▽＾〃)o")

    @commands.command(pass_context=True)
    async def hasAdmin(self, ctx):
        member = discord.Member.bot
        if(member.hasPermission("ADMINISTRATOR")):
           print("Bot is an admin")

bot.add_cog(Random(bot))
TOKEN = 'TOKEN'
bot.run(TOKEN)
