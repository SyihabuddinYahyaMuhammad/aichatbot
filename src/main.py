from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request, Query, Depends, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional
import asyncio
import random
import string



app = FastAPI()
chat = []
afkTime = 30
tokenId = "admin"

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def balesanBot(chat):
    if chat.lower() == "help":
        return "Masukkan pertanyaan, dan bot akan berusaha menjawab"
    else:
        return "Pertanyaan tidak dikenali"

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
    
