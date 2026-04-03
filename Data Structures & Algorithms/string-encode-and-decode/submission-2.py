class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        delimit = "~"
        for s in strs:
            block = f"{len(s)}{delimit}{s}"
            output = output + block
        print("Encode",output)
        return output

    def decode(self, s: str) -> List[str]:
        decoded_out = []
        delimit = "~"
        while s:
            meta = s[:2]
            #len_meta = int(s[0])
            len_meta = int(s.split(delimit)[0])
            lefttrimmed = delimit.join(s.split(delimit)[1:])
            word = lefttrimmed[:len_meta]
            decoded_out.append(word)
            s = lefttrimmed[len(word): ]
        return decoded_out