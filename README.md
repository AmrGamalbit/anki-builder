# AnkiBuilder

AnkiBuilder is a web app that helps you create Anki decks effortlessly. Provide a source, and the app will generate a ready-to-use deck with meanings, pronunciations, and examples — powered by AI.

## Features
- **Multiple sources**: Generate decks from plain text, CSV files, YouTube videos, or web articles
- **Smart word selection**: AI picks words and idioms based on your level that you may not know
- **Multiple AI providers**: Supports Groq and Gemini, plus a free dictionary API
- **Pronunciation support**: Add audio via Google Text-to-Speech or dictionary providers
- **Card styling**: Customize the appearance of your cards with a user-friendly style editor
- **Modern UI**: Responsive design with built-in dark mode support

## Tech Stack
- **Frontend**: Vue
- **Backend**: FastAPI

## Getting Started

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment Variables
Create a `.env` file in the backend directory:
```env
GROQ_APIKEY=your_key_here
GEMINI_APIKEY=your_key_here
```

Only fill in the key for the provider you intend to use.

## License
This project is licensed under the MIT License.
