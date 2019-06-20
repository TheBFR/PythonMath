def factors(num):
    '''returns a list of the factors of num'''
    factorList = []
    for i in range(1,num+1):
        if num % i == 0:
            factorList.append(i)
    return factorList

factOne = factors(100)
factTwo = factors(120)

print(factOne)
print(factTwo)

commonFacts = set(factOne) & set(factTwo)
cfs = list(commonFacts)
print(cfs[-1])
