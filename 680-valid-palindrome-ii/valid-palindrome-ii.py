class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return (self.is_valid(s, left + 1, right) or 
                        self.is_valid(s, left, right - 1))
            left += 1
            right -= 1
        return True

    # --- MOVE EVERYTHING BELOW TO THE LEFT ---
    def is_valid(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True