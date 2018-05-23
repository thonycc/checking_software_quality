/*
C implementation of the FSM algorithm of the Robot Maid
inputs = ['cook','sleep','vacuum','dance','clean']
states = ['sleeping','cooking','vacuuming','dancing','cleaning']
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    char const *cur_state="sleeping";

    while (1)
    {
        char i[10];

        printf("what do you want from me ? ");

        scanf("%s", i);

        if (strcmp(i, "sleep") == 0 && strcmp(cur_state, "sleeping") == 0)
        {
            printf("already sleeping \n");
            //printf("The current state is %s \n",cur_state);
        }

        else if (strcmp(i, "sleep") == 0)
        {
            printf("going to sleep\n");
            cur_state="sleeping";
            //printf("The current state is %s \n",cur_state);
        }
        else if (strcmp(i, "dance") == 0)
        {
            printf("going to dance\n");
            cur_state="dancing";
            //printf("The current state is %s \n",cur_state);
        }
        else if (strcmp(i, "clean") == 0)
        {
            printf("going to clean\n");
            cur_state="cleaning";
            //printf("The current state is %s \n",cur_state);
        }
        else if (strcmp(i, "cook") == 0)
        {
            printf("going to cook\n");
            cur_state="cooking";
            //printf("The current state is %s \n",cur_state);
        }
        else if (strcmp(i, "vacuum") == 0)
        {
            printf("going to vacuum\n");
            cur_state="vacuuming";
            //printf("The current state is %s \n",cur_state);
        }
        else
        {
            printf("This is not possible, try something different please \n");
        }
    }
}
