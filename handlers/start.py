from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Handles /start command."""
    user_first_name = (
        update.effective_user.first_name if update.effective_user else "there"
    )
    welcome_text = (
        f"👋 Hi {user_first_name}! Welcome to **Speech2TextsBot**.\n\n"
        "I can convert your voice messages, audio files, and video clips into written text automatically.\n\n"
        "📌 **Quick Start:**\n"
        "Simply send or forward any audio, voice note, or video file to me, and I'll transcribe it for you!\n\n"
        "Type /help to see supported formats and usage details."
    )
    await update.message.reply_text(welcome_text, parse_mode="Markdown")
