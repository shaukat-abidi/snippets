# https://leetcode.com/problems/maximum-subarray
from typing import List
'''
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 105
-10^4 <= nums[i] <= 10^4

'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        local_sum = -100000 # Minimum as per constraint 
        global_sum = float('-inf')
        for ind, val in enumerate(nums):
            local_sum = max(val, local_sum + val)
            global_sum = max(local_sum, global_sum)
            print(f"At index-{ind}: local_Sum:{local_sum}, global_sum:{global_sum}")
        
        return global_sum
        

if __name__ == '__main__':
    sol = Solution()
    nums = [5,4,-1,7,8]
    print(sol.maxSubArray(nums))
        
