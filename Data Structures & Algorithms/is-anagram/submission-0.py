class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        else:
            a1=dict()
            a2=dict()
            for i in range(0,len(s)):
                if s[i] not in a1:
                    a1[s[i]] = 1
                else:
                    a1[s[i]] += 1
                if t[i] not in a2:
                    a2[t[i]] = 1
                else:
                    a2[t[i]] += 1
            return a1 == a2        
            
