#include <stdio.h>

int main(int argc , char *argv[])
{
    int a;
    printf("Program name, insert 0\nthe word you have inserted, insert 1\nexit program, press 2\n");
    scanf("%i" , &a);
    if (a == 0 || a == 1 || a == 2)
    {
         printf(argv[a]);
    }
    else
    {
        printf("invaild input");
    }
}