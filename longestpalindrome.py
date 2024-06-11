# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
# Example 2:

# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is 1.
from collections import Counter
s = "abccccdd"
c =Counter(s)
ans =0
for i in c.values():
    ans += int(i/2)*2
    if ans%2 ==0 and i%2==1:
       ans = ans+1 
print(ans)   

s ="abccccdd"
pair_counter = 0
chars = set()
for ch in s:
    if ch in chars:
        chars.remove(ch)
        pair_counter += 1
    else:
        chars.add(ch)                   
pair_counter = pair_counter * 2 + (1 if len(chars) > 0 else 0)
print(pair_counter)