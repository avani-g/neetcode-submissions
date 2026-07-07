class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        sorted_items = sorted(d.items(), key= lambda x: x[1], reverse=True)

        k_freq = []

        for i in range(k):
            k_freq.append(sorted_items[i][0])
        
        return k_freq
        