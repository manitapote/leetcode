def swap_odd_and_even(n: int):
    #even masK: Ox55555555 as 5 hexa = 0101 repeated to 8 times
    #odd mask: 0xAAAAAAAA as A hexa = 1010 repeated to 8 times
    even_mask = 0x55555555
    odd_mask = 0xAAAAAAAA #This has zero in the front not O

    return ((n & even_mask) << 1) | ((n & odd_mask) >> 1)


n = 41
print(swap_odd_and_even(n))