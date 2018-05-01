from fysom import *

##========================================================================
## Implementation of a robot maid who can cook, vaccum, clean the dishes and dance

## features : - The link which enable the robot to vacuum after cleaning the dishes has been misdirected from cleaning to cooking
#              - The link which enable the robot to cook after vacuuming has been misdirected from vacuuming to cleaning

## Implementation of the finite state machine thanks to the Python module fysom
fsm=Fysom(initial = 'sleeping',
          events= [('sleep','cooking','sleeping'), ## Here are the transitions
                   ('sleep','vacuuming','sleeping'),
                   ('sleep','dancing','sleeping'),
                   ('sleep','cleaning','sleeping'),
                   ('cook','sleeping','cooking'),
                   ('cook','dancing','cooking'),
                   ('cook','vacuuming','cleaning'),
                   ('cook','cleaning','cooking'),
                   ('clean','cooking','cleaning'),
                   ('clean','cleaning','cleaning'),
                   ('clean','vacuuming','cleaning'),
                   ('clean','dancing','cleaning'),
                   ('dance','cleaning','dancing'),
                   ('dance','sleeping','dancing'),
                   ('dance','vacuuming','dancing'),
                   ('dance','cooking','dancing'),
                   ('vacuum','sleeping','vacuuming'),
                   ('vacuum','cleaning','cooking'),
                   ('vacuum','cooking','vacuuming'),
                   ('vacuum','dancing','vacuuming'),
                   ])

# While loop aiming at simulating interactions between the owner of the robot
# and the robot.
while(1):
    i=input("what do you want from me ? ")
    if i == 'sleep':
        if fsm.current == 'sleeping':
            print('already sleeping')
            break
        else :
            fsm.sleep()
            print('going to sleep')
            break
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
