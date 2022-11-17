import numpy as np
from scipy import stats
from scipy.stats import ttest_ind
print("H0 the means of the two groups are the same")
print("H1 the means of the two groups are different")

a=np.array([5,8,9,8,7,7,2])
b=np.array([9,6,5,4,8])

pop_mean=0
alpha=0.05
amean=np.mean(a)
astd=np.std(a,ddof=1)
#여기요
an=a.size

bmean=np.mean(b)
bstd=np.std(b,ddof=1)
#여기요
bn=b.size

varpool=((an-1)*(astd)**2 + (bn-1)*(bstd)**2)/(an+bn-2)
print("vp:",round(varpool,4))

t=(amean-bmean)/np.sqrt(varpool*((1/an)+(1/bn)))

print("Test stastics",np.round(t,4))

#여기
distt=stats.t(an+bn-2)
ll=distt.ppf(alpha/2)
ul=distt.ppf(1-alpha/2)

if(np.abs(t)>ul):
    print("reject h0")
else:
    print("accept h0")
    
ttest_ind(a,b,equal_var=True)
