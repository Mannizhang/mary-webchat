import asyncio
import datetime
import random
import websockets
users = set()

async def server(websocket, path):
    users.add(websocket)
    while True:
        msg = await websocket.recv() # 接收到信息了。

        if msg is not None:
            for u in users:
                await u.send(msg)
    users.remove(websocket)

start_server = websockets.serve(server, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()