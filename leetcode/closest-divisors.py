import math


# not optimized - exceeds time limit
class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        pairs = []
        for i in range(num + 2):
            for j in range(num + 2):
                if i * j == num + 1 or i * j == num + 2:
                    pairs.append([i, j])
        pairs.sort(key=lambda pair: abs(pair[0] - pair[1]))
        return pairs[0]


# an optimized solution
class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        for i in range(math.floor(math.sqrt(num + 2)), 0, -1):
            if (num + 1) % i == 0:
                return [i, round((num + 1) / i)]
            if (num + 2) % i == 0:
                return [i, round((num + 2) / i)]
