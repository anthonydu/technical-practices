class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


# marginally faster runtime
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        while 1:
            try:
                nums.remove(val)
            except:
                break
        return len(nums)


# another one
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)
