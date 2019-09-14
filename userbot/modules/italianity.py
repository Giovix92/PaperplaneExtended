# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
#
""" Userbot module for having some fun with people. """

import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from userbot import CMD_HELP
from userbot.events import register, errors_handler

# ================= CONSTANT =================

BESTEMMIE = [
    "Porco dio",
    "Puttana la madonna",
    "Gesu' btrfs",
    "madonna maiala",
    "dio cane",
    "madonna zoccola",
    "gesu' scemo",
    "giuseppe bastardo",
    "madonna pompinara",
    "madonna murata",
    "dio obeso",
    "cristo slabbrato",
    "dio zoppo",
    "dio ladro",
    "dio cristo",
    "gesucchia",
    "madonna troia",
    "gesu' bestia",
    "gesu' script",
    "dio programmatore",
    "madonna tester",
    "gesu' tastiera",
    "dio merda",
    "dio canaglia",
    "cristo gamer",
    "giuseppe cornuto",
    "Dio giasen",
    "Dio mido",
    "Madonna tissot",
    "Dio giovix",
]

FRASI = [
    "Ollà, son duri sti gnocchetti eh",
    "Ma io che cazzo ne so scusi",
    "Beh, veda un po' lei",
    "Io zappo la vigna, voi che facete?",
    "CENDODIGIOTTOOOOOOO",
    "130 SI VOLAAAA",
    "Eh, volevi!",
    "Io sono giapponese",
    "Sono Enrico Pasquale Pratticò",
    "OSANNA AL CRISTO SIGNOR",
]

# ===========================================

@register(outgoing=True, pattern="^.bestemmia$")
@errors_handler
async def bstmmia(bestemmia):
    """ Tira un porcone anche tu! """
    if not bestemmia.text[0].isalpha() and bestemmia.text[0] not in ("/", "#", "@", "!"):
        await bestemmia.edit(random.choice(BESTEMMIE))

@register(outgoing=True, pattern="^.frase$")
@errors_handler
async def fraseita(frase):
    """ Spara qualche frase pure tu. """
    if not frase.text[0].isalpha() and frase.text[0] not in ("/", "#", "@", "!"):
        await frase.edit(random.choice(FRASI))


CMD_HELP.update({
    "italianity":
    ".bestemmia\
\nUso: Ti servirà in casi estremi.\
\n\n.frase\
\nUso: Sputa fuori alcune delle frasi italiane piu' famose."
})

