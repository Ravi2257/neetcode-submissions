class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in t:
            if i not in dic:
                return False
            else:
                dic[i]-=1
            
        for i in dic:
            if dic[i]!=0:
                return False
        return True