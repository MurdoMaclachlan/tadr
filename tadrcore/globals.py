"""
    Copyright (C) 2021-present, Murdo B. Maclachlan

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <https://www.gnu.org/licenses/>.
    
    Contact me at murdo@maclachlans.org.uk
"""

from os import environ, makedirs
from os.path import expanduser, isdir
from sys import platform
from time import time
from typing import Dict, NoReturn

global Globals, VERSION
VERSION = "2.0.0-alpha-20211210"


# Contains all static vars
class Static:
    def __init__(self) -> NoReturn:
        self.AUTHORS = ["transcribersofreddit"]
        self.DEBUG = False
        self.LIMIT = 10
        self.LOG_UPDATES = False
        self.MESSAGES = ["Sorry; I can't find your transcript post on the link"]
        self.OS = platform
        self.PATHS = self.define_paths(expanduser("~"), self.OS)
        self.REPLY = "done -- this was an automated action; please contact me with any questions."
        self.SLEEP = 10
        self.SPLITTER = "."
        self.START_TIME = time()
        self.VERBOSE = True
        self.VERSION = VERSION

    # Defines save paths for config and data based on the user's OS
    def define_paths(self, home: str, os: str) -> Dict[str, str]:
        """Detects OS and defines the appropriate save paths for the config and data.
        Exits on detecting an unspported OS. Supported OS's are: Linux, MacOS, Windows.

        Arguments:
        - home (string)
        - os (string)

        Returns: a string dict containing the newly defined save paths
        """
        os = "".join(list(os)[:3])

        # Route for a supported operating system
        if os in ["dar", "lin", "win"]:

            paths = (
                {
                    "config": environ["APPDATA"] + "\\tadr",
                    "data": environ["APPDATA"] + "\\tadr\data"
                } if os == "win" else {
                    "config": f"{home}/.config/tadr",
                    "data": f"{home}/.tadr/data"
                }
            )

            # Create any missing paths/directories
            for path in paths:
                if not isdir(paths[path]):
                    print(f"DEBUG: Making path: {paths[path]}")
                    makedirs(path, exist_ok=True)
            return paths

        # Exit if the operating system is unsupported
        else:
            print(f"FATAL: Unsupported operating system: {os}, exiting.")
            exit()


Globals = Static()