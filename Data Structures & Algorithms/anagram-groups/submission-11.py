class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        done = set()

        for idx1, s1 in enumerate(strs):        
            curr = [s1]
            if idx1 in done:
                continue
            
            for idx2, s2 in enumerate(strs):
                if idx1 == idx2 or len(s2) != len(s1) or idx2 in done:
                    continue

                s_count = Counter(s1)
                isAna = True

                for c in s2:                  
                    s_count[c] -= 1
                
                for count in s_count.values():
                    if count != 0:
                        isAna = False

                if isAna:
                    curr.append(s2)
                    done.add(idx2)
            
            out.append(curr)
            done.add(idx1)
        
        return out
                


        