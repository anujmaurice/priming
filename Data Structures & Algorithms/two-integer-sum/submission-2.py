class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers: defaultdict[int, List] = defaultdict(list)
        returnlist: List[int] = []
        for i, n in enumerate(nums):
            numbers[n].append(i)

        for i, n in enumerate(nums):

            diff_num = target - n

            if diff_num in numbers.keys():
                index_list = numbers.get(diff_num)
                if index_list:
                    index = index_list[0]
                    numbers[diff_num] = index_list[1:]
                    if i == index and not numbers[diff_num]:
                        continue
                    if (i == index) and numbers[diff_num]:
                        index_list = numbers.get(diff_num)
                        index = index_list[0]
                        numbers[diff_num] = index_list[1:]
                    print(i, n, "----", index, diff_num, numbers[diff_num])
                    returnlist.extend([i,index])
                    return returnlist

        return returnlist
