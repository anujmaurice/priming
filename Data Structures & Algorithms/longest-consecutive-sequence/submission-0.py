class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        input_set = set(nums)
        largest = 0
        for i in input_set:
            print(i)
            longest = 0
            if i-1 not in input_set:
                longest = longest+1
                j = i+1
                while j in input_set:
                    j = j+1
                    longest = longest+1
            if longest > largest:
                largest = longest
        return largest
        