import asyncio
import logging
from pathlib import Path
from typing import Tuple
from faster_whisper import WhisperModel
from config import Config

logger = logging.getLogger(__name__)


class Transcriber:
    def __init__(self) -> None:
        logger.info(
            f"Initializing Faster-Whisper model '{Config.WHISPER_MODEL}' on CPU..."
        )
        # Using CPU with int8 quantization for optimal deployment on free/low-tier instances
        self.model = WhisperModel(
            Config.WHISPER_MODEL, device="cpu", compute_type="int8"
        )
        logger.info("Faster-Whisper model loaded successfully.")

    def _transcribe_sync(self, audio_path: Path) -> Tuple[str, str]:
        """Synchronous Whisper transcription call to execute in thread pool."""
        segments, info = self.model.transcribe(
            str(audio_path), beam_size=5, vad_filter=True
        )

        text_segments = []
        for segment in segments:
            text_segments.append(segment.text.strip())

        full_text = " ".join(text_segments).strip()
        language = info.language.upper() if info.language else "UNKNOWN"

        return full_text, language

    async def transcribe(self, audio_path: Path) -> Tuple[str, str]:
        """Asynchronously transcribes audio file off the main event loop."""
        loop = asyncio.get_running_loop()
        return await loop.run_in_executor(
            None, self._transcribe_sync, audio_path
        )


transcriber_service = Transcriber()
