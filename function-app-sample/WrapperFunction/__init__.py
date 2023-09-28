import azure.functions as func

import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def index():
    return {
        "info": "hello world.",
    }
