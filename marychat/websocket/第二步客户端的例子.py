import asyncio.async
import websockets




async def server(websocket,path):
    pass;

start_server = websockets.serve(server, '127.0.0.1', 9999)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()