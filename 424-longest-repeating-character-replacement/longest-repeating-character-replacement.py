class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq={}
        maxfreq=0
        left=0
        maxlen=0

        for right in range(len(s)):
            char=s[right]
            freq[char]=freq.get(char,0)+1
            maxfreq= max(maxfreq,freq[char])
        

            while (right-left+1)-maxfreq>k:
                freq[s[left]]-=1
                left+=1

            maxlen=max(right-left+1,maxlen)
        return maxlen
            
        