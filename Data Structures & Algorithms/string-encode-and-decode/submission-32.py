class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        - Need to know length of original string
        - Can split with any character
        '''
        enc_arr = []
        for s in strs:
            size = str(len(s))
            s_enc = "|" + size + "|"+ s
            enc_arr.append(s_enc)
        
        return ''.join(enc_arr)




    def decode(self, s: str) -> List[str]:
        curr = 0
        out = []
        while curr < len(s):
            if s[curr] == "|":
                i = curr + 1

                while i < len(s) and s[i].isdigit():
                    i += 1

                word_len = int(s[curr+1:i])
                start_indx = i+1
                end_indx = start_indx + word_len

                out.append(s[start_indx:end_indx])
                curr = end_indx
            else:
                curr += 1
                #|100string_length_100... 
            
                

        return out
