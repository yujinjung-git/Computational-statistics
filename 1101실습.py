import numpy as np
import seaborn as sns
from scipy import stats
import pandas as pd
print("H0 the mean difference is zero")
print("H1 the mean difference is less than zero")

before=np.array([5,8,9,8,7,7,2])
after=np.array([9,6,5,9,5,8,5])

di=before-after
print(di)

pop_diff=0
n=len(di)
di_mean=np.mean(di)
#이거바꾸기
di_std=np.std(di)
me_std=0
for i in di:
    me_std+=(i-di_mean)**2
me_std=np.sqrt(me_std)/np.sqrt(n-1)

t=(di_mean-pop_diff)/(me_std/np.sqrt(n))
print("T", np.round(t,4))

dist_t=stats.t(n-1)
alpha=0.05

ll=dist_t.ppf(alpha)
print("Lower limit", np.round(ll,4))

if(t<ll):
    print("H0 rejected")
else:
    print("H0 accepted")
    
data1=pd.DataFrame(zip(before,after))
data1.columns=['before', 'after']
sns.boxplot(data=data1,orient='h')