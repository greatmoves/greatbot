import discord
import random
import json
import os

from discord.ext import commands
from hewwwo import hewwwo
from cip import encrypt, decrypt
from rps import res
from prntsc_disc import getimage, randurl
from reddit import caller
from helpcommand import create_help

client = commands.Bot(command_prefix='!', help_command=None, owner_id=)

@client.event
async def on_ready():
    print('Bot is running.')


@client.command(hidden = True, enabled = False)
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def reddit(ctx, *, subreddit):
    async with ctx.typing():
        embed = caller(str(subreddit), ctx.channel.is_nsfw())
    await ctx.send(embed=embed)


@reddit.error
async def test_on_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is currently on cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        await ctx.send("Please try a different subreddit, or try again in a NSFW channel.")

@client.command()
async def help(ctx):
    avatar_url = (client.user.avatar_url)
    async with ctx.typing():
        embed = create_help(avatar_url)
    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user)
async def prnt(ctx):
    async with ctx.typing():
        embed = getimage()
    await ctx.send(embed = embed)

@prnt.error
async def test_on_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is currently on cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

@client.command()  # Vigenère cipher commands
async def vc(ctx, key, *, plaintext):
    plaintext = plaintext.replace(" ", "")
    ciphertext = encrypt(plaintext, key.upper())
    await ctx.send("Your encrypted text is: " + str(ciphertext) + ' with the key: ' + str(key) + '.')


@vc.error
async def test_on_error(ctx, error):
    await ctx.send(
        f'{"You need a key and a plaintext to use a Vigenère Cipher!"}' " <@{}>".format(ctx.message.author.id))


@client.command()
async def dc(ctx, key, *, ciphertext):
    ciphertext = ciphertext.replace(" ", "")
    plaintext = decrypt(ciphertext, key.upper())
    await ctx.send("Your decrypted text is: " + str(plaintext) + ' with the key: ' + str(key) + '.')


@dc.error
async def test_on_error(ctx, error):
    await ctx.send(
        f'{"You need a key and a ciphertext to use a Vigenère Cipher!"}' " <@{}>".format(ctx.message.author.id))


@client.command()  # rock paper scissors
@commands.cooldown(1, 15, commands.BucketType.user)
async def rps(ctx, play):
    async with ctx.typing():
        message = res(play.lower()) + " <@{}>".format(ctx.message.author.id)
    await ctx.send(message)


@rps.error
async def test_on_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This command is currently on cooldown, please try again in {:.2f}s'.format(error.retry_after)
        await ctx.send(msg)
    else:
        await ctx.send("You need to play either rock, paper or scissors. That's how the game works...")


@client.command(aliases=['ht'])
async def _ht(ctx):
    responses = ['Heads!', 'Tails!']
    await ctx.send(f'{random.choice(responses)}' " <@{}>".format(ctx.message.author.id))


@client.command(hidden = True, enabled = False)
async def echo(ctx, *, message):
    await ctx.send(f'{message}')


@client.command()
async def uwu(ctx, *, message):
    await ctx.send(f'{hewwwo(message)}')


@client.command(aliases=["heck", "meme"], hidden = True, enabled = False)  # just here to remind myself that aliases exist
async def test(ctx, *, message1):
    print(message1)

client.run('BOTTOKEN')
