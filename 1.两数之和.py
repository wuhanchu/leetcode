#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target: int):
        value_map = {}
        for index, value in enumerate(nums):
            value_distance = target - value

            if value_map.get(value_distance) is not None:
                return [value_map.get(value_distance), index]
            else:
                value_map[value] = index
# print(Solution().twoSum([2, 7, 11, 15], 9))