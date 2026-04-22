from fastapi import FastAPI

from app.core.db import Base, engine
from app.models import LessonDB, QuizQuestionDB, AnswerOptionDB
from app.routers import lessons, quiz
from app.core.db import SessionLocal
from app.services.seed_service import seed_lessons, seed_quiz_questions

app = FastAPI(title="ReactQuest API")

app.include_router(lessons.router)
app.include_router(quiz.router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        seed_lessons(db)
        seed_quiz_questions(db)
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def read_root():
    return {"message": "ReactQuest API is running."}