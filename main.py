from fastapi import FastAPI, Request
from pydantic import BaseModel
from .summarizer.summarizer import generate_summary


app = FastAPI()

class SummaryRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize_text(request: SummaryRequest):
    summary = generate_summary(request.text)
    return {"summary": summary}
