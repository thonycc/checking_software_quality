from fysom import *

##========================================================================
## Implementation of a robot maid who can cook, vaccum, clean the dishes and dance

## features :   -  The link which enable the robot to vacuum after cleaning the dishes has been misdirected from cleaning to cooking
##              -  The link which enable the robot to dance after cooking has been misdirected from cooking to vaccuming
##              - The link which enable the robot to clean after sleeping has been misdirected from sleeping to dancing
##

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
                   ('clean','sleeping','dancing'),
                   ('clean','vacuuming','cleaning'),
                   ('clean','dancing','cleaning'),
                   ('dance','cleaning','dancing'),
                   ('dance','sleeping','dancing'),
                   ('dance','vacuuming','dancing'),
                   ('dance','cooking','vacuuming'),
                   ('vacuum','sleeping','vacuuming'),
                   ('vacuum','cleaning','cooking'),
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
    elif i == 'vacuum':
        fsm.vacuum()
        print('going to vacuum')
    elif i == 'cook' :
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
