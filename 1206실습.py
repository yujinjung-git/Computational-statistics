import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data1=pd.read_csv("class1.csv", header=0)

obs_freq=data1['class'].value_counts()
obs_freq

#expected frequency
pop0=[0.5,0.3,0.2]
n=np.sum(obs_freq)
exp_freq=[n*j for j in pop0]
exp_freq

T=np.sum((obs_freq-exp_freq)**2/exp_freq)

print("test statistics :", round(T,3))
alpha=0.05
dist_chi=stats.chi2(2)
ul=dist_chi.ppf(1-alpha)
if(T>ul):
    print("reject H0")
else:
    print("accept H0")
    
effsizes=np.sqrt(T/(np.sum(n)*(len(exp_freq)-1)))
print("effect size",round(effsizes,3))

T, pval=stats.chisquare(obs_freq, exp_freq)

print("test statistics ", round(T,3))
print("pvalue", round(pval,3))

