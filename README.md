# Operation

## Encryption

On first boot device will use PUBLIC 'secret' private key and re-generate public key. It will then use this key-pair. 

## Registry

There will be a 'registry' server that each machine will connect to on boot. It will publish to the topic 'register' an 'up' msg

Registery topic messages to PUB to

'up'
'alive'
'down'

Sent information
 - Device name
 - 

SUB topics

'available'

## Connection

Command and Control (C&C) is accessed via a REQ/REP link on a one-per-device link. Additional pub/sub sockets can be identified via C&C system for transfer of binary data.


