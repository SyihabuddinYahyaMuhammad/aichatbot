from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio

app = FastAPI()
chat = []
afkTime = 5

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def balesanBot(chat):
    if chat.lower() == "help":
        return "Masukkan pertanyaan, dan bot akan berusaha menjawab"
    else:
        return "Pertanyaan tidak dikenali"

@app.get("/", response_class=HTMLResponse)
async def get(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "chat": chat})

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global afkTime
    await websocket.accept()
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
    
