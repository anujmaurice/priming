class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict: defaultdict[str, List[str]] = defaultdict(list)
        # res = []
        for s in strs:
            # 1. Sort the string 's' and join it back into a string
            sorted_s = "".join(sorted(s)) 

             # 2. Get the current list for that sorted key
            entry_in_dict = sort_dict[sorted_s]

            # 3. Add the original string to that list
            entry_in_dict.append(s)

        return list(sort_dict.values())
        