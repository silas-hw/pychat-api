from classes import User, Message
import socket
import pickle

class Client():
    '''
    represents a connection to the server,
    When creating a client connection the username and usercolour of the bot can be defined
    '''

    HEADER = 64
    PORT = 5000
    IP = '86.3.196.184'
    ADDR = (IP, PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "!close"

    def __init__(self, name="UN-NAMED", colour="#3240a8"):
        self.bot = User(name, colour)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

    def send(self, msg):

        msg = Message(msg, self.bot) #make message object with content
        message = pickle.dumps(msg)
        msgLength = len(message)
        sendLength = str(msgLength).encode(self.FORMAT)
        sendLength += b' ' * (self.HEADER-len(sendLength))
        self.client.send(sendLength)
        self.client.send(message)

    def _receive(self):
        msgHeader = self.client.recv(self.HEADER).decode(self.FORMAT)

        if msgHeader:
            msgLength = int(msgHeader)
            msg = self.client.recv(msgLength)
            msg = pickle.loads(msg)
            return msg

    def listener(self, func):
        def wrapper():
            while True:
                msg = self._receive()
                func(msg)
        return wrapper