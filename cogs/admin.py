from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import discord
from discord import Interaction, app_commands, ui
from discord.ext import commands

if TYPE_CHECKING:
    from bot import ValorantBot


class Admin(commands.Cog):
    """Error handler"""

    def __init__(self, bot: ValorantBot) -> None:
        self.bot: ValorantBot = bot

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, sync_type: Literal['guild', 'global']) -> None:
        """Sync the application commands"""

        async with ctx.typing():
            if sync_type == 'guild':
                self.bot.tree.copy_global_to(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Synced guild !")
                return

            await self.bot.tree.sync()
            await ctx.reply(f"Synced global !")

    @commands.command()
    @commands.is_owner()
    async def unsync(self, ctx: commands.Context, unsync_type: Literal['guild', 'global']) -> None:
        """Unsync the application commands"""

        async with ctx.typing():
            if unsync_type == 'guild':
                self.bot.tree.clear_commands(guild=ctx.guild)
                await self.bot.tree.sync(guild=ctx.guild)
                await ctx.reply(f"Un-Synced guild !")
                return

            self.bot.tree.clear_commands()
            await self.bot.tree.sync()
            await ctx.reply(f"Un-Synced global !")

    @app_commands.command(description='Shows basic information about the bot.')
    async def about(self, interaction: Interaction) -> None:
        """Shows basic information about the bot."""

        owner_url = f'https://discord.com/users/231680517538316289'
        github_project = 'https://github.com/xaynaver/Valorant-DiscordBot'
        support_url = 'https://instagram.com/nekonug._/'

        embed = discord.Embed(color=0x8000ff)
        embed.set_author(name='VALORANT BOT PROJECT', url=github_project)
        embed.set_thumbnail(url='https://i.pinimg.com/originals/10/4d/5f/104d5fcdae0f8fbbeb574d46425cd006.jpg')
        embed.add_field(name='ᴘʀᴏᴅ:', value=f"[xaynaver#7499]({owner_url})", inline=False)
        embed.add_field(name='ᴅᴇᴠ:', value=f"[ꜱᴛᴀᴄɪᴀ.#7475](https://discord.com/users/240059262297047041)", inline=False)
        embed.add_field(
            name='ᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ:',
            value=f"Discord bot that shows your Valorant infomation like store, night.market, points, mission and bundles.\n"
            "Use /login first for 2FA user or you can use /store directly for non 2FA user.\n"
            "Other commands /bundles /notify /battlepass /point /mission\n"
            "Made with love | rosie <3",
            inline=False,
        )
        view = ui.View()
        view.add_item(ui.Button(label='ɢɪᴛʜᴜʙ', url=github_project, row=0))
        view.add_item(ui.Button(label='ꜱᴀᴡᴇʀɪᴀ', url='https://saweria.co/xaynaver', row=0))
        view.add_item(ui.Button(label='ɪɴꜱᴛᴀɢʀᴀᴍ', url=support_url, row=0))

        await interaction.response.send_message(embed=embed, view=view)


async def setup(bot: ValorantBot) -> None:
    await bot.add_cog(Admin(bot))
