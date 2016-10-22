import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8766') as websocket:

        name = input("")
        await websocket.send(name)

        greeting = await websocket.recv()
        print("< {}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
asyncio.get_event_loop().run_forever()