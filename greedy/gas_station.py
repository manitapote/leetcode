
from typing import List
def gas_station(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1

    start = tank = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            start, tank = i+1, 0

    return start

gas = [2, 5, 1, 3]
cost = [3, 2, 1, 4]
print(gas_station(gas, cost))


#case 1: if total gas is less than total cost, there is no solution
#Case 2: If total gas is greater than total cost, there exist atleast a
#Solution that leads to circular travel