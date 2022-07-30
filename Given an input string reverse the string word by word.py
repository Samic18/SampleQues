'''split string into individual words using space as deliminator then print words in reverse order
Time Complexity: O(n)
Space Complexity: O(n)'''

def reverse(s, left, right):
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverseByWords(s):
    s = list(s)
    n = len(s)
    beg = 0
    for i in range(n):
        if s[i] == " ":
            reverse(s, beg, i - 1)
            beg = i + 1
    reverse(s, beg, n - 1)
    reverse(s, 0, n - 1)
    s = "".join(s)
    return s
    
 
 
 '''The optimal approach tries to swap the words of the string from the beginning and end, using a two-pointers-based approach, to reverse the string in constant space. The algorithm is as follows:

Convert the string into an array of strings, which will store the words.
Initialize the 2 pointers left and right to 0 and string.length() – 1 respectively.
While the left pointer does not exceed the right pointer, swap the elements at the left and right pointer, move the left pointer forward and the right pointer backward by 1 place.
Finally, return the final calculated string.
Time Complexity: O(n)
Space Complexity: O(1)'''

def reverseByWords(s):
    s = s.split(" ")
    left = 0
    right = len(s) - 1
    while left <= right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    s = " ".join(s)
    return s
