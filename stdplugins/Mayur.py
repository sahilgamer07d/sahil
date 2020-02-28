"""use cmd .mayur
aaahaaa you can edit this 😉"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "Sahil":

        await event.edit(input_str)

        animation_chars = [

            
            "👑Sahil👑👑👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️◼️️👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️◼️◼️👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "‎◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Sahil👑👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Sahil👑👑Sahil👑◼️◼️\n◼️👑Sahil👑👑Sahil👑👑Sahil👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Sahil👑👑Sahil👑◼️◼️\n◼️👑Sahil👑👑Sahil👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Sahil👑👑Sahil👑◼️◼️\n◼️👑Sahil👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Sahil👑👑Sahil👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑Sahil👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            "👑 Sahil 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
