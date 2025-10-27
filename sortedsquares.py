class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        result = [0]*len(nums)
        pos = len(nums)-1
        
        while right >= left:
            leftsq = nums[left] ** 2
            rightsq = nums[right] ** 2
            if leftsq >= rightsq:
                result[pos] = leftsq
                left += 1
                pos -= 1
            else:
                result[pos] = rightsq
                right -= 1
                pos -= 1
                
        return result
