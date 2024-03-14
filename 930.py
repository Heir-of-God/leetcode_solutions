class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        # counting subarrs with cur_sum <= target
        def count_subarrs(target):
            if target == -1:
                return 0
            l_pointer = cur_sum = 0
            result = 0

            for r_pointer in range(0, len(nums), 1):
                cur_sum += nums[r_pointer]
                while cur_sum > target:
                    cur_sum -= nums[l_pointer]
                    l_pointer += 1
                result += r_pointer - l_pointer + 1

            return result

        return count_subarrs(goal) - count_subarrs(goal - 1)
