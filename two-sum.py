class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_dict = {}
        for i in range(len(nums)):
            if nums[i] not in map_dict:
                map_dict[target - nums[i]] = i
            else:
                return map_dict[nums[i]],i