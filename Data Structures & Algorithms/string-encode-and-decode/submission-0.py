class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(len(s))+"#"+s
        return res
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = s.index('#', i)
            L = int(s[i:j])  
            strs.append(s[j+1:j+1+L])
            i = j+1+L
        return strs

        