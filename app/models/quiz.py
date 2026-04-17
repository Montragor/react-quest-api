from pydantic import BaseModel


class AnswerOptions(BaseModel):
    id: str
    text: str
    isCorrect: bool


class QuizQuestion(BaseModel):
    id: str
    question: str
    answers: list[AnswerOptions]
    explanation: str
