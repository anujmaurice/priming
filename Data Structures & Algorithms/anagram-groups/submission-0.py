class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sort_dict: defaultdict[str, List[str]] = defaultdict(list)
        # res = []
        for s in strs:
            entry_in_dict = sort_dict["".join(sorted(s))]
            entry_in_dict.append(s)
            sort_dict["".join(sorted(s))] = entry_in_dict

        return list(sort_dict.values())
        