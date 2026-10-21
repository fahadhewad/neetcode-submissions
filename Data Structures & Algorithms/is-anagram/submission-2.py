class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        lettersA = {}
        lettersB = {}

        for i in range(len(s)):
            lettersA[s[i]] = lettersA.get(s[i], 0) + 1

        for i in range(len(t)):
            lettersB[t[i]] = lettersB.get(t[i], 0) + 1

        for key, value in lettersA.items():
            if key not in lettersB or value != lettersB.get(key):
                return False

        return True