class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_prod: list[int] = [1 for _ in range(len(nums))]
        prefix_prod[0] = nums[0]
        for ind in range(1, len(nums), 1):
            prefix_prod[ind] = prefix_prod[ind - 1] * nums[ind]

        suffix_prod: list[int] = [1 for _ in range(len(nums))]
        suffix_prod[-1] = nums[-1]
        for ind in range(-2, -len(nums) - 1, -1):
            suffix_prod[ind] = suffix_prod[ind + 1] * nums[ind]

        res: list[int] = [suffix_prod[1]]
        for ind_num in range(1, len(nums) - 1, 1):
            res.append(prefix_prod[ind_num - 1] * suffix_prod[ind_num + 1])
        res.append(prefix_prod[-2])

        return res


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res: list[int] = [1 for _ in range(len(nums))]
        prefix_prod: int = 1
        sufix_prod: int = 1
        l_pointer: int = 0
        r_pointer: int = len(nums) - 1

        for _ in range(len(nums)):
            res[l_pointer] *= prefix_prod
            res[r_pointer] *= sufix_prod

            prefix_prod *= nums[l_pointer]
            sufix_prod *= nums[r_pointer]

            l_pointer += 1
            r_pointer -= 1

        return res
