import sys
import easygui as g
if g.ccbox("亲爱的还玩吗?",choices=("还要玩！","算了吧/(ㄒoㄒ)/~~")):
    g.msgbox("还是不玩了，快睡觉吧！")
else:
    sys.exit(0)
