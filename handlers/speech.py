import io
import uuid
import logging
from pathlib import Path
from telegram import Update
from telegram.ext import ContextTypes

from config import Config
from services.converter import convert_to_wav
from services.transcriber import transcriber_service
from services.utils import cleanup_temp_file

logger = logging.getLogger(__name__)


async def speech_handler(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    """Handles incoming voice messages, audio files, and video uploads."""
    message = update.message
    if not message:
        return

    # Determine which media type was sent
    media = (
        message.voice
        or message.audio
        or message.video
        or message.document
    )

    if not media:
        return

    # File size validation
    if media.file_size and media.file_size > Config.MAX_FILE_SIZE:
        max_mb = Config.MAX_FILE_SIZE // (1024 * 1024)
        await message.reply_text(
            f"❌ File is too large. Maximum supported size is {max_mb} MB."
        )
        return

    status_msg = await message.reply_text("⏳ Downloading media file...")

    unique_id = uuid.uuid4().hex
    raw_path = Config.TEMP_FOLDER / f"raw_{unique_id}"
    wav_path = None

    try:
        # Download media file
        file_obj = await context.bot.get_file(media.file_id)
        await file_obj.download_to_drive(custom_path=raw_path)

        await status_msg.edit_text(
            "⚙️ Processing and converting audio format..."
        )
        wav_path = await convert_to_wav(Path(raw_path))

        await status_msg.edit_text("✍️ Transcribing with OpenAI Whisper...")
        transcription, language = await transcriber_service.transcribe(wav_path)

        if not transcription.strip():
            await status_msg.edit_text(
                "⚠️ Couldn't extract any spoken words or speech from this file."
            )
            return

        header = f"🌐 **Language Detected:** `{language}`\n\n📝 **Transcription:**\n"

        # Handle long responses (Telegram limit is 4096 chars)
        if len(header) + len(transcription) <= 4000:
            await status_msg.edit_text(
                f"{header}{transcription}", parse_mode="Markdown"
            )
        else:
            await status_msg.edit_text(
                "📄 Transcription finished! Attached as a file due to length."
            )
            file_bytes = io.BytesIO(transcription.encode("utf-8"))
            file_bytes.name = f"transcription_{unique_id[:8]}.txt"

            await message.reply_document(
                document=file_bytes,
                caption=f"🌐 **Language Detected:** `{language}`",
                parse_mode="Markdown",
            )

    except RuntimeError as e:
        logger.error(f"Media conversion failed: {e}")
        await status_msg.edit_text(
            "❌ Unrecognized or corrupted media file format."
        )
    except Exception as e:
        logger.exception(f"Unexpected error during media processing: {e}")
        await status_msg.edit_text(
            "❌ An unexpected error occurred while processing your file."
        )
    finally:
        cleanup_temp_file(raw_path)
        cleanup_temp_file(wav_path)
