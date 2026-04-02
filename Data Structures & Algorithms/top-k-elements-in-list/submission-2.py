class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        output = []
        for n in nums:
            count_dict[n] = 1 + count_dict.get(n, 0)

        buckets = [[] for i in range(len(nums)+1)]


        for num, freq in count_dict.items():
            buckets[freq].append(num)

        # 3. Collect the top k elements 
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res