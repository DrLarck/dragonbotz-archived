"""
Box command

--

Author : Drlarck

Last update : 07/04/20 by DrLarck
"""

from discord.ext import commands

# util
from utility.command.checker import CommandChecker
from utility.entity.player import Player
from utility.global_tool import GlobalTool

# tool
from utility.command.tool.tool_box import ToolBox


class CommandBox(commands.Cog):

    def __init__(self, client):
        # Public
        self.client = client

    @commands.check(CommandChecker.game_ready)
    @commands.check(CommandChecker.register)
    @commands.command()
    async def box(self, context, rarity: str = None):
        # Log
        await self.client.logger.log(context)
        
        # Init
        player = Player(self.client, context.message.author)
        box_tool = ToolBox(self.client, context)
        global_tool = GlobalTool()

        # Normal box
        if rarity is None:
            await box_tool.box_manager(player)

        else:
            # Get the rarity value
            value = await global_tool.get_rarity_value(rarity)

            if value is not None:
                await box_tool.box_manager(player, rarity=value)

            else:
                await context.send(f"Sorry, but I can't find the rarity `{rarity}`")


def setup(client):
    client.add_cog(CommandBox(client))