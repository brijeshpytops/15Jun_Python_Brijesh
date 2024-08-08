#include <stdio.h>

void main()
{
    int win = 34;
    int guess;
    int status = 1; // true
    int count = 0;

    while (status)
    {
        printf("Guess a num : ");
        scanf("%d", &guess);
        if (win == guess)
        {
            count += 1;
            printf("Congrats You win!!!, after guessing number %d times.\n\n", count);
            status = 0;
        }
        else
        {
            if (guess < win)
            {
                printf("Too low\n\n");
            }
            else
            {
                printf("Too high\n\n");
            }
            count += 1;
        }
    }
}