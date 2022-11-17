import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

print("H0 : the mean is 360")
print("H1 : the men is not 360")

pop_mean0=360
n=30
sample_mean=356
sample_std=np.sqrt(100)
alpha=0.5

T=(sample_mean-pop_mean0)/(sample_std/np.sqrt(n))
print("T : ", np.round(T,3))

x=np.linspace(-5,5,100)
y=stats.t(10).pdf(x)
plt.plot(x,y,color='blue')
plt.xlabel("t")
plt.title("t-distribution : df = 10")


dist_t=stats.t(29)
ll=dist_t.ppf(alpha/2)
ul=dist_t.ppf(1-(alpha/2))
plt.plot(x,dist_t.pdf(x),color='red')
plt.title("freedo 29")

print("critical values are {} and {}".format(np.round(ll,3),np.round(ul,3)))

if(np.abs(T)>ul):
    print("Result : we can reject H0")
else:
    print("Result : we accept H0")
    
cohen=np.abs(sample_mean-pop_mean0)/sample_std
if(cohen>=1.3):
    print("Effect size: "+str(cohen)+", Huge effect")
elif(cohen>=0.8):
     print("Effect size: "+str(cohen)+", Large effect")
elif(cohen>=0.5):
    print("Effect size: "+str(cohen)+", Medium effect")
elif(cohen>=0.2):
    print("Effect size: "+str(cohen)+", Small effect")
else:
    print("Effect size: "+str(cohen))
    
from scipy.stats import ttest_1samp

samp_data=[356,370,360,366,345,340,369,382] 
print(ttest_1samp(samp_data, popmean=pop_mean0)   )



'''///////////////////////////////////////////'''
'''z-test start'''
print("H0z : the mean is 360")
print("H1z : the men is not 360")

zmean=360
zn=30
zsmean=356
zsstd=np.sqrt(100)
alphaz=0.5
Tz=(zmean-zsmean)/(zsstd/np.sqrt(n))
print("Test stastics is {}".format(np.round(T,3)))

dist_norm=stats.norm(loc=0, scale=1)
llz=dist_norm.ppf(alphaz/2)
ulz=dist_norm.ppf(1-(alphaz/2))
print("critical value are {} and {}".format(np.round(llz,3),np.round(ulz,3)))

if(np.abs(Tz)>ulz):
    print("Result : we can reject H0")
else:
    print("Result : we accept H0")
