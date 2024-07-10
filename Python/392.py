class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t): #iterate through the strings
            if s[i] == t[j]: #if the characters match, then move to the next character in s
                i += 1
            j += 1
        return i == len(s)