import easygui as g
a=g.integerbox(msg="请输入您的得分",title="分数统计",lowerbound=0,upperbound=100)
print(a)
