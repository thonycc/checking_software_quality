from fysom import *

##========================================================================
## Implementation of a robot maid who can cook, vaccum, clean the dishes and dance

# Features : Cannot cook after sleeping
           	# - Cannot vacuum after dancing
       		# - Cannot clean after vacuuming
			# - Cannot sleep after vacuuming and conversely
			# - Cannot cook after cleaning and conversely


## Implementation of the finite state machine thanks to the Python module fysom
fsm=Fysom(initial = 'sleeping',
          events= [('sleep','cooking','sleeping'), ## Here are the transitions
                   ('sleep','dancing','sleeping'),
                   ('sleep','cleaning','sleeping'),
                   ('cook','dancing','cooking'),
                   ('cook','vacuuming','cooking'),
                   ('clean','sleeping','cleaning'),
                   ('clean','dancing','cleaning'),
                   ('dance','cleaning','dancing'),
                   ('dance','sleeping','dancing'),
                   ('dance','vacuuming','dancing'),
                   ('dance','cooking','dancing'),
                   ('vacuum','cleaning','vacuuming'),
                   ('vacuum','cooking','vacuuming'),
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