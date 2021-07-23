import time

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket


class SimpleEcho(WebSocket):
    def handleMessage(self):
        for key, client in self.server.connections.items():
            client.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, "connected")

    def handleClose(self):
        print(self.address, "closed")

server = SimpleWebSocketServer('', 8765, SimpleEcho)
server.serveforever()







