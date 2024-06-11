# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

# Example 1:

# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]
# Example 2:

# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]

words =[ "bella","label","roller"]
result =[]
chars = set(words[0])
for char in chars:
    freq = min([word.count(char) for word in words])
    result += freq*[char]
print(result)
  