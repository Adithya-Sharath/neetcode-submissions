from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sort = dict(Counter(nums).most_common())
        ls=[]
        ls = list(sort.keys())[:k]
        return ls
