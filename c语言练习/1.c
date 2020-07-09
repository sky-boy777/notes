#include<stdio.h>
main()
{
  int a=10,y=0;
  do
  {
      a+=2;
      y+=a;
      if(y>50) break;

  }
  while(a=14);
  printf("a=%d y=%d\n",a,y);
}
