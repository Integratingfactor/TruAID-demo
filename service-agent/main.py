from fastapi import FastAPI

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TranslationTask(BaseModel):
    text: str
    target_language: str

@app.post("/translate")
async def submit_translation_task(task: TranslationTask):
    if not task.text or not task.target_language:
        raise HTTPException(status_code=400, detail="Text and target language must be provided")
    # Here you would add the logic to handle the translation task
    return {"message": "Translation task submitted", "task": task}
