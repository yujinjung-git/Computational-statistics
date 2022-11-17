import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
#1-1
dist_norm=stats.norm(loc=0, scale=np.sqrt(10))
sample_norm=dist_norm.rvs(size=20)
mean1=np.mean(sample_norm)
print("1-1 평균", mean1)

#1-2
mean2=[]
i=0
while(i<50):
    sample_norm=dist_norm.rvs(size=20)
    means=np.mean(sample_norm)
    mean2.append(means)
    i+=1

plt.hist(mean2, bins=50, rwidth=0.5, color='r')
plt.title("1-2")
plt.show()
print("1-2 plt 참조")

#1-3
mean3=np.mean(mean2)
var3=np.var(mean2)
print("1-3 평균 ", mean3,",", "1-3 분산 ", var3)
print("\n")

#2-1
dist_norm2=stats.norm(loc=10, scale=np.sqrt(10))
x=dist_norm2.rvs(size=100)
plt.hist(x,bins=50,rwidth=0.5,color='r')
plt.title("2-1")

#2-1 mean
realval=10
m21=sum(x)/len(x)
temp=0
i=0
for i in x:
    temp+=pow(i-m21,2)
var21=temp/(len(x)-1)
print("2-1 hist 참조, 2-1 평균", m21, ",", "2-1 분산", var21)

#2-2
y=[]
for i in x:
    temp=(i-m21)/np.sqrt(realval)
    y.append(temp)
    
print("2-2 y 평균", np.round(np.mean(y),3),",", "2-2 y 분산", np.round(np.var(y))) #평균,분산 각 0, 1 프린트

print("\n")
#3
mean31=34.3
var31=30.14
dist_norm31=stats.norm(loc=mean31, scale=np.sqrt(var31))

clength=dist_norm31.cdf(32)-dist_norm31.cdf(29) #췌장길이 확률 구하기
print("3 췌장 길이 29~21일 확률: ", clength)
print("\n")
#4-1
print("4-1 : Z 검정")
#4-2

dist_norm4=stats.norm(loc=0, scale=1)

mu4=360
x4=356
pstd4=10
n4=30
alpha=0.05

print("4-2 H0 : mu=360, H1: mu!=360 ")
ll=dist_norm4.ppf(alpha/2)
ul=dist_norm4.ppf(1-(alpha/2))
t=(x4-mu4)/(pstd4/np.sqrt((n4)-1))


if(np.abs(t)>ul):
    print("4-2 Reject H0")
else:
    print("4-2 Accept H0")

print("\n")
#5
dist_norm5=stats.norm(loc=0, scale=1)
mu5=15000
n5=100
x5=15200
pstd5=1220
alpha5=0.01

print("5-1 H0: mu>=15000, H1: mu<15000")
ll= dist_norm5.ppf(alpha5)
t=(x5-mu5)/(pstd5/np.sqrt((n5)-1))

if(t<ll):
    print("5-2 Reject H0")
else:
    print("5-2 Accept H0")
print("\n")
#보너스 문제
print("보너스 문제 : 물고기입니다.")
