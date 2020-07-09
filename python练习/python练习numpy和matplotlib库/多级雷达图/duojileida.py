import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']
labels=np.array(['综合','KDA','发育','推塔','生存','输出'])
nAttr=6
data=np.array([7,9,6,6,8,7])#数据值
angles=np.linspace(0,2*np.pi,nAttr,endpoint=False)
data=np.concatenate((data,[data[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig=plt.figure(facecolor='white')
plt.subplot(111,polar=True)
plt.plot(angles,data,'bo-',color='y',linewidth=2)
plt.fill(angles,data,facecolor='y',alpha=0.25)
plt.thetagrids(angles*180/np.pi,labels)
plt.figtext(0.52,0.95,'DATA能力值雷达图',ha='center')
plt.grid(True)
plt.savefig('dota_radar.png')
plt.show()
