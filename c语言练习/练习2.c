#include<stdio.h>
void main()
{
   int x=35;
   char z='A';
   int b;
   b=((x&15)&&(z<'a'));
   printf("%d",b);/*运行结果为1*/
}
