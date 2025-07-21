class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        nikki=s.strip().split()[-1]
        return len(nikki)