#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

typedef struct newtype
{
    int number ;
    char character;
    float fl;
    char *qqq;
}
newtype;


int f(int , int);
int main(void)
{
    printf("Result : %i\n" , f(9 , 2));
    newtype W;
    (W).number = 5;
    (W).character = 'A';
    (W).fl = 4.65;
    (W).qqq = "qwerty";
    printf("%i\n%c\n%0.2f\n%s" , (W).number , (W).character , (W).fl , (W).qqq);
}
int f(int X , int Y)
{
    return pow(X , Y) + (X / Y);
}