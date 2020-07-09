#include<stdio.h>
void main()
{
    int r,n,m,temp;
    printf("输入两个数(用空格分开)\n");
    scanf("%d %d",&n,&m);
    if(n<m)
    {
        temp=n;
        n=m;
        m=temp;
    }
    while(m!=0)
    {
        r=n%m;
        n=m;
        m=r;
    }
    printf("%d",n);
}
