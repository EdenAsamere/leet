def mostWordsFound(sentences):
    no_words = []
    for i in sentences:
        res=i.split(" ")
        a=len(res)
        no_words.append(a)
        mostword=max(no_words)
    print(mostword)
  
            
        
     
       

sentences=["please wait","continue to fight","continue to win"]
mostWordsFound(sentences)
