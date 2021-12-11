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

from typing import List


def check_message(
    Log: object, message: object, messageIDs: List, Static: object, Notify: object
) -> bool:

    # Avoid checking messages from before program start, or that have already been
    # checked
    if message.created_utc < Static.START_TIME or message.id in messageIDs:
        return False

    messageIDs.append(message.id)

    if (
        message.body.split(Static.SPLITTER)[0] in Static.MESSAGES
        and message.author.name in Static.AUTHORS
    ):

        # Declaring these variables saves on API requests and speeds up program a lot.
        # They'll be deleted later on to ensure memory is saved, because I don't know
        # whether or not Python does that for you.
        parent = message.parent()
        parentBody = parent.body.casefold()

        # Haven't tried re-replying; try.
        if parentBody == "done":
            del parent, parentBody
            return True

        # Have tried re-replying; there's a problem.
        elif parentBody == Static.REPLY:
            Notify.Notification.new("Problematic post found.").show()
            Log.new(f"Problematic post at: {parent.url}", "INFO")
            del parent, parentBody
            return False