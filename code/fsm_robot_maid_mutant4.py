from fysom import *

##========================================================================
## Implementation of a robot maid who can cook, vaccum, clean the dishes and dance

## features : - 2 outputs has been changed

## Implementation of the finite state machine thanks to the Python module fysom
fsm=Fysom(initial = 'sleeping',
          events= [('sleep','cooking','sleeping'), ## Here are the transitions
                   ('sleep','vacuuming','sleeping'),
                   ('sleep','dancing','sleeping'),
                   ('sleep','cleaning','sleeping'),
                   ('sleep','sleeping','sleeping'),
                   ('cook','sleeping','cooking'),
                   ('cook','dancing','cooking'),
                   ('cook','vacuuming','cooking'),
                   ('cook','cleaning','cooking'),
                   ('clean','cooking','cleaning'),
                   ('clean','sleeping','cleaning'),
                   ('clean','vacuuming','cleaning'),
                   ('clean','dancing','cleaning'),
                   ('dance','cleaning','dancing'),
                   ('dance','sleeping','dancing'),
                   ('dance','vacuuming','dancing'),
                   ('dance','cooking','dancing'),
                   ('vacuum','sleeping','vacuuming'),
                   ('vacuum','cleaning','vacuuming'),
                   ('vacuum','cooking','vacuuming'),
                   ('vacuum','dancing','vacuuming')
                   ])

# While loop aiming at simulating interactions between the owner of the robot
# and the robot.
while(1):
    i=input("what do you want from me ? ")
    if i == 'sleep':
        if fsm.current == 'sleeping':
            print('already sleeping')
        else :
            fsm.sleep()
            print('going to sleep')
    elif i == 'vacuum':  #Change of the loop from the original one to allow the change of outputs depending of the previous state
        if fsm.current == 'cleaning'
            fsm.vacuum()
            print('going to sleep')
        else :
            fsm.vacuum()
            print('going to vacuum')
    elif i == 'cook' : #Change of the loop from the original one to allow the change of outputs depending of the previous state
        if fsm.current == 'sleeping':
            fsm.cook()
            print('going to dance')
        else:
            fsm.cook()
            print('going to cook')
    elif i == 'dance' :
        fsm.dance()
        print('going to dance')
    elif i == 'clean' :
        fsm.clean()
        print('going to clean')
    else :
        print('Sorry, it is not possible')
