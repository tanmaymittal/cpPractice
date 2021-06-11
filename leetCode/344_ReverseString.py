"""
Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.

Follow up: Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.

"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        counter = len(s)-1
        for x in range(len(s)//2): 
            print(s[x])
            temp = s[x]
            s[x] = s[counter]
            s[counter] = temp
            counter -=1

# PASSED 