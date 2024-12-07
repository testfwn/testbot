import os
import asyncio
from aiohttp import web
from pyrogram import idle
from server import web_server
from tgServices import BotClient
from datetime import datetime
import json
import variables as var
import time
import os
import subprocess
import sys


def install_dependencies():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
    except Exception as e:
        print(f"Error installing dependencies: {e}")
        sys.exit(1)


# Install dependencies


async def main():
    try:
        await BotClient.start()

        app = web.AppRunner(await web_server())
        await app.setup()

        bind_address = var.BIND_ADDRESS
        bind_port = int(os.getenv("PORT", 8000))
        await web.TCPSite(app, bind_address, bind_port).start()

        print("--------Bot Started----------------")

        await asyncio.gather(
            idle(),
        )
    except Exception as error:
        pass


if __name__ == "__main__":
    try:
        try:
            install_dependencies()
        except:
            pass

        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        BotClient.stop()
    except Exception as error:
        pass
