# In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.

# Return the sentence after the replacement.

 

# Example 1:

# Input: dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
s = set(dictionary)
sentence = sentence.split()
for j, w in enumerate(sentence):
     for i in range(1, len(w)):
        if w[:i] in s: 
            sentence[j] = w[:i]
            break
print(" ".join(sentence))
