import os
import json
import discord
from discord import app_commands
from dotenv import load_dotenv
import aiohttp

load_dotenv()

client = discord.Client(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print("ready")

@tree.command(name="kick", description="kick player")
async def kick(interaction: discord.Interaction, player: str, reason: str = "none"):
    await interaction.response.defer()

    async with aiohttp.ClientSession() as session:
        resp = await session.post(
            f"https://apis.roblox.com/messaging-service/v1/universes/{os.getenv('ROBLOX_UNIVERSE_ID')}/topics/rolink",
            headers={"x-api-key": os.getenv("ROBLOX_API_KEY"), "Content-Type": "application/json"},
            json={"message": json.dumps({"command": "kick", "args": {"target": player, "reason": reason}})}
        )
    
    text = f"kicked **{player}**" if resp.status == 200 else "Failed to kick.."
    
    await client.http.request(
        discord.http.Route("POST", f"/webhooks/{interaction.application_id}/{interaction.token}"),
        json={"flags": 32768, "components": [{"type": 17, "components": [{"type": 10, "content": text}]}]}
    )

@tree.command(name="ban", description="ban player")
async def ban(interaction: discord.Interaction, player: str, reason: str = "none", seconds: int = -1, ban_alts: bool = True):
    await interaction.response.defer()

    async with aiohttp.ClientSession() as session:
        resp = await session.post(
            f"https://apis.roblox.com/messaging-service/v1/universes/{os.getenv('ROBLOX_UNIVERSE_ID')}/topics/rolink",
            headers={"x-api-key": os.getenv("ROBLOX_API_KEY"), "Content-Type": "application/json"},
            json={"message": json.dumps({"command": "ban", "args": {"target": player, "reason": reason, "seconds": seconds, "ban_alts": ban_alts}})}
        )
    
    text = f"banned **{player}**" if resp.status == 200 else "Failed to ban.."

    await client.http.request(
        discord.http.Route("POST", f"/webhooks/{interaction.application_id}/{interaction.token}"),
        json={"flags": 32768, "components": [{"type": 17, "components": [{"type": 10, "content": text}]}]}
    )

if __name__ == "__main__":
    client.run(os.getenv("DISCORD_TOKEN"))
