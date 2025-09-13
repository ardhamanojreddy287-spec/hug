from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Allow CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeRequest(BaseModel):
    code: str

@app.post("/check")
async def check_code(data: CodeRequest):
    # Example logic: check if code contains "print"
    if "print" in data.code:
        return {"result": "✅ Code contains print statement!"}
    else:
        return {"result": "❌ No print statement found."}
    {
  "status": "success",
  "message": "✅ Code contains print statement!"
}