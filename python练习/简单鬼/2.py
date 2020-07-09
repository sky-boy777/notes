import easygui
n=0
a=easygui.multpasswordbox('输入','校园登入',(['用户名'],['密码']))
while 1:
        if a[0]=='a123':
                if a[1]=='123':
                        easygui.msgbox(msg='登入成功', title='温馨提示', ok_button='确定', image=None, root=None)
                        break
        else:
                n+=1
                if n>2:
                        easygui.msgbox(msg='你不是本人，警告你不要试图屎出密码\n再见', title='警告提示', ok_button='滚', image=None, root=None)
                        break
                else:
                        a=easygui.multpasswordbox('输入错误，请重新输入\n还有%d机会'%(3-n),'校园登入',(['用户名'],['密码']))
