def maximumWealth(accounts):
    res = []
    for i in accounts:
        res.append(sum(i))
    print(max(res))
        
        
        
        



accounts = [[1,5],[7,3],[3,5]]
maximumWealth(accounts)
