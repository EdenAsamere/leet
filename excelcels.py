def excel(s):
    start = ord(s[0])
    end = ord(s[3])
    s1,s2 = int(s[1]),int(s[4])
    letter =[range(start,end+1)]
    print(letter)
    count = [s1,s2]*(s2-s1+1)
    output = ['']*(end-start+1)
    for i in range(start,end+1):
        output.append(i)
    print(count)

s ="A1:C3"
excel(s)
        
