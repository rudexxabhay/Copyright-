import asyncio
import importlib
from pyrogram import idle
from COPYRIGHT2 import COPYRIGHT2
from COPYRIGHT2.modules import ALL_MODULES

LOGGER_ID = -1002094142057

# Handling the event loop properly
try:
    loop = asyncio.get_event_loop()
    if loop.is_closed():
        raise RuntimeError
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("COPYRIGHT2.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("𝖻𝖺𝗁𝖺𝗇𝖼𝗁𝗈𝖽 𝖯𝗂𝗋𝗈 𝖢𝗈𝖽𝖾𝗋 𝗄𝗋𝗅𝗈 𝖾𝖽𝗂𝗍 𝖺𝖺 𝗀𝗒𝖺 𝗇 𝖾𝗋𝗋𝗈𝗋")
    await COPYRIGHT2.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝗋𝗎𝗇𝗇𝗂𝗇𝗀**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
