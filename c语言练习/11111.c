#include <stdio.h>
#include <stdlib.h>

typedef int DataType;

typedef struct node {
    DataType member;
    struct node *next;
}*LinkList, *pNode;

// 初始化链表
LinkList GetEmptyList() {
    LinkList head = (pNode)malloc(sizeof(struct node));
    head->member = 0;
    head->next = NULL;
    return head;
}


// 在非增链表中插入结点
void InsertNode(LinkList head, DataType x) {
    pNode p,q;
    for(p = head; p->next != NULL; p = p->next) {
        if(p->next->member <= x) {
            q = (pNode)malloc(sizeof(struct node));
            q->member = x;
            q->next = p->next;
            p->next = q;
            return;
        }
    }
    q = (pNode)malloc(sizeof(struct node));
    q->member = x;
    q->next = p->next;
    p->next = q;
}

// 新结点插入为首结点
void PushNode(LinkList head, DataType x) {
    pNode p = (pNode)malloc(sizeof(struct node));
    p->member = x;
    p->next = head->next;
    head->next = p;
}

// 删除结点
int DeleteNode(LinkList head, DataType x) {
    pNode p,q;
    for(p = head; p != NULL; p = p->next) {
        if(p->next->member == x) {
            q = p->next;
            p->next = q->next;
            free(q);
            return 1; // 成功删除member(第一个)为x的结点
        }
    }
    return 0; // 没有找到member为x的结点
}

// 查找结点
int FindNode(LinkList head, DataType x) {
    pNode p;
    for(p = head->next; p != NULL; p = p->next) {
        if(p->member == x) return 1; // 找到了
    }
    return 0; // 没有找到
}

// 销毁链表
void DestroyList(LinkList head) {
    pNode q,p = head;
    while(p) {
        q = p;
        p = q->next;
        free(q);
    }
    head = NULL;
}

// 遍历链表
void ShowList(LinkList head) {
    pNode p = head->next;
    while(p != NULL) {
        printf("%d ",p->member);
        p = p->next;
    }
    printf("\n");
}

int main() {
    DataType x,res;
    LinkList head = GetEmptyList();
    printf("输入一个整数('q' to quit): ");
    while(scanf("%d",&x) == 1) {
        InsertNode(head, x); // 创建非增链表
        printf("输入一个整数('q' to quit): ");
    }
    fflush(stdin);
    ShowList(head);
    printf("输入待查找的整数: ");
    scanf("%d",&x);
    res = FindNode(head, x);
    if(res) printf("找到了。\n");
    else printf("没找到！\n");
    printf("输入待删除的整数: ");
    scanf("%d",&x);
    res = DeleteNode(head, x);
    if(res) printf("成功删除。\n");
    else printf("没找到数据为:%d的结点！\n",x);
    ShowList(head);
    DestroyList(head);
    return 0;
}
