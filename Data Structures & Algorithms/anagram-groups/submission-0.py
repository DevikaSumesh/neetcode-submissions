class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        r=defaultdict(list)
        for s in strs:
            sortedstr=''.join(sorted(s))
            r[sortedstr].append(s)
        return list(r.values())