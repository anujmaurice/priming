class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen: Dict[int, int] = {}
        for n in nums:
            if n in seen.keys():
                return True
            else:
                seen[n] = n
        return False