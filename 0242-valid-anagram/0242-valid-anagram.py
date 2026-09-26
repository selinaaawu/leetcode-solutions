class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # valid anagram if same letters
        # can use dict mapping # letters
        # create Counter of each and compare

        ## QUICK AND EASY
        return Counter(s) == Counter(t)

        ## MANUALLY
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        return countS == countT
        