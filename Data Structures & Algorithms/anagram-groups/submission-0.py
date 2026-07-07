class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = {}

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in d: d[sorted_s] = []
            d[sorted_s].append(s)
        
        sublists = []

        for key in d:
            sublists.append(d[key])
        
        return sublists
        