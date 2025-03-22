#Bit manipulation: Common tasks like setting, clearing, toggling and checking bits can be performed quickly using bitwise
#operators
#Bitwise operators: NOT, AND, OR and XOR
#XOR: If bits are same use the 0, else 1


#Characteristics: XOR
#a ^ 0 = a
#a ^ a = 0


#Left shift ( << n ): Shits the bits of a numbr to the left by n positions, adding 0 to the right.
#This is equivalent to mulitplying a number by 2^n.
#1001 << 2 => 100100

#Right shift ( >> n): Shits the bits of a number to the right by n positions, discarding bits on the right
#This is equivalent to diving a number by 2^n (integer division).

#1001 >> 2 = 0010

#Some bit manipulation techniques
# 1) Setting the ith bit of x to 1: x |= (1 << i)
# 2) Clearing the ith bit of x: x &= ~(1  << i )
# 3) Toggling the ith bit of x (from 0 to 1 and 1 to 0): x ^= (1 << i)
# 4) Checking if the ith bit is set: x & (i << 1) != 0 set else not set
# 5) Checking if a number is odd or even: If x & 1 == 0, x is even
# 6) Checking if a number if power of 2: if x > 0 and x & (x -1) == 0, x is a power of 2


