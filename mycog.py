import discord
from discord.ext import commands
from enum import Enum
import random

class Mycog:

    def __init__(self, bot):
        self.bot = bot
        buildHeroTables(self)
        buildItemsTables(self)

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
    
class Hero:
    def __init__(self, name, mainStat, melee, hasAghs, range):
        self.name = name
        self.mainStat = mainStat
        self.melee = melee
        self.range = range
        self.hasAghs = hasAghs
        
    def isMelee():
        return melee
        
    def isRanged():
        return not melee
    
class Item:
    def __init__(self, name, cost, tags):
        self.name = name
        self.cost = cost
        self.tags = tags
        
class MainStat(Enum):
    STRENGTH=1
    AGILITY=2
    INTELLIGENCE=3
    
class ItemTags(Enum):
    ACTIVE=1
    CONSUMABLE=2
    BOOTS=3
    DEFENSIVE=4
    OFFENSIVE=5
    MELEE=6
    RANGED=7
    
def buildHeroTables(self):
    heroes = dict()
    
    #Strength Heroes
    heroes["Abbadon"]=Hero("Abbadon",MainStat.STRENGTH,True,True,150)
    heroes["Alchemist"]=Hero("Alchemist",MainStat.STRENGTH,True,False,150)
    heroes["Axe"]=Hero("Axe",MainStat.STRENGTH,True,True,150)
    heroes["Beastmaster"]=Hero("Beastmaster",MainStat.STRENGTH,True,True,150)
    heroes["Brewmaster"]=Hero("Brewmaster",MainStat.STRENGTH,True,True,150)
    heroes["Bristleback"]=Hero("Bristleback",MainStat.STRENGTH,True,True,150)
    heroes["Centaur Warrunner"]=Hero("Centaur Warrunner",MainStat.STRENGTH,True,True,150)
    heroes["Chaos Knight"]=Hero("Chaos Knight",MainStat.STRENGTH,True,True,150)
    heroes["Clockwerk"]=Hero("Clockwerk",MainStat.STRENGTH,True,True,150)
    heroes["Doom"]=Hero("Doom",MainStat.STRENGTH,True,True,150)
    heroes["Dragon Knight"]=Hero("Dragon Knight",MainStat.STRENGTH,True,False,150)
    heroes["Earth Spirit"]=Hero("Earth Spirit",MainStat.STRENGTH,True,True,150)
    heroes["Earthshaker"]=Hero("Earthshaker",MainStat.STRENGTH,True,True,150)
    heroes["Elder Titan"]=Hero("Elder Titan",MainStat.STRENGTH,True,True,150)
    heroes["Huskar"]=Hero("Huskar",MainStat.STRENGTH,False,True,400)
    heroes["Io"]=Hero("Io",MainStat.STRENGTH,False,True,575)
    heroes["Kunkka"]=Hero("Kunkka",MainStat.STRENGTH,True,True,150)
    heroes["Legion Commander"]=Hero("Legion Commander",MainStat.STRENGTH,True,True,150)
    heroes["Lifestealer"]=Hero("Lifestealer",MainStat.STRENGTH,True,True,150)
    heroes["Lycan"]=Hero("Lycan",MainStat.STRENGTH,True,False,150)
    heroes["Magnus"]=Hero("Magnus",MainStat.STRENGTH,True,True,150)
    heroes["Night Stalker"]=Hero("Night Stalker",MainStat.STRENGTH,True,True,150)
    heroes["Omniknight"]=Hero("Omniknight",MainStat.STRENGTH,True,True,150)
    heroes["Phoenix"]=Hero("Phoenix",MainStat.STRENGTH,False,True,500)
    heroes["Pudge"]=Hero("Pudge",MainStat.STRENGTH,True,True,150)
    heroes["Sand King"]=Hero("Sand King",MainStat.STRENGTH,True,True,150)
    heroes["Slardar"]=Hero("Slardar",MainStat.STRENGTH,True,False,150)
    heroes["Spirit Breaker"]=Hero("Spirit Breaker",MainStat.STRENGTH,True,True,150)
    heroes["Sven"]=Hero("Sven",MainStat.STRENGTH,True,True,150)
    heroes["Tidehunter"]=Hero("Tidehunter",MainStat.STRENGTH,True,True,150)
    heroes["Timbersaw"]=Hero("Timbersaw",MainStat.STRENGTH,True,True,150)
    heroes["Tiny"]=Hero("Tiny",MainStat.STRENGTH,True,False,150)
    heroes["Treant Protector"]=Hero("Treant Protector",MainStat.STRENGTH,True,True,150)
    heroes["Tusk"]=Hero("Tusk",MainStat.STRENGTH,True,True,150)
    heroes["Underlord"]=Hero("Underlord",MainStat.STRENGTH,True,False,150)
    heroes["Undying"]=Hero("Undying",MainStat.STRENGTH,True,True,150)
    heroes["Wraith King"]=Hero("Wraith King",MainStat.STRENGTH,True,True,150)
    #Agility Heroes
    heroes["Anti-Mage"]=Hero("Anti-Mage",MainStat.AGILITY,True,True,150)
    heroes["Arc Warden"]=Hero("Arc Warden",MainStat.AGILITY,False,False,625)
    heroes["Bloodseeker"]=Hero("Bloodseeker",MainStat.AGILITY,True,True,150)
    heroes["Bounty Hunter"]=Hero("Bounty Hunter",MainStat.AGILITY,True,True,150)
    heroes["Broodmother"]=Hero("Broodmother",MainStat.AGILITY,True,False,150)
    heroes["Clinkz"]=Hero("Clinkz",MainStat.AGILITY,False,False,640)
    heroes["Drow Ranger"]=Hero("Drow Ranger",MainStat.AGILITY,False,True,625)
    heroes["Ember Spirit"]=Hero("Ember Spirit",MainStat.AGILITY,True,False,150)
    heroes["Faceless Void"]=Hero("Faceless Void",MainStat.AGILITY,True,True,150)
    heroes["Gyrocopter"]=Hero("Gyrocopter",MainStat.AGILITY,False,True,365)
    heroes["Juggernaut"]=Hero("Juggernaut",MainStat.AGILITY,True,True,150)
    heroes["Lone Druid"]=Hero("Lone Druid",MainStat.AGILITY,False,True,550)
    heroes["Luna"]=Hero("Luna",MainStat.AGILITY,False,True,330)
    heroes["Medusa"]=Hero("Medusa",MainStat.AGILITY,False,True,600)
    heroes["Meepo"]=Hero("Meepo",MainStat.AGILITY,True,True,150)
    heroes["Mirana"]=Hero("Mirana",MainStat.AGILITY,False,True,630)
    heroes["Monkey King"]=Hero("Monkey King",MainStat.AGILITY,True,False,300)
    heroes["Morphling"]=Hero("Morphling",MainStat.AGILITY,False,False,350)
    heroes["Naga Siren"]=Hero("Naga Siren",MainStat.AGILITY,True,True,150)
    heroes["Nyx Assassin"]=Hero("Nyx Assassin",MainStat.AGILITY,True,True,150)
    heroes["Pangolier"]=Hero("Pangolier",MainStat.AGILITY,True,False,150)
    heroes["Phantom Assassin"]=Hero("Phantom Assassin",MainStat.AGILITY,True,False,150)
    heroes["Phantom Lancer"]=Hero("Phantom Lancer",MainStat.AGILITY,True,True,150)
    heroes["Razor"]=Hero("Razor",MainStat.AGILITY,False,True,475)
    heroes["Riki"]=Hero("Riki",MainStat.AGILITY,True,True,150)
    heroes["Shadow Fiend"]=Hero("Shadow Fiend",MainStat.AGILITY,False,True,500)
    heroes["Slark"]=Hero("Slark",MainStat.AGILITY,True,True,150)
    heroes["Sniper"]=Hero("Sniper",MainStat.AGILITY,False,True,550)
    heroes["Spectre"]=Hero("Spectre",MainStat.AGILITY,True,False,150)
    heroes["Templar Assassin"]=Hero("Templar Assassin",MainStat.AGILITY,False,False,140)
    heroes["Terrorblade"]=Hero("Terrorblade",MainStat.AGILITY,True,False,150)
    heroes["Troll Warlord"]=Hero("Troll Warlord",MainStat.AGILITY,True,False,150)
    heroes["Ursa"]=Hero("Ursa",MainStat.AGILITY,True,True,150)
    heroes["Vengeful Spirit"]=Hero("Vengeful Spirit",MainStat.AGILITY,True,True,150)
    heroes["Venomancer"]=Hero("Venomancer",MainStat.AGILITY,False,True,450)
    heroes["Viper"]=Hero("Viper",MainStat.AGILITY,False,True,575)
    heroes["Weaver"]=Hero("Weaver",MainStat.AGILITY,False,True,425)
    #Intelligence Heroes
    heroes["Ancient Apparition"]=Hero("Ancient Apparition",MainStat.INTELLIGENCE,False,True,675)
    heroes["Bane"]=Hero("Bane",MainStat.INTELLIGENCE,False,True,400)
    heroes["Batrider"]=Hero("Batrider",MainStat.INTELLIGENCE,False,True,375)
    heroes["Chen"]=Hero("Chen",MainStat.INTELLIGENCE,False,True,650)
    heroes["Crystal Maiden"]=Hero("Crystal Maiden",MainStat.INTELLIGENCE,False,True,600)
    heroes["Dark Seer"]=Hero("Dark Seer",MainStat.INTELLIGENCE,True,True,150)
    heroes["Dark Willow"]=Hero("Dark Willow",MainStat.INTELLIGENCE,False,False,475)
    heroes["Dazzle"]=Hero("Dazzle",MainStat.INTELLIGENCE,False,True,550)
    heroes["Death Prophet"]=Hero("Death Prophet",MainStat.INTELLIGENCE,False,False,600)
    heroes["Disruptor"]=Hero("Disruptor",MainStat.INTELLIGENCE,False,True,600)
    heroes["Enchantress"]=Hero("Enchantress",MainStat.INTELLIGENCE,False,True,550)
    heroes["Enigma"]=Hero("Enigma",MainStat.INTELLIGENCE,False,True,500)
    heroes["Invoker"]=Hero("Invoker",MainStat.INTELLIGENCE,False,True,600)
    heroes["Jakiro"]=Hero("Jakiro",MainStat.INTELLIGENCE,False,True,400)
    heroes["Keeper of the Light"]=Hero("Keeper of the Light",MainStat.INTELLIGENCE,False,True,600)
    heroes["Leshrac"]=Hero("Leshrac",MainStat.INTELLIGENCE,False,True,600)
    heroes["Lich"]=Hero("Lich",MainStat.INTELLIGENCE,False,True,550)
    heroes["Lina"]=Hero("Lina",MainStat.INTELLIGENCE,False,True,670)
    heroes["Lion"]=Hero("Lion",MainStat.INTELLIGENCE,False,True,600)
    heroes["Nature's Prophet"]=Hero("Nature's Prophet",MainStat.INTELLIGENCE,False,True,600)
    heroes["Necrophos"]=Hero("Necrophos",MainStat.INTELLIGENCE,False,True,550)
    heroes["Ogre Magi"]=Hero("Ogre Magi",MainStat.INTELLIGENCE,True,True,150)
    heroes["Oracle"]=Hero("Oracle",MainStat.INTELLIGENCE,False,True,620)
    heroes["Outworld Devourer"]=Hero("Outworld Devourer",MainStat.INTELLIGENCE,False,True,450)
    heroes["Puck"]=Hero("Puck",MainStat.INTELLIGENCE,False,True,550)
    heroes["Pugna"]=Hero("Pugna",MainStat.INTELLIGENCE,False,True,630)
    heroes["Queen of Pain"]=Hero("Queen of Pain",MainStat.INTELLIGENCE,False,True,550)
    heroes["Rubick"]=Hero("Rubick",MainStat.INTELLIGENCE,False,True,550)
    heroes["Shadow Demon"]=Hero("Shadow Demon",MainStat.INTELLIGENCE,False,True,500)
    heroes["Shadow Shaman"]=Hero("Shadow Shaman",MainStat.INTELLIGENCE,False,True,400)
    heroes["Silencer"]=Hero("Silencer",MainStat.INTELLIGENCE,False,True,600)
    heroes["Skywrath Mage"]=Hero("Skywrath Mage",MainStat.INTELLIGENCE,False,True,600)
    heroes["Storm Spirit"]=Hero("Storm Spirit",MainStat.INTELLIGENCE,False,True,480)
    heroes["Techies"]=Hero("Techies",MainStat.INTELLIGENCE,False,True,700)
    heroes["Tinker"]=Hero("Tinker",MainStat.INTELLIGENCE,False,True,500)
    heroes["Visage"]=Hero("Visage",MainStat.INTELLIGENCE,False,True,600)
    heroes["Warlock"]=Hero("Warlock",MainStat.INTELLIGENCE,False,True,600)
    heroes["Windranger"]=Hero("Windranger",MainStat.INTELLIGENCE,False,True,600)
    heroes["Winter Wyvern"]=Hero("Winter Wyvern",MainStat.INTELLIGENCE,False,True,425)
    heroes["Witch Doctor"]=Hero("Witch Doctor",MainStat.INTELLIGENCE,False,True,600)
    heroes["Zeus"]=Hero("Zeus",MainStat.INTELLIGENCE,False,True,350)
    
    self.heroes = heroes
    
def buildItemTables(self):
    items = dict()
    boots = dict()
    
    items["Moon Shard"]=Item("Moon Shard", 4000, [ItemTags.CONSUMABLE])
    
    boots["Guardian Greaves"]=Item("Guardian Greaves",5350, [ItemTags.BOOTS, ItemTags.ACTIVE])
    boots["Power Treads"]=Item("Power Treads",1350, [ItemTags.BOOTS])
    boots["Phase Boots"]=Item("Phase Boots",1240, [ItemTags.BOOTS, ItemTags.ACTIVE])
    boots["Tranquil Boots"]=Item("Tranquil Boots",950, [ItemTags.BOOTS])
    boots["Boots of Travel"]=Item("Boots of Travel",4400, [ItemTags.BOOTS, ItemTags.ACTIVE])
    
    self.items = items
    self.boots = boots