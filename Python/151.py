class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split() #separating the string into words
        
        reversed_words = words[::-1] #reversing the string

        reversed_string = ' '.join(reversed_words) #concatenating the words and forming the inverted string including the space
        
        return reversed_string