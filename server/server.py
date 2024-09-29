from aiohttp import web

async def websocket_handler(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    
    print("Client connected", flush=True)
    
    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.TEXT:
                print(f"Received: {msg.data}", flush=True)
                await ws.send_str(f"Server received: {msg.data}")
            elif msg.type == web.WSMsgType.BINARY:
                print("Received binary data", flush=True)
                await ws.send_str("Binary data not supported.")
            elif msg.type == web.WSMsgType.CLOSED:
                print("Connection closed by client", flush=True)
                break
            elif msg.type == web.WSMsgType.ERROR:
                print(f"WebSocket connection closed with exception {ws.exception()}", flush=True)

    except Exception as e:
        print(f"Error occurred: {str(e)}", flush=True)
    finally:
        print("Closing WebSocket connection", flush=True)
        await ws.close()

    return ws

app = web.Application()
app.add_routes([web.get('/ws', websocket_handler)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)
