def smallthancurr(nums):
    ress = sorted(nums)
    smaller = []
    keys = []
    for i in range(len(ress)):
        res = ress.index(ress[i])
        smaller.append(res)
        keys.append(res)
    print(smaller)
    a = list(zip(keys,smaller))
    
    print(a)
    print(keys)
nums = [8,1,2,2,3]
smallthancurr(nums)

