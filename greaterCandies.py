def runningSum(nums,extra):
    res = ([i+extra for i in nums])
    print(res)
    minn = min(res)
    print(minn)
    output = []
    for i in range(len(res)):
        if minn == res[i]: 
            output.append(False)
            print(res[i])
        else:
            output.append(True)
    print(output)
        
candies = [4,2,1,1,2]
extra = 1
runningSum(candies,extra)
