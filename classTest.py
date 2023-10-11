from typing import List

class Solution:
    def __init__(self, x) -> None:
        self.x = x

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return [0, 1]
    
    def getX(self):
        return self.x

res = Solution(1)
print(res.twoSum([2,7,11,15], 9))
print(res.x)

xcoord = res.getX()
print(xcoord)