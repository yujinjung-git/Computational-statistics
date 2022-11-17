import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

#random number between 0 and 1
print(np.random.rand())

#integer generation 뒤에 size=n 적으면n개만큼 뽑아줌
print(np.random.randint(0,100, size=10))

#float number generation
print(np.random.uniform(0,100,size=3))


#sampling 비복원추출과 복원 추출
#sampling without raplacement

a=np.arange(10) #0~9까지 생성 (배열)
print(np.random.choice(a,5))

#sampling with replacement

print(np.random.choice(a,5,replace=True))


#확률밀도함수
#normal distribution

dist_norm=stats.norm(loc=0, scale=1)

#pdf plot

x=np.linspace(-5,5,100) #-5부터 5까지 100개의 간격으로 나눠라
y=dist_norm.pdf(x)

plt.plot(x,y)
plt.title("normal distribution")
plt.show() #그래프에서 그래프아래의 넓이가 확률

#cdf plot
y2=dist_norm.cdf(x)
plt.plot(x,y2)
plt.title("normal distribution cdf")
plt.show()

#percent point function 확률값알려주면 그 그래프아래의 넓이알려줌

a=dist_norm.ppf(0.05)
b=dist_norm.ppf(0.95)

print("the percent points of a and b are {} and {}".format(a,b))


#sampling
sample_norm=dist_norm.rvs(size=2000) #size커질수록 중간에 모임
plt.hist(sample_norm, bins=50, rwidth=0.5, color='r')
plt.title("samples from Normal distribution")

