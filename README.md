# 🎙️ Speech2TextsBot

Production-ready Telegram Bot to transcribe voice messages, audio files, and videos into text using **OpenAI Faster-Whisper** and Python 3.12+.

---

## ✨ Features
- 🗣️ **Voice Notes & Audio Files:** Supports `.ogg`, `.mp3`, `.wav`, `.m4a`, `.aac`, `.flac`.
- 🎥 **Video Files:** Extracts and transcribes audio from `.mp4`, `.mkv`, `.mov`.
- 🌐 **Automatic Language Detection:** Identifies the spoken language automatically.
- 📦 **Smart Long Transcriptions:** Delivers transcriptions via text or auto-exports `.txt` files if Telegram limits are exceeded.
- ⚡ **High Performance:** Powered by CTranslate2 via `faster-whisper` for minimal RAM usage and rapid transcription speeds.

---

## 🛠️ Local Installation

### Prerequisites
- Python 3.12 or higher
- System installation of **FFmpeg**

#### Installing FFmpeg:
- **macOS:** `brew install ffmpeg`
- **Ubuntu/Debian:** `sudo apt update && sudo apt install -y ffmpeg`
- **Windows:** Download from [FFmpeg Official](https://ffmpeg.org/download.html) and add to PATH.

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Speech2Textsbot.git](https://github.com/yourusername/Speech2Textsbot.git)
   cd Speech2Textsbot
