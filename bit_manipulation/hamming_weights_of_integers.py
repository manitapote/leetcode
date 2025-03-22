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

from typing import List
def hamming_weight_dynamic(n: int) -> List:
    dp = [0]*(n+1)
    for x in range(1, n+1):
        print(x >> 1)
        dp[x] = dp[x >> 1] + (x & 1)

    #Logic: if the last bit is 1, the x and x >> 1 has 1 bit difference
    #If the last bit is 0, the x and x >> 1 has 0 difference
    return dp
# n=4
# print(convert_to_binary(n))
n=7
print(hamming_weight_dynamic(n))

#Time complexity: O(log_2_(n)) as there are log_2_n bits for a number
#If we repeat this n times : O(nlog_2_(n))
#If there are 32 bits for each number, the time is constant for each number and O(n)
#Sapce complexity: O(1)


# FastAPI, ONNX, TensorRT, and serverless
# deployment.