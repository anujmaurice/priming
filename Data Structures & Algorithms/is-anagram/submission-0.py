class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict: defaultdict[str, int] = defaultdict(int)
        t_dict: defaultdict[str, int] = defaultdict(int)

        for e in s:
            s_dict[e] += 1
        for e in t:
            t_dict[e] += 1
        
        if s_dict != t_dict:
            return False
        else:
            return True