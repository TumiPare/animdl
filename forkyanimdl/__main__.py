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
from .core.cli.commands.grab import animdl_grab
from .core.cli.commands.download import animdl_download
from .core.cli.commands.schedule import animdl_schedule
from .core.cli.commands.search import animdl_search
from .core.cli.commands.stream import animdl_stream
from .core.cli.commands.update import animdl_update
# import download, grab, schedule, search, stream, update
from .core.cli.helpers import stream_handlers


def grab(name, episode, provider, index = 1):
    animdl_grab(name,index,provider,range=episode)

def download(name, episode, provider, folder_path, latest = False):
    animdl_download(name,1,provider,range=episode)

def schedule(name, episode, provider):
    pass

def search(name, episode, provider):
    pass

def stream(name, episode, provider):
    pass

def update(name, episode, provider):
    pass



if __name__ == "__main__":
    grab("One Piece", 100, "allanime")
