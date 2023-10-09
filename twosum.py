class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        hsh = {}
        for i in range(len(nums)):
            hsh[nums[i]]=i
        for i in range(len(nums)):
            j = target-nums[i]
            if j in hsh and i != hsh[j]:
                return [i,hsh[j]]
            