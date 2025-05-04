class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        
        domino={}
        count=0

        for a,b in dominoes:
            key = tuple(sorted((a, b)))

            domino[key]=domino.get(key,0)+1
        
        for i in domino.values():
            if i>=2:
                count += (i * (i - 1)) // 2
        return count
