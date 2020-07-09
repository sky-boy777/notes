import easygui as g
msg = "选择你喜欢的一种业余生活"
title = ""
choicess_list = ["看书","游泳","骑自行车","玩游戏"]
reply = g.choicebox(msg,choices=choicess_list)
print(reply)
