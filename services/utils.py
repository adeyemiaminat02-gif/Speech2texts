import os
import logging
from pathlib import Path
from config import Config

logger = logging.getLogger(__name__)


def setup_logging() -> None:
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=getattr(logging, Config.LOG_LEVEL.upper(), logging.INFO),
    )


def cleanup_temp_file(file_path: str | Path | None) -> None:
    """Safely removes a temporary file from disk."""
    if file_path is None:
        return
    try:
        path = Path(file_path)
        if path.exists():
            os.remove(path)
            logger.debug(f"Successfully deleted temp file: {path}")
    except Exception as e:
        logger.error(f"Failed to delete temp file {file_path}: {e}")
