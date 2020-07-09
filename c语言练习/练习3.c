#include<stdio.h>
void main()
{
    int a,b,c;
    a=b=c=1;
    b=b+c;
    a=a+b;
    printf("%d",(c<b)?b:a);
}
