# Time complexity = O(logn)
# Space complexity = O(1)
# Yes
# No

class Solution:
    def binarySerachFirst(self, nums: List[int], target) -> int:
        low = 0
        high = len(nums) - 1
        while(low<=high):
            mid = low+((high-low)//2)
            if(nums[mid]==target):
                if(mid==0 or nums[mid]>nums[mid-1]):
                    return mid
                else:
                    high = mid - 1 #keep moving left
            elif(nums[mid]>target):
                high = mid-1
            else:
                low = mid+1
        return -1

    def binarySerachLast(self, nums: List[int],low ,high , target):
        while(low<=high):
            mid = int(low+((high-low)//2))
            if(nums[mid]==target):
                if(mid==(len(nums)-1) or nums[mid]<nums[mid+1]):
                    return mid
                else:
                    low = mid + 1. #keep moving right
            elif(nums[mid]>target):
                high = mid-1
            else:
                low = mid+1
        return -1


    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n==0:
            return [-1,-1]
        if(nums[0]>target or nums[n-1]<target):
            
            return [-1,-1]
        first = self.binarySerachFirst(nums,target)
        if(first == -1): 
            return [-1,-1]
        last = self.binarySerachLast(nums,first,n-1,target)
        return (first,last)
        