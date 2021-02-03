import zmq
import time

host = "127.0.0.1"
port = "5555"
conn_string = "tcp://{}:{}".format(host, port)

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.SUB)

public_key = b''

with open("device.pub", "br") as public:
    public_key = public.read(40)

# Connects to a bound socket
print(conn_string)

# Topic subscription
socket.setsockopt(zmq.SUBSCRIBE, "".encode())

# Server public key, needed for connection
socket.setsockopt(zmq.CURVE_SERVERKEY, public_key)

# Generated client keys, one-time use
client_public, client_secret = zmq.curve_keypair()

# Use generated key in communication with server
socket.setsockopt(zmq.CURVE_PUBLICKEY, client_public)
socket.setsockopt(zmq.CURVE_SECRETKEY, client_secret)

socket.connect(conn_string)

# Receives a string format message
while(1):
    print(socket.recv_string())
    time.sleep(1)
