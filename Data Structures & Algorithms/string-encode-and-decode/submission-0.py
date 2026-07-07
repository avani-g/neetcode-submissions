class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for s in strs:
            str_len = str(len(s))
            if len(s) < 10:
                str_len = "0" + str_len
            if len(s) < 100:
                str_len = "0" + str_len
            
            encoded += str_len + s
        
        return encoded

    def decode(self, s: str) -> List[str]:

        strs = []

        while s != "":
            curr_length = int(s[:3])
            strs.append(s[3 : 3 + curr_length])
            s = s[3 + curr_length:]
        
        return strs



