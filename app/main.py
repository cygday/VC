from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import uuid
import os

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return FileResponse(os.path.join("static", "index.html"))

waiting = None
pairs = {}
clients = {}

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    global waiting, pairs
    user_id = str(uuid.uuid4())
    clients
    
    
    # Match with waiting user or wait for a partner
    if waiting is None:
        waiting = ws
        partner = None
    else:
        partner = waiting
        pairs[ws] = partner
        pairs[partner] = ws
        waiting = None
        

    try:
        while True:
            msg = await ws.receive_text()
            if ws in pairs:
                await pairs[ws].send_text(msg)
    except WebSocketDisconnect:
        if ws in pairs:
            try:
                await pairs[ws].close()
            except Exception:
                pass
            del pairs[pairs[ws]]
            del pairs[ws]
        if waiting == ws:
            waiting = None
    try:
        while True:
            msg = await ws.receive_text()
            data = json.loads(msg)
            
            target = data.get("target")
            if target and target in clients:
                await clients[target].send_text(json.dumps({
                    "from": user_id,
                    "data": data["data"]
                }))
    except WebSocketDisconnect:
        clients.pop(user_id, None)
