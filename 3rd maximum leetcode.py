def thirdMax(nums):
    sortedarr = sorted(nums,reverse=True)
    res = list(dict.fromkeys(sortedarr))
    if len(res) < 3:
        return res[0]
    return res[2]
nums = [2,2,3,1]
print(thirdMax(nums))
