from typing import List


# method 1
# time complexity: O(n)
# space complexity : O(n^2)??

#correction:
# time complexity: O(n^2 + m^2)
# space complexity : O(n + m)
s = 'racecar'; l='carace'
a={}
b = {}

class Solution:
    def isAnagram(self, s : str, l: str)  -> bool:
        a = {i:s.count(i) for i in s}
        b = {i:l.count(i) for i in l}

        if len(s) != len(l):
            return False

        for i in a.keys():
            if i in b:
                if a[i] == b[i]:
                    continue
                else:
                    return False
            else: 
                return False
        return True
    


instance = Solution()
print(instance.isAnagram(s,l))

# method 2
class Solution:
    def isAnagram(self, s: str, l: str) -> bool:
        if len(s) != len(l):
            return False

        # Use a dictionary to count occurrences more efficiently
        a = {}
        b = {}

        for char in s:
            a[char] = a.get(char, 0) + 1
        
        for char in l:
            b[char] = b.get(char, 0) + 1 # it is giving default value just in case a char is not found.

        return a == b  # Compare the two dictionaries

instance = Solution()
print(instance.isAnagram(s, l))

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT