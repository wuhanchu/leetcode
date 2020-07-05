#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
import math
max_value =  math.pow(2,31)  

class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            value = str(x)[1:][::-1]
        else:
            value = str(x)[::-1]

        value = int(value)

        if abs(value) > max_value:
            return 0
        elif x< 0:
            return -1*value
        else:
            return value

# @lc code=end
