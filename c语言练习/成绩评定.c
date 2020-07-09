#include<stdio.h>
void main()
{
    int s;
	printf("输入一个0到100的数：\n",s);
    scanf("%d",&s);
    switch(s/10)
    {
        case 10:
        case 9: printf("优秀\n"); break;
        case 8: printf("好");break;
        case 7: printf("良");break;
        case 6: printf("及格");break;
        default: printf("不及格");
    }
}
