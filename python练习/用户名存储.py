#用户名的获取
import json

def get_stored_username():
    """如果存储了用户名，就获取他"""
    try:
        with open('lianxi.json')as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''提示输入用户名'''
    username=input('输入名字:')
    with open('lianxi.json','w')as f_obj:
        json.dump(username,f_obj)
    return username

def greet_user():
    """问候用户，并指出名字"""
    username=get_stored_username()
    if username:
        print('欢迎'+username+'。')
    else:
        username=get_new_username()
        print('欢迎'+username+'加入。')

greet_user()
    
            
