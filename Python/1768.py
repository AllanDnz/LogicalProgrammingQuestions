class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = ""
        i = 0
        while i < min(len(word1), len(word2)): 
            #concatenating the characters alternatively
            result += word1[i]
            result += word2[i] 
            i += 1
        return result + word1[i:] + word2[i:] 