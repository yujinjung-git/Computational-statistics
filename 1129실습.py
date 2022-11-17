import numpy as np
import pandas as pd
from statsmodels.stats.proportion import proportions_ztest

data1=pd.read_csv("./onep.csv")

table1=pd.crosstab(index=data1['class'], columns=data1['handed'],margins=True, margins_name='Total')
table1

table2=pd.crosstab(index=data1['class'], columns=data1['handed'],margins=True, margins_name='index')
table2

table3=pd.crosstab(index=data1['class'], columns=data1['handed'], margins=True, margins_name='Total', normalize='columns')
table3

table4=pd.crosstab(index=data1['class'], columns=data1['handed'], margins=True, margins_name='Total', normalize='all')
table4

print("H0 90% of doctors recommend aspirin for headache")
print("H1 90% of doctors don't recommend aspirin for headache")

pop0=0.9
n=100
yes=82
phat=yes/n
zstat, pval=proportions_ztest(count=yes, nobs=n, value=pop0)

print("z statistic : ", round(zstat,4))
print("p value : ", round(pval, 4))

ef=np.abs(phat-pop0)/np.sqrt(pop0*(1-pop0))
print(ef)