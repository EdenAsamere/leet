def numJewelsInStones(jewels, stones):
    temp = []
    for i in jewels:
        y=stones.count(i)
        temp.append(y)
        res = sum(temp)
    print(res)
jewels = "z"
stones = "ZZ"
numJewelsInStones(jewels, stones)
