class Solution:
    def compress(self, chars: List[str]) -> int:
        length = len(chars)
        ans = 0

        if length == 1: #if there is only one character, then return 1
            return 1
        
        i = 0 
        while i < length: #iterate through the characters
            char = chars[i]
            count = 0
            while i < length and chars[i] == char: #count the number of times the character appears
                count += 1
                i += 1
            
            chars[ans] = char #update the character
            ans += 1
            if count > 1: #if the count is greater than 1, then update the count
                for c in str(count):
                    chars[ans] = c
                    ans += 1
        return ans
