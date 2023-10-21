class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        s,e = 0,len(skill)-1
        chemistry = 0
        tskill = skill[s]+skill[e]
        while s < e:
            diff = skill[s]+skill[e] 
            if tskill != diff:
                return -1
            else:
                chemistry += (skill[s]*skill[e])
                s+=1
                e-=1
                
        return chemistry
        