# simple_pub.py
import zmq
import time

host = "127.0.0.1"
port = "5555"
conn_string = "tcp://{}:{}".format(host, port)

public_key, secret_key = zmq.curve_keypair()

with open("device.priv", "bw+") as private:
    private.write(secret_key)

with open("device.pub", "bw+") as private:
    private.write(public_key)

# Creates a socket instance
context = zmq.Context()
socket = context.socket(zmq.PUB)

# Enable Curve Encryption
socket.setsockopt(zmq.CURVE_SERVER, True)

# Load Server secret key, client must load the public key to communicate
# Which has been given to it prior
socket.setsockopt(zmq.CURVE_SECRETKEY, secret_key)



# Binds the socket to a predefined port on localhost
print(conn_string)
socket.bind(conn_string)

# Sends a string message
# Receives a string format message
while(1):
    socket.send_string("hello")
    time.sleep(1)
