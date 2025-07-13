from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import secrets
import string

app = FastAPI(title="Random Secure String Generator API")

# Optional: CORS Middleware if you're using a frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class StringOptions(BaseModel):
    length: int = Query(32, ge=1, le=512)
    include_uppercase: bool = True
    include_lowercase: bool = True
    include_numbers: bool = True
    include_special_chars: bool = False

@app.post("/generate")
def generate_secure_string(options: StringOptions):
    character_pool = ""

    if options.include_uppercase:
        character_pool += string.ascii_uppercase
    if options.include_lowercase:
        character_pool += string.ascii_lowercase
    if options.include_numbers:
        character_pool += string.digits
    if options.include_special_chars:
        character_pool += "!@#$%^&*()-_=+[]{}|;:,.<>?/"

    if not character_pool:
        return {
            "error": "At least one character type must be selected!"
        }

    generated = ''.join(secrets.choice(character_pool) for _ in range(options.length))

    return {
        "generated_string": generated,
        "length": len(generated)
    }

@app.get("/ping")
def ping():
    return {"message": "pong"}