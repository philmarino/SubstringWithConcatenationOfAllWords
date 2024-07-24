from itertools import permutations

def findSubstring(s, words):
    perms = list(permutations(words))
    answer = []
    for item in perms:
        word = ''.join(item)
        index = s.find(word)
        if index > -1:
            answer.append(index)

    answer.sort()
    return answer

# Example 1:
# Input: 
s = "barfoothefoobarman"
words = ["foo","bar"]
print(findSubstring(s, words))

# Output: [0,9]
# Explanation:
# The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
# The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

# Example 2:
# Input: 
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(findSubstring(s, words))

# Output: []
# Explanation:
# There is no concatenated substring.

# Example 3:
# Input: 
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(findSubstring(s, words))

# Output: [6,9,12]
# Explanation:
# The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
# The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
# The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].
