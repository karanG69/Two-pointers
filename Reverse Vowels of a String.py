class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']

        if len(s)==1:
            return s
        if len(s)==2:
            if s[0] in vowels and s[1] in vowels:
                return s[::-1]
            else:
                return s
        ans1=""
        ans2=""
        st=0
        ed=len(s)-1
        while(st<ed):
            if s[st] in vowels and s[ed] in vowels:
                ans1+=s[ed]
                ans2+=s[st]
                st+=1
                ed-=1
            elif s[st] not in vowels and s[ed] in vowels:
                ans1+=s[st]
                st+=1
            elif s[ed] not in vowels and s[st] in vowels:
                ans2+=s[ed] 
                ed-=1
            else:
                ans1+=s[st]
                ans2+=s[ed]
                st+=1
                ed-=1
        if st==ed:
            ans1+=s[st]
        return ans1+ans2[::-1]
