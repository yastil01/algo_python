'''
Merge sort:
Time complexity: O(nlogn)
Space complexity: O(n)
'''
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l1, l2):
            res = [] 
            p1 = p2 = 0
            
            while p1 < len(l1) and p2 < len(l2):
                if l1[p1] < l2[p2]:
                    res.append(l1[p1])
                    p1 += 1
                else:
                    res.append(l2[p2])
                    p2 += 1
            
            while p1 < len(l1):
                res.append(l1[p1])
                p1 += 1
            
            while p2 < len(l2):
                res.append(l2[p2])
                p2 += 1
                
            return res
        
        n = len(nums)
        if n == 1:
            return nums
        
        sorted_left = self.sortArray(nums[:n//2])
        sorted_right = self.sortArray(nums[n//2:])
        
        return merge(sorted_left, sorted_right)
