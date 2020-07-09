import easygui as g
a=g.boolbox(msg='Shall I continue?', title=' ', choices=('确定', '错误'), image=None)
print(a)
