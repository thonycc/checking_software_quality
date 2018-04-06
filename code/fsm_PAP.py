from fysom import *
import random

##========================================================================
## Implementation of an authentification protocol that uses a password (PAP)

## Implementation of the finite state machine thanks to the Python module fysom
fsm=Fysom(initial = 'Ack',
          events= [('gp','Ack','open'), ## Here are the transitions
                    ('wp','Ack','try2'),
                    ('wp','try2','try3'),
                    ('wp','try3','close')])

# While loop aiming at simulating interactions between a client and a server.
# The client sends the password and the server replies accordingly if it is ok
# or not
while(1):
    i=input("Enter your password : ")
    if i == 'rar+':
        fsm.gp()
        print('Good password')
        break
    else:
        if fsm.current == 'close':
            print('Your account is now blocked')
            break
        else :
            fsm.wp()
            print('Wrong password')
