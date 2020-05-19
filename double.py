from discord.ext import commands
import json
import time

client = commands.Bot(command_prefix = 'dt-')

# on_ready event
@client.event
async def on_ready():
    print("Bot online!")

@client.command()
async def stop(ctx):
    await ctx.send("okhaije")
    exit()

@client.event
async def on_message(message):

    if "Double" in message.content:
        try:
            await message.channel.send("Trouble! <@465662909645848577> <@464733215903580160>")
        except:
            time.sleep(120)
            await message.channel.send("Trouble! <@465662909645848577> <@464733215903580160>")
    else:
        pass

with open("token.json") as file:
    main = json.load(file)
client.run(main['double'])