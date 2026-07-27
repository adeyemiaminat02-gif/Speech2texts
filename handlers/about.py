from telegram import Update
from telegram.ext import ContextTypes
from config import Config


async def about_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Handles /about command."""
    about_text = (
        "ℹ️ **About Speech2TextsBot**\n\n"
        "Speech2TextsBot is a fast, accurate Speech-to-Text bot powered by **OpenAI Whisper** engine.\n\n"
        "⚡ **Features:**\n"
        "• Automatic language identification\n"
        "• Audio extraction from video\n"
        "• High accuracy powered by neural transcriptions\n"
        f"• Active Whisper Model Engine: `{Config.WHISPER_MODEL}`\n\n"
        "Built with Python 3.12+ and `python-telegram-bot` v22+."
    )
    await update.message.reply_text(about_text, parse_mode="Markdown")
