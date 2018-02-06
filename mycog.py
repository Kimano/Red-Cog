import discord
from discord.ext import commands
from enum import Enum
import random

class Mycog:

    def __init__(self, bot):
        self.bot = bot
        self.heroes = buildHeroTables(self)

    @commands.command(pass_context=True)
    async def hero(self, ctx, user: discord.Member=None):
        if(user is None):
            user = ctx.message.author
        name,hero = selectHero(self.heroes)
        await self.bot.say(user.mention + " got " + name);

def setup(bot):
    bot.add_cog(Mycog(bot))

def selectHero(heroes):
    return random.choice(list(heroes.items()))
    
def buildHeroTables(self):
    heroes = dict()
    #Strength Heroes
    heroes["Abbadon"]=Hero("Abbadon",MainStat.STRENGTH,True,True)
    heroes["Alchemist"]=Hero("Alchemist",MainStat.STRENGTH,True,False)
    heroes["Axe"]=Hero("Axe",MainStat.STRENGTH,True,True)
    heroes["Beastmaster"]=Hero("Beastmaster",MainStat.STRENGTH,True,True)
    heroes["Brewmaster"]=Hero("Brewmaster",MainStat.STRENGTH,True,True)
    heroes["Bristleback"]=Hero("Bristleback",MainStat.STRENGTH,True,True)
    #Agility Heroes
    
    #Intelligence Heroes
    return heroes

class Hero:
    def __init__(self, name, mainStat, melee, hasAghs):
        self.name = name
        self.mainStat = mainStat
        self.melee = melee
        self.hasAghs = hasAghs
        
    def isMelee():
        return melee
        
    def isRanged():
        return not melee
    
class Item:
    def __init__(self, name, cost, active):
        self.name = name
        self.cost = cost
        self.active = active
        
class MainStat(Enum):
    STRENGTH=1
    AGILITY=2
    INTELLIGENCE=3