import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        n = math.gcd(len(str1), len(str2)) #find the gcd of the lengths of the strings
        return str1[:n]