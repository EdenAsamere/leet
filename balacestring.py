def balancedStringSplit(s):
    rcounter = 0
    lcounter = 0
    counter = 0
    for i in range(len(s)):
        if s[i] == 'R':
            rcounter += 1  
        else:
            lcounter += 1
        print(lcounter,rcounter)
        if rcounter == lcounter:
            counter += 1
    print(counter)
        
s = "RLRRLLRLRL"
balancedStringSplit(s)
