class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s,e = 0,len(skill)-1
        chemistry = 0
        tskill = set()
        while s < e:
            tskill.add(skill[s]+skill[e])
            if len(tskill)>1:
                return -1
            else:
                chemistry += (skill[s]*skill[e])
                s+=1
                e-=1
        return chemistry
        