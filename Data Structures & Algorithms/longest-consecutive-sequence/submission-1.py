class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        # num : sequence length
        nums_dict = {}

        for num in nums:
            nums_dict[num] = 1
        
        for num in nums:
            if num - 1 not in nums_dict:
                counter = 1
                while num + counter in nums_dict:
                    counter += 1
                nums_dict[num] = counter
        
        return max(nums_dict.values())
