from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Query, Depends, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional
import asyncio
import random
import string
import os
import logging
import requests


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

app = FastAPI()
chat = []
afkTime = 300
tokenId = "admin"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def balesanBot(chat):
    # logger.debug("OPENROUTER_API_KEY: " + OPENROUTER_API_KEY)
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:8000",
        "X-Title": "AI Chat App",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/llama-3.2-3b-instruct:free",
        "messages": [{"role": "user", "content": chat}],
        "top_p": 1,
        "temperature": 0.7,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "repetition_penalty": 1,
        "top_k": 0
    }
    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=payload
        )

        if response.status_code == 200:
            result = response.json()
            logger.debug("result:", result)
            return result["choices"][0]["message"]["content"]
        else:
            error_detail = response.text()
            logger.debug(
                f"API Error Details: {error_detail}"
            )
            return "Something Wrong with the API"

    except Exception as e:
        logger.debug(f"Unexpected Error: {str(e)}")
        return "Something Wrong!"

def get_random_string():
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

async def get_token(
    websocket: WebSocket,
    token: Optional[str] = Query(None),
):
    if token is None:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
    return token

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    global tokenId
    tokenId = get_random_string()
    return templates.TemplateResponse("index.html", {"request": request, "token": tokenId})

@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    token: str = Depends(get_token),
):
    global afkTime, tokenId
    await websocket.accept()
    if  token != tokenId:
        websocket.send_text("token incorrect.\nconnection clossed.")
        websocket.close()
    tokenId = get_random_string()
    while True:
        try:
            data = await asyncio.wait_for(websocket.receive_text(), timeout=afkTime)
            await websocket.send_text(balesanBot(data))
        except asyncio.TimeoutError:
            print('timeout!')
            await websocket.send_text("host afk detected.\nconnection clossed.")
            await websocket.close()
            break
        except WebSocketDisconnect:
            print("host closed!")
            break
    
