from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums).items()
        buckets = [ [] for _ in range(0, len(nums)) ]

        for num, count in counts:
            buckets[count-1].append(num)
        
        ans = []

        for count in range(len(nums), 0, -1):
            for num in buckets[count-1]:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return ans
