'''

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Mr Ding"
Output: "rM gniD"

'''

def reverseWords(s):
    result = [word[::-1] for word in s.split()]
    return " ".join(result)

print(reverseWords("Let's take LeetCode contest"))