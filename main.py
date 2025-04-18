from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import Body
from pydantic import BaseModel
from generate import create_lesson_doc
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class User(BaseModel):
    name: str

class LessonInput(BaseModel):
    user: User
    standard: str

@app.post("/generate")
async def generate_lesson(data: LessonInput = Body(...)):
    file_path = create_lesson_doc(data.user.name, data.standard)
    return FileResponse(
        path=file_path,
        filename="lesson_plan.docx",
        media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
