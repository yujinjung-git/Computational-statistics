import numpy as np
import pandas as pd
from scipy import stats
from matplotlib import pyplot as plt

#위에 다 디폴트러 넣어러ㅏ

#Hypothesis
print("H0: The mean of IQ is 100")
print("H1: The mean of IQ is not equal to 100")


#sample data
sample=pd.read_csv("./sample.csv", header=None)
sample.head()

sample.columns=["IQ"]
sample_list=sample["IQ"].to_list()

#population vs sample

pop_mean0=100 #모평균(귀무가설)
pop_std=np.sqrt(80) #모시그마

n=sample.shape[0] #샘플사이즈
sample_mean=np.mean(sample_list) #
sample_std=np.std(sample_list, ddof=1) #to use (n-1)
#ddof default는 n

#test statistics
T=(sample_mean - pop_mean0)/(pop_std/np.sqrt(n))
#(X바 빼기모평균) / (모시그마/n루트)
print("test statistics is {}".format(np.round(T,3)))

#critical values
alpha=0.05
dist_norm=stats.norm(loc=0,scale=1)

ll=dist_norm.ppf(alpha/2) #low limit
ul=dist_norm.ppf(1-(alpha/2)) #upper limit
#임계치

print("critical values are {} and {}".format(np.round(ll,3),np.round(ul,3)))


#decision
if(np.abs(T)>ul):
    print("result : we can reject H0")
else:
    print("reject : we accept H0")
    
#normality check
stats.probplot(sample_list, plot=plt, dist='norm')
plt.title('probability plot : normality')
plt.show()

    
