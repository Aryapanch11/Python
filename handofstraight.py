# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

# Example 1:

# Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
# Example 2:

# Input: hand = [1,2,3,4,5], groupSize = 4
# Output: false
# Explanation: Alice's hand can not be rearranged into groups of 4.
from collections import Counter
hand = [1,2,3,6,2,3,4,7,8]
groupSize= 3
if len(hand) % groupSize != 0:
        print (False)
count = Counter(hand)  
sorted_keys = sorted(count.keys()) 
for  key in sorted_keys:
    if count[key]>0:
        start_count =count[key]
        for i in range(key,key + groupSize):
            if count[i]<start_count:
                 print (False)
            count[i] -= start_count
print (True)
# step1 - check if group possile
# step2 - count occurance of each card
# step3 - sort the unique card values
# step4 - form consecutive groups
# -if this card is still avalibalbe
#  check and form a group starting from key
# step5 - return true if all group are formed