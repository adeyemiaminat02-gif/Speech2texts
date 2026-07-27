import logging
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    filters,
)

from config import Config
from services.utils import setup_logging
from handlers.start import start_handler
from handlers.help import help_handler
from handlers.about import about_handler
from handlers.speech import speech_handler

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()
    logger.info("Initializing Speech2TextsBot...")

    app = ApplicationBuilder().token(Config.BOT_TOKEN).build()

    # Register Command Handlers
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("about", about_handler))

    # Register Media Handler
    media_filter = (
        filters.VOICE
        | filters.AUDIO
        | filters.VIDEO
        | filters.Document.ALL
    )
    app.add_handler(MessageHandler(media_filter, speech_handler))

    logger.info("Bot successfully initialized. Starting polling loop...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
