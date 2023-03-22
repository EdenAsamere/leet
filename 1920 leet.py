def buildArray(nums):
    ans =[]
    for i in range(len(nums)):
        res = nums[nums[i]]
        ans.append(res)
    print(ans)
    return


nums = [0,2,1,5,3,4]
buildArray(nums)
         
