import discord
from discord import message
from discord.ext import commands
import random
import time

from discord.member import Member

client = commands.Bot(command_prefix="do ")


def shootP():
    @client.command()
    async def shoot(ctx, member:discord.Member,* ,reason=None):
        actions = ["missed", "shot"]
        action = random.choice(actions)
        print(action)

        #missed
        if action == actions[0]:
            await ctx.send(f"Missed {member}")
        #killed
        if action == actions[1]:
            #deaths
            hurt = ["head", "chin", "elbow", "leg"]
            #randomize
            hurtC = random.choice(hurt)
            #tell how your about to die
            await ctx.send(f"{member} Got Shot In The " + hurtC)
            #brain
            if hurtC == hurt[0]:
                time.sleep(2)
                await ctx.send(f"{member} Is Dead")
                await member.kick(reason=reason)

            #chin
            if hurtC == hurt[1]:
                time.sleep(6)
                await ctx.send(f"{member} Is Dead")
                await member.kick(reason=reason)

            #elbow
            if hurtC == hurt[2]:
                time.sleep(35)
                await ctx.send(f"{member} Is Dead")
                await member.kick(reason=reason)

            #leg
            if hurtC == hurt[3]:
                time.sleep(31)
                await ctx.send(f"{member} Is Dead")
                await member.kick(reason=reason)


def runworld(token):
    client.run(token)

def GunReady():
    @client.event
    async def on_ready():
        print("Guns Ready!")
