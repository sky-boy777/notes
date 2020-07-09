#include<stdio.h>
void main()
{
    int n,flag=0;
    printf("输入整数:\n");
    scanf("%d",&n);
    if(n%2==0&&n%3==0)
    flag=1;
    if(flag==0)
        printf("%d不能同时被2和3整除\n",n);
    else
        printf("%d能被2和3同时整除",n);
}
