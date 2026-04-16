from pathlib import Path

BASE_DIR = path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

LESSONS_FILE = DATA_DIR / "lessons.json"
QUIZ_FILE = DATA_DIR / "quiz_questions.json"

FRONTEND_ORIGIN = "http://localhost:5173"

