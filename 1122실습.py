from scipy import stats
group0=[9,8,7,8,8,9,8]
group50=[7,6,6,7,8,7,6]
group100=[4,3,2,3,4,3,2]
groupall=group0+group50+group100

print("H0 These samples are from the same population")
print("H1 Not all samples are from the same population")

for i, value1 in enumerate([group0,group50,group100]):
    for j, value2 in enumerate([group0, group50, group100]):
        if i>=j:
            continue
        tstat,pval=stats.ttest_ind(value1,value2)
        print('sample {} vs sample {} : test statistic is {}'.format(i,j,round(tstat,4)))
        print('pvalue is {}'.format(pval))
    

        alpha=0.05
        ngroup=3
        alpha_bon=alpha/ngroup
        
        if pval<alpha_bon:
            print("two samples are not same")
        else:
            print("two samples are same")