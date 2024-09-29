import aiohttp
import asyncio
import argparse

async def websocket_client(address):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.ws_connect(f'ws://{address}/ws') as ws:
                while True:
                    # サーバーにメッセージを送信
                    await ws.send_str("Hello, WebSocket Server!")
                    print("Sent: Hello, WebSocket Server!", flush=True)

                    # サーバーからのメッセージを受信
                    msg = await ws.receive()  # メッセージを1つ受信
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        print(f"Received from server: {msg.data}", flush=True)
                    elif msg.type == aiohttp.WSMsgType.CLOSED:
                        print("Connection closed", flush=True)
                        break
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        print(f"Error: {ws.exception()}", flush=True)
                        break

                    await asyncio.sleep(1)  # 1秒間待機

    except Exception as e:
        print(f"An error occurred: {e}", flush=True)

# イベントループを実行
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='WebSocket Client')
    parser.add_argument('--address', required=True, help='Address of the host')

    # 引数を解析
    args = parser.parse_args()

    # websocket_client関数を呼び出す
    asyncio.run(websocket_client(args.address))
