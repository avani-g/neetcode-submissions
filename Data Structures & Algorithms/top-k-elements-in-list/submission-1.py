class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        h = []

        for num, count in d.items():
            heapq.heappush(h, (count, num))
            if len(h) > k:
                heapq.heappop(h)
        
        k_freq = []

        for p in h:
            k_freq.append(p[1])
        
        return k_freq
        