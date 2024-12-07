from tgServices import BotClient
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from pyrogram import filters, enums
import variables


@BotClient.on_message(filters.command("alive"))
async def alive_command(_, message: Message):

    await message.reply("<b>Bot is alive and running!</b>")
