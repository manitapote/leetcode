# 17 Letter Combinations of a Phone Number


def find_letter_combination(num: str):
    if len(num) == 0:
        return []

    map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def dfs(i, map, result, num, chosen):
        if i == len(num):
            result.append(''.join(chosen[:]))
            return

        for alpha in map[num[i]]:
            chosen.append(alpha)

            dfs(i+1, map, result, num, chosen)

            chosen.pop()

        return result


    return dfs(0, map, [], num, [])


digits = "23"
print(find_letter_combination(digits))
digits = ""
print(find_letter_combination(digits))
digits = "22"
print(find_letter_combination(digits))
digits='2'
print(find_letter_combination(digits))
