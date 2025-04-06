from typing import List
def number_of_candies(ratings: List[int]):
    candies = [1] * len(ratings)

    for i in range(1, len(ratings)):
        if ratings[i-1] < ratings[i]:
            candies[i] = candies[i - 1] + 1

    for i in range(len(ratings) - 1, 0, -1):
        if ratings[i - 1] > ratings[i]:
            #Crucial part: if the adjacent to the right is less and
            #already has less candy, keep as it is
            candies[i - 1] = max(candies[i - 1], candies[i] + 1)
    return sum(candies)




ratings = [4, 3, 2, 4, 5, 1]
print(number_of_candies(ratings))
ratings = [1, 3, 3]
print(number_of_candies(ratings))

#The main learning is local minima for increasing order lie on left side
# and for decreasing order lie in right side