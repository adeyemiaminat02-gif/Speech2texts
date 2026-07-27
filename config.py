import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    WHISPER_MODEL: str = os.getenv("WHISPER_MODEL", "base")
    MAX_FILE_SIZE: int = int(os.getenv("MAX_FILE_SIZE", 52428800))  # 50 MB
    TEMP_FOLDER: Path = Path(os.getenv("TEMP_FOLDER", "temp"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate(cls) -> None:
        if not cls.BOT_TOKEN:
            raise ValueError("BOT_TOKEN environment variable is missing!")
        cls.TEMP_FOLDER.mkdir(parents=True, exist_ok=True)


Config.validate()
