#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>

int main (void)
{
    //  Socket to talk to clients
    void *context = zmq_ctx_new ();
    void *responder = zmq_socket (context, ZMQ_PUB);
    int rc = zmq_bind (responder, "tcp://127.0.0.1:5555");
    assert (rc == 0);

    while (1) {
        char buffer [10];
        //zmq_recv (responder, buffer, 10, 0);
        //printf ("Received Hello\n");
        sleep (1);          //  Do some 'work'
        zmq_send (responder, "World", 5, 0);
    }

    return 0;
}