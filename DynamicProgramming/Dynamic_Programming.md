## Dynamic Programming

When there are overlapping subproblems in which result of one subproblem depends on another we use dynamic programming.

There are two ways to store the results:
- Top Down (or memoization)
- Bottom up (or tabulation)

#### Reasons to use dynamic programming:
1) Optimal Substructure:  When we use the optimal results of subproblems to achieve the optimal result of the bigger problem.
2) Overlapping subproblems: When same subproblems are solved repeatedly in different parts of the problem.


#### Approaches of Dynamic Programming (DP)
1) Top-Down Approach (Memoization)
In this approach, the solution of recursive is kept and added to memoization table to avoid repeated calls of same subproblems.

2) Bottom-Up Approach (Tabulation)
In this approach, we start with the smallest sub-problem and gradually build up to the final solution.
We use dp table where we first fill the solution for base cases and then fill the remaining entries of the table using
recursive formula. We use recursive formula on table entries and do not make recursive calls.


Dynamic programming solves the exponential time complexity to linear time.

Memoization approach for Fibonacci series:

```
 def fibRec(n, memo):
  
    # Base case
    if n <= 1:
        return n

    # To check if output already exists
    if memo[n] != -1:
        return memo[n]

    # Calculate and save output for future use
    memo[n] = fibRec(n - 1, memo) + \
              fibRec(n - 2, memo)
    return memo[n]

def fib(n):
    memo = [-1] * (n + 1)
    return fibRec(n, memo)

n = 5
print(fib(n))
```
Time Complexity: O(n) <br />
Memory Complexity: O(n) <br /><br />


Tabulation approach:
```
def fibo(n):
    dp = [0] * (n + 1)

    # Storing the independent values in dp
    dp[0] = 0
    dp[1] = 1

    # Using the bottom-up approach
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = 5
print(fibo(n))
```