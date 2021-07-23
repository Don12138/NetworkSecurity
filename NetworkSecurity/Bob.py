import asyncio
import threading

import websockets
import Client
import Vigenere
import people
import signatureOfRSA


class listen_task(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client

    def run(self):
        new_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(new_loop)
        asyncio.get_event_loop().run_until_complete(self.client.listen('ws://localhost:8765'))


if __name__ == '__main__':
    Bob = Client.Client('Bob')
    listen_task(Bob).start()
