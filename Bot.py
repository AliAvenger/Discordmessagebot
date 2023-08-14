import discord
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
        print("Sent")
        print("------------------------")
        # channel id 
        user = await client.fetch_channel("")
                # text you want to send
        await user.send("")
        
    # file command    await user.send(file=discord.File('somo.jpg'))
    


client.run('')     


     
