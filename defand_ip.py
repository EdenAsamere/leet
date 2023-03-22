def defangIPaddr(address):
    add=address.split('.')
    res=[]
    for i in add:
        res.append(i)
        res.append("[.]")
        y =''.join(res)
        x = y.strip('[.]')

    print(x)
    return
    
        
   

address = "1.1.1.1"
defangIPaddr(address)
    
