#include<stdio.h>
void main()
{
    int a,b,c;
    printf("请输入三角形三边的值a,b,c:(用空格分开)\n");
    scanf("%d %d %d",&a,&b,&c);
    if(a==b&&b==c)
        printf("等边三角形\n");
    else if(a!=b&&a!=c&&b!=c)
        printf("一般三角形\n");
    else
    printf("等腰三角形");

}
