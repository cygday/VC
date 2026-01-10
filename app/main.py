from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import json
import uuid
import os

app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

@app.get("/")
async def root():
    return FileResponse(os.path.join("static", "index.html"))

#waiting = None
#pairs = {}
#clients = {}

#@app.websocket("/ws")
#async def ws_endpoint(ws: WebSocket):
 #   await ws.accept()
 #   global waiting, pairs
 #   user_id = str(uuid.uuid4())
 #   clients[user_id] = ws
    
    
    # Match with waiting user or wait for a partner
  #  if waiting is None:
   #     waiting = ws
    #    partner = None
    #else:
     #   partner = waiting
      #  pairs[ws] = partner
      #  pairs[partner] = ws
      #  waiting = None
        
    #await try_match(user_id)
    
    #try:
     #   while True:
     #       msg = await ws.receive_json() 
            
      #      partner_id = pairs.get(user_id)
            
       #     if not partner_id:
        #        continue
         #   await clients[partner_id].send_json(msg)
            
          #  if user_id in waiting:
           #     waiting.remove(user_id)
                
            #    partner = pairs.pop(user_id, None)
                
            #if partner:
                    
             #   pairs.pop(partner, None)
             #   await try_match(partner)

            #if msg.get("type") == "next":
             #   partner = pairs.pop(user_id, None)
              #  if partner:
               #     pairs.pop(partner, None)
                    
                #    await try_match(partner)
                    
                #await try_match(user_id)
                
                #continue
            
                                
    #        if ws in pairs:
   #             await pairs[ws].send_text(msg)
  #  except WebSocketDisconnect:
 #       if ws in pairs:
          #  try:
         #       await pairs[ws].close()
        #    except Exception:
       #         pass
      #      del pairs[pairs[ws]]
     #       del pairs[ws]
    #    if waiting == ws:
   #         waiting = None
  #  try:
 #       while True:
       #     msg = await ws.receive_text()
      #      data = json.loads(msg)
            
     #       target = data.get("target")
    #        if target and target in clients:
   #             await clients[target].send_text(json.dumps({
  #                  "from": user_id,
 #                   "data": data["data"]
#                }))
                
 #   except WebSocketDisconnect:
 #       clients.pop(user_id, None)
        
#async def try_match(user_id):
  #  if waiting:
  #      partner_id = waiting.pop(0)
        
  #      pairs[user_id] = partner_id
  #      pairs[partner_id] = user_id
        
  #      await clients[user_id].send_json({
  #          "type": "matched",
  #          "role": "offer"
  #      })
        
 #       await clients[partner_id].send_json({
 #           "type": "matched",
 #           "role": "answer"
 #           })
#    else:
#        waiting.append(user_id)
