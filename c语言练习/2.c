typedef int DataType;

//链表
typedef struct Node
{
  DataType *data;
  struct Node *next;
}Node, *pNode, *pList;
void InitLinkList(pList *pplist);//初始化链表
pNode BuyNode(DataType d);//创建链表节点
void PushBack(pList *pplist, DataType d);//尾插
void PopBack(pList *pplist);//尾删
void PushFront(pList *pplist, DataType d);//头插
void PopFront(pList *pplist);//头删
void PrintList(pList plist);//打印链表
pNode Find(pList plist, DataType d);//查找指定元素
void Remove(pList *pplist, DataType d);//删除指定的一个元素
void RemoveAll(pList *pplist, DataType d);//删除指定的所有元素
void Insert(pList *pplist, pNode pos, DataType d);//指定位置的后面插入
void Erase(pList *pplist, pNode pos);//指定位置删除
void DestroyList(pList *pplist);//销毁链表
pNode BuyNode(DataType d)

{
  pNode newNode = (pNode)malloc(sizeof(Node));
  if (newNode == NULL)
  {
    perror("malloc");
    exit(EXIT_FAILURE);
  }
  newNode->data = d;
  newNode->next = NULL;
  return newNode;
}
void InitLinkList(pList *pplist)
{
  assert(pplist);
  *pplist = NULL;
}
void PushBack(pList *pplist, DataType d)
{
  assert(pplist);
  pNode newNode = BuyNode(d);
  pNode cur = *pplist;
  //链表没有节点
  if (*pplist == NULL)
  {
    *pplist = newNode;
    return;
  }
  //链表有节点
  while (cur->next != NULL)
  {
    cur = cur->next;
  }
  cur->next = newNode;
}
void PopBack(pList *pplist)
{
  pNode cur = *pplist;
  pNode prev = NULL;
  assert(pplist);
  //链表没有节点
  if (*pplist == NULL)
  {
    return;
  }
  //链表有一个节点
  if (cur->next == NULL)
  {
    free(*pplist);
    *pplist = NULL;
    return;
  }
  //链表有两个及两个以上节点
  while (cur->next != NULL)
  {
    prev = cur;//prev中保存的是cur之前的那个节点
    cur = cur->next;
  }
  prev->next = NULL;
  free(cur);
}
void PushFront(pList *pplist, DataType d)
{
  pNode newNode = BuyNode(d);
  //pNode cur = *pplist;
  assert(pplist);
  ////链表没有节点
  //if (*pplist == NULL)
  //{
  // *pplist = newNode;
  //}
  ////链表有节点
  newNode->next = *pplist;
  *pplist = newNode;

}
void PopFront(pList *pplist)
{
  pNode cur = *pplist;
  assert(pplist);
  //链表为空
  if (*pplist == NULL)
  {
    return;
  }
  *pplist = cur->next;
  free(cur);
  cur = NULL;
}
void PrintList(pList plist)
{
  pNode cur = plist;
  while (cur)
  {
    printf("%d-->", cur->data);
    cur = cur->next;
  }
  printf("NULL\n");
}
pNode Find(pList plist, DataType d)
{
  pNode cur = plist;
  while (cur)
  {
    if (cur->data == d)
    {
      return cur;
    }
    cur = cur->next;
  }
  return NULL;
}
void Remove(pList *pplist, DataType d)
{
  pNode cur = *pplist;
  pNode prev = NULL;
  assert(pplist);
  if (cur == NULL)
  {
    return;
  }
  while (cur)
  {
    if (cur->data == d)
    {
      pNode del = cur;
      if (cur == *pplist)
      {
        *pplist = cur->next;
      }
      prev->next = cur->next;
      free(del);
      del = NULL;
      return;
    }
    else
    {
      prev = cur;
      cur = cur->next;
    }
  }
}
void RemoveAll(pList *pplist, DataType d)
{
  pNode cur = *pplist;
  pNode prev = NULL;
  assert(pplist);
  if (*pplist == NULL)
  {
    return;
  }
  while (cur)
  {
    if (cur->data == d)
    {
      pNode del = cur;
      if (cur == *pplist)
      {
        *pplist = cur->next;
      }
      else
      {
        prev->next = cur->next;
      }
      cur = cur->next;
      free(del);
      del = NULL;
    }
    else
    {
      prev = cur;
      cur = cur->next;
    }
  }

}
//在pos后面插入一个元素
void Insert(pList *pplist, pNode pos, DataType d)
{
  pNode newNode = BuyNode(d);
  assert(pplist);
  assert(pos);
  if (*pplist == NULL)
  {
    PushFront(pplist, d);
    return;
  }
  newNode->next = pos->next;
  pos->next = newNode;
}
void Erase(pList *pplist, pNode pos)
{
  assert(pplist);
  assert(pos);
  //要删除的是尾节点
  if (pos->next == NULL)
  {
    PopBack(pplist);
  }
  //删除的是非尾节点
  else
  {
    pNode del = pos->next;
    pos->data = pos->next->data;
    pos->next = pos->next->next;
    free(del);
    del = NULL;
  }
}
void DestroyList(pList *pplist)
{
  assert(pplist);
  pNode cur = *pplist;
  while (cur)
  {
    pNode del = cur;
    cur = cur->next;
    printf("del:%d\n", del->data);
    free(del);
    del = NULL;
  }
}
