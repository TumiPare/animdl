"""
A one cli for all the anime.
"""

import os
import random
import sys

# import click
# from rich.align import Align
# from rich.style import Style
# from rich.text import Text
# from rich.traceback import install

from .core import __version__
from .core.cli.commands import download, grab, schedule, search, stream, update
from .core.cli.helpers import stream_handlers

# install(show_locals=True, suppress=[click])

commands = {
    "download": download.animdl_download,
    "grab": grab.animdl_grab,
    "schedule": schedule.animdl_schedule,
    "search": search.animdl_search,
    "update": update.animdl_update,
    "stream": stream.animdl_stream,
}


# @click.group(commands=commands, invoke_without_command=True)
# @click.version_option(__version__.__core__, "--version")
# @click.option("-x", "--disable-update", is_flag=True, help="Disable update check.")
# @click.pass_context
def __animdl_cli__():
    pass

def get_link(name, episode, provider):
    grab.animdl_grab(name,1,provider,range=episode)

if __name__ == "__main__":
    get_link("One Piece", 100, "allanime")
