def count_one(n: int) -> int:
    count = 0
    # binary = n
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1

    return count

def convert_to_binary(n):
    binary = ''
    while n > 0:
        remainder = n % 2
        n = n // 2
        binary = str(remainder) + binary

    return int(binary)

n=4
print(convert_to_binary(n))
