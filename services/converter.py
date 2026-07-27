import asyncio
import logging
from pathlib import Path
from services.utils import cleanup_temp_file

logger = logging.getLogger(__name__)


async def convert_to_wav(input_path: Path) -> Path:
    """Converts input media file to mono 16kHz WAV format required by Whisper."""
    output_path = input_path.with_suffix(".wav")

    # Command to convert audio/video to 16kHz mono WAV
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(input_path),
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
        str(output_path),
    ]

    logger.info(f"Converting {input_path} to {output_path} via FFmpeg...")

    process = await asyncio.create_subprocess_exec(
        *cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        error_msg = stderr.decode().strip()
        logger.error(f"FFmpeg conversion failed: {error_msg}")
        cleanup_temp_file(output_path)
        raise RuntimeError(
            f"FFmpeg failed to process media file. Details: {error_msg}"
        )

    return output_path
