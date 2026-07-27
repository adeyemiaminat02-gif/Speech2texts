from telegram import Update
from telegram.ext import ContextTypes
from config import Config


async def help_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Handles /help command."""
    max_mb = Config.MAX_FILE_SIZE // (1024 * 1024)
    help_text = (
        "🛠️ **Help & Supported Formats**\n\n"
        "**Supported Media Formats:**\n"
        "• 🎙️ **Voice Notes:** `.ogg`, `.opus`\n"
        "• 🎵 **Audio Files:** `.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`\n"
        "• 🎥 **Video Files:** `.mp4`, `.mkv`, `.mov`\n\n"
        "**File Limits:**\n"
        f"• Maximum file size allowed: **{max_mb} MB**\n\n"
        "**How to use:**\n"
        "1. Upload or forward a media file to this chat.\n"
        "2. Wait a brief moment while the bot processes and transcribes.\n"
        "3. Get your transcription right here! (If it's too long, it will be delivered as a `.txt` file)."
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")
