class Solution:
    def isPalindrome(self, s: str) -> bool:
        pal = ""
        for i in range(len(s)):
            if(s[i].isalnum()):
                pal += s[i]
            else:
                continue 
        for j in range(len(pal)//2):
            if(pal[j].upper()==pal[len(pal)-j-1].upper()):
                continue
            else:
                return False
        return True



        