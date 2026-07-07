class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums == []:
            return []

        prefix = [1]
        suffix = [1]

        current_product = 1
        for num in nums:
            current_product *= num
            prefix.append(current_product)
        
        current_product = 1
        for num in reversed(nums):
            current_product *= num
            suffix.append(current_product)
        
        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[len(nums) - 1 - i])
        
        return ans


        