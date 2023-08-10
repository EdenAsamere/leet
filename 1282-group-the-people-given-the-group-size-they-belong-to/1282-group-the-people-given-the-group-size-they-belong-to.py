class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dic = {}
        res = []
        for i, j in enumerate(groupSizes):
            if j not in dic:
                dic[j] = [i]
            else:
                dic[j].append(i)
                
            if len(dic[j]) == j:
                while len(dic[j]) > 0:
                    res.append(dic[j][:j])
                    dic[j] = dic[j][j:]
        return res
