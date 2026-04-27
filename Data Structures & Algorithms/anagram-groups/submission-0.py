class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map=defaultdict(list)
        for i in strs:
            key ="".join(sorted(i))
            Map [key] . append(i)
        return list(Map.values())