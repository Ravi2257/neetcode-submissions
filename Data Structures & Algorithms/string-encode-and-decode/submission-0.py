class Solution:

    def encode(self, strs: List[str]) -> str:
        
        s=""
        for i in range(len(strs)):
            s = s+str(len(strs[i]))+"#"+strs[i]
        print(s)
        return s   


    def decode(self, s: str) -> List[str]:
        text,i = [], 0
        while i < len(s):
            j = s.index('#', i)
            length = int(s[i:j])
            text.append(s[j+1:j+1+length])
            i = j + 1 + length
        return text