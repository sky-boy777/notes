#include<stdio.h>
void main()
{
   int x=11,y=1;
   if(x%2==1)
    x+=5;
   else
    x-=3;
   y+=5;
   printf("%d %d",x,y);
   return 0;
}
