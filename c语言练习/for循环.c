#include<stdio.h>
int main()
{
    int i=1,sum=0,m;
    printf("请输入一个整数：")
    scanf("%d",&m);
    for(;i<=m;) {sum+=i;i++;}
    printf("%d",sum);
}
