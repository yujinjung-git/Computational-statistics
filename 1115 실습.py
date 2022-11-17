import numpy as np
import seaborn as sns
from scipy import stats
import pandas as pd

group0=[9,8,7,8,8,9,8]
group50=[7,6,6,7,8,7,6]
group100=[4,3,2,3,4,3,2]
groupall=group0+group50+group100

print("H) these samples are from the same population")
print("H1 not all samples are from the same population")

levene_pval, W_stat=stats.levene(group0,group50,group100)
alpha=0.05
if levene_pval<alpha:
    print("the samples don's have the same variance")
else:
    print("the samples have the same variance")
    
meanall=np.mean(groupall)

#msb computation
for i in [group0, group50, group100]:
    ssb=np.sum(len(i)*(np.mean(i)-meanall)**2)

ssb=np.sum(len(i)*(np.mean(i)-meanall)**2 for i in [group0, group50, group100])
msb=ssb/(3-1)
print("msb: {}".format(msb))

ssw=np.sum((len(i)-1)*np.var(i, ddof=1) for i in [group0, group50, group100])
#for i in [group0, group50, group100]:
#    ssw=np.sum((len(i)-1))*np.var(i, ddof=1)
dfw=np.sum(([len(i)-1 for i in [group0, group50, group100]]))
#for i in [group0, group50, group100]:
#    dfw=np.sum([len(i)-1])

msw=ssw/dfw
print("Msw:{}".format(msw))

f=msb/msw
print("test statistic F : {}".format(f))

f_dist=stats.f(2,dfw)
alpha=0.05
rl=f_dist.ppf(1-alpha)
print("critical value : {}".format(rl))

if f>rl:
    print("reject")
else:
    print("accept")
    

f_stats,p_val=stats.f_oneway(group0, group50, group100)
print("test statistic f : {}".format(f_stats))
print("pvalue : {}".format(p_val))

