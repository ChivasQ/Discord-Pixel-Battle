import discord
from PIL import Image
from discord.ext import commands

from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


@bot.event
async def on_ready():
    print('hi')

@bot.command()
async def NewPainting(ctx, sizex, sizey):
    im = Image.new('RGB', (int(sizex) * 10, int(sizey) * 10), '#FFFFFF')
    im.save('painting.png')
    await ctx.message.delete()
    await ctx.send(file=discord.File("painting.png"))

@bot.command()
async def SetPixel(ctx, x, y, color):
    im = Image.open('painting.png')
    if color.lower() == 'red':
        pixel = Image.open('colors/RED.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'r-o':
        pixel = Image.open('colors/R-O.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'orange':
        pixel = Image.open('colors/ORANGE.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'y-o':
        pixel = Image.open('colors/Y-O.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'yellow':
        pixel = Image.open('colors/YELLOW.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'y-g':
        pixel = Image.open('colors/Y-G.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'green':
        pixel = Image.open('colors/GREEN.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'b-g':
        pixel = Image.open('colors/B-G.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'blue':
        pixel = Image.open('colors/BLUE.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'b-p':
        pixel = Image.open('colors/B-P.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'purple':
        pixel = Image.open('colors/PURPLE.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'p-r':
        pixel = Image.open('colors/R-P.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'white':
        pixel = Image.open('colors/WHITE.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    elif color.lower() == 'black':
        pixel = Image.open('colors/BLACK.png')
        im.paste(pixel, (int(x) * 10, int(y) * 10))
        im.save('painting.png')
    await ctx.message.delete()
    await ctx.send(file=discord.File("painting.png"))


bot.run(settings['token'])
