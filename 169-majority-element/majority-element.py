class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nikki={}
        count=1
        for num in nums:
            if num in nikki:
                nikki[num]+=1
            else:
                nikki[num]=1
        n=len(nums)
        for num,count in nikki.items():
            if count > n/2:
                return num