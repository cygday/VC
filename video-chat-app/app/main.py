from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
import json
import uuid

app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

clients = {}

@app.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    user_id = str(uuid.uuid4())
    clients
    
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