def finalValueAfterOperations(operations):
    x = 0
    for i in range(len(operations)):
        if operations[i] == '--X' or operations[i] == 'X--':
            x-=1
        elif operations[i] == '++X' or operations[i] == 'X++':
            x+=1
    print(x)


operations = ["++X","++X","X++"]
finalValueAfterOperations(operations)


        
            
                
                   
