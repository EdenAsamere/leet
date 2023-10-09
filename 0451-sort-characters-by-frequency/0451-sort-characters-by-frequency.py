import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        dic ={}
        minheap=[]
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in dic:
            heapq.heappush(minheap,(dic[j],j))
        re = ''
        print(minheap)
        while minheap:
            fre,ch = heapq.heappop(minheap)
            re += ch*fre
        return re[::-1]
        
            
        