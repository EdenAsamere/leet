def restoreString(s, indices):
    temp=[]
    y = list(zip(s,indices))
    print(y)
    for val,i in y:
        temp.insert(i,val)
    res = ''.join(temp)
    print(res)
    


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
restoreString(s, indices)
