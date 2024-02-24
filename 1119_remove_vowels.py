class Solutions(object):
    def remove_vowels(self, sentence: str) -> str:
        for a in ['a', 'e', 'i', 'o', 'u']:
            sentence = sentence.replace(a, '')

        return sentence


sentence = "The urgent care center was flooded with patients after the news of a new deadly virus was made public."
a = Solutions()
print(a.remove_vowels(sentence))

#space complexity: O(n)
#time complexity: O(n)

import re
class ReSolutions(object):
    def remove_vowels(self, sentence: str) -> str:
        return re.sub(r'[aeiou]', '', sentence)
sentence = "The urgent care center was flooded with patients after the news of a new deadly virus was made public."
a = ReSolutions()
print(a.remove_vowels(sentence))

#Time Complexity O(n)
#Space Complexity O(n)


