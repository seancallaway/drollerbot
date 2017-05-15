#!/usr/bin/env python3
"""
    run.py
    ~~~~~~

    Runs the DRollerBot.

    :copyright: (c) 2017 by Sean Callaway.
    :license: MIT, see LICENSE for more details.
"""

from drollerbot import thebot
import config

thebot.run(config.BOT_USER_TOKEN)
