import numpy as np
from scipy import stats
print("#######1########")
#1-1 서울부산 드라마 시청률 two proportion ztest
print("H0: watching proportion same")
print("H1: watching proportion not same")

p1=(293/550)
p2=(341/708)
alpha=0.1
phat=(293+341)/(550+708)
var2=phat*(1-phat)
z=(p1-p2)/np.sqrt(var2*((1/550)+(1/708)))
print("1 test statistics : {}".format(np.round(z,4)))

distnorm=stats.norm(loc=0, scale=1)
ll=distnorm.ppf(alpha/2)
ul=distnorm.ppf(1-(alpha/2))
#print(ul)
print("1-1 result")

if(np.abs(z)>ul):
    print("reject H0, not same")
else:
    print("Accept H0, same")


#1-2
print("1-2 effect")
effect=(np.abs(p1-p2))/np.sqrt(var2)
print(effect)
if effect>=1.3:
    print("huge")
elif effect>=0.8:
    print("large")
elif effect>=0.5:
    print("medium")
elif effect>=0.2:
    print("small")
else:
    print("less than small")

print('\n')

print("\n#######2########")

#2-1 paired t test 쥐 훈련
y1=np.array([7.5, 7.1, 8.9, 8.5, 9.2, 6.0, 7.5])
y2=np.array([8.3, 7.5, 9.5, 8.1, 8.8, 7.4, 7.4])
di=y2-y1
alpha2=0.01
#print(di)

print("H0 y1 y2 same")
print("H1 y1 y2 not the same")

dimean=np.mean(di)
distd=np.std(di, ddof=1)
din=di.size

distt2=stats.t(din-1)
t=dimean/(distd/np.sqrt(din))
print("2-1 T: ",np.round(t,4))

ll=distt2.ppf(alpha2/2)
ul=distt2.ppf(1-(alpha2/2))

print("2-1 result")
if(np.abs(t)>ul):
    print("H0 reject, y1 y2 not same")
else:
    print("H0 accept, y1 y2 same")

#2-2 
effect2=np.abs(dimean)/distd
print("2-2 effect size : ", effect2)
print(effect2)
if effect2>=1.3:
    print("huge")
elif effect2>=0.8:
    print("large")
elif effect2>=0.5:
    print("medium")
elif effect2>=0.2:
    print("small")
else:
    print("less than small")
    
print("\n#######3########")    

#3-1 unpaired t test 분산 같을때 분산 구하기 spulling
n1=100
n2=100
n1mean=0.41
n2mean=0.45
n1std=0.01
n2std=0.02
alpha3=0.05

print("H0 equal A company B company")
print("H1 not equal A company B company")

stdpool=((n1-1)*(n1std**2)+(n2-1)*(n2std**2))/(n1+n2-2)
print("3-1 Var : ", stdpool)

t3=(n1mean-n2mean)/np.sqrt(stdpool*((1/n1)+(1/n2)))
distt3=stats.t(n1+n2-2)
print("T3", t3)

ll=distt3.ppf(alpha3/2)
ul=distt3.ppf(1-(alpha3/2))

print("3-2 Result :")
if(np.abs(t3)>ul):
    print("reject H0, A compamy B company not the same")
else:
    print("accept H0, A company B company same")

#4 멘델 one proportion z test?
print("\n#######4########")
n4=8023
green=2006
yellow=n4-green
gremean=green/n4
yelmean=yellow/n4
mu4=0.25
alpha4=0.05

print("H0 p(green proportion)==0.25")
print("H1 p(green proportion)!=0.25")

z4=(gremean-mu4)/np.sqrt((mu4*(1-mu4))/n4)
print("test statistics z : ",np.round(z4,4))

dist4=stats.norm(loc=0, scale=1)
ll=dist4.ppf(alpha4)
ul=dist4.ppf(1-(alpha4/2))

print("\n")
print("4 Result")
if(np.abs(z4)>ul):
    print("H0 reject, green != 0.25")
else:
    print("H0 accept, green == 0.25")











