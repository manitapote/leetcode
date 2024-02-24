#Time complexity O(n)
# def check(sentence):
#     store = {}
#     if len(sentence) > 128:
#         return False
#
#     for s in sentence:
#         if s in store:
#             return False
#         else:
#             store[s]= None
#     return True


#Time complexity is n^2
# def check(sentence):
#     for i, s in enumerate(sentence):
#         if s in sentence[i+1:]:
#             return False
#     return True

#Without using the another datas structure
#Time: O(nlog(n))
#Space : O(n)
def check(sentence):
    sorted_sentence = sorted(sentence)
    i = 0
    while True:
        if sorted_sentence[i] == sorted_sentence[i+1]:
            return False
        else:
            i = i + 1

            if i >= len(sorted_sentence) - 1:
                return True

a = 'aba'
print(check(a))

