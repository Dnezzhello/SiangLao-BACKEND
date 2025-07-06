# SiangLao Backend

Flask-based backend service for Lao ASR (Automatic Speech Recognition) that processes audio files through multiple ML models.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure ML service is running on `http://localhost:8000`

## Run

Start the Flask server:
```bash
python app.py
```

Or with environment:
```bash
FLASK_ENV=development python app.py
```

Server runs on `http://localhost:5000`

## API Endpoints

- `POST /api/upload` - Upload audio file
- `POST /api/transcribe/<request_id>` - Start transcription
- `GET /api/status/<request_id>` - Check progress
- `GET /api/result/<request_id>` - Get results
- `GET /health` - Health check

## Configuration

Set `FLASK_ENV` environment variable:
- `development` (default)
- `production` 
- `testing`

## File Support

Supported audio formats: WAV, MP3, M4A (max 10MB)