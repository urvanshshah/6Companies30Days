# 1:Given an array of strings, return all groups of strings that are anagrams

class Solution:
    def Anagrams(self, words, n):
        def ss(s):
            count = [0]*26
            for i, c in enumerate(s):
                count[ord(c)-ord('a')] += 1
            ans = ""
            for i in range(26):
                ans+= chr(ord('a')+i)*count[i]
            return ans
        anagram = {}      
        for i,string in enumerate(words):
            ascString = ss(string)
            if ascString not in anagram:
                anagram[ascString] = []
            anagram[ascString].append(words[i])
        return [val for val in anagram.values()]
        n = 256
