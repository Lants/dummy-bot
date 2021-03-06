# Developer commands and tools for kasa baby bot

from nextcord.ext import commands
import random

class Development(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    #------------------------------------------COMMANDS------------------------------------------

    # !sleep
    # Close connection to Discord
    @commands.command(name = "sleep", description = "\"Put me to sleep!\"")
    @commands.check_any(commands.has_permissions(administrator = True), commands.is_owner())
    async def sleep(self, ctx):
        if random.random() < .5:
            await ctx.channel.send("nighty night! I go sleep now " + str(ctx.author.mention))
        else:
            await ctx.channel.send("aw, it's not my bedtime yet " + str(ctx.author.mention) + "! fine.. goodnight!")
        await ctx.bot.close()

    # !echo <string>   
    # Echo back input. Used for testing.
    @commands.command(name = "echo", description = "Echoes back input. Used for testing.")
    @commands.check_any(commands.has_permissions(administrator = True), commands.is_owner())
    async def echo(self, ctx, *, args: str):
        await ctx.send(args)


    #---------------------------------- COG FEATURES -----------------------------------------------
    # !load <cogname>
    # Loads an inactive cog
    @commands.command(name = 'load', description = "Load specificed Cog.")
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
    async def _load(self, ctx, *, module: str):
        """Loads a module."""
        try:
            module = 'cogs.' + module
            self.bot.load_extension(module)
        except Exception as e:
            await ctx.send("Could not load extension. Uhhh ask Lance for help lmao")
        else:
            await ctx.send("Loaded: " + module)

    # !unload <cogname>
    # Unloads an active cog
    @commands.command(name = 'unload', description = "Unload specificed Cog.")
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
    async def _unload(self, ctx, *, module: str):
        """Unloads a module."""
        try:
            module = 'cogs.' + module
            self.bot.unload_extension(module)
        except Exception as e:
            await ctx.send("Could not unload extension. Uhhh ask Lance for help lmao")
        else:
            await ctx.send("Unloaded: " + module)

    # !reload <cogname>
    # Reloads an active cog
    @commands.command(name = 'reload', description = "Reload specificed Cog.")
    @commands.check_any(commands.is_owner(), commands.has_permissions(administrator = True))
    async def _reload(self, ctx, *, module: str):
        """Reloads a module."""
        try:
            module = 'cogs.' + module
            self.bot.reload_extension(module)
        except Exception as e:
            await ctx.send("Could not reload extension. Uhhh ask Lance for help lmao")
        else:
            await ctx.send("Reloaded: " + module)

    # !channelType
    # Prints type of channel that the command is used from
    @commands.command(name = 'channelType', description = 'Prints type of channel that the command is used from')
    async def channelType(self, ctx):
        # await ctx.send(isinstance(ctx.channel, discord.channel.DMChannel))
        await ctx.send(ctx.channel.type)

    #-------------------------------------------COMMAND ERROR HANDLING-----------------------------------------------    
    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("uhh.. ur not good enough to do this sorry")
        
    @sleep.error    
    async def sleep_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Only my parents can make make me go to bed! (Admins only dummy)")
        
        
        
def setup(bot):
    bot.add_cog(Development(bot))        
        
        