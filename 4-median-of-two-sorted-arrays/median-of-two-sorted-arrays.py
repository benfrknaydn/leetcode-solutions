class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        
        nums1

        """
        if len(nums1)> len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        iTotal= ( len(nums1) + len(nums2) + 1) // 2
        start, end = 0, len(nums1)
        while start <= end:
            i1 = (start+end) // 2
            i2 = iTotal - i1
            if i1 > 0 and nums2[i2] < nums1[i1-1]:
                end = i1 -1 
            elif i1 < len(nums1) and nums1[i1] < nums2[i2 -1]:
                start = i1 +1 
            else:
                left1= nums1[i1 -1] if i1 > 0 else float('-inf')
                left2= nums2[i2-1] if i2 > 0 else float('-inf')
                right1=nums1[i1] if i1 < len(nums1) else float('inf')
                right2=nums2[i2] if i2 < len(nums2) else float('inf')

                if (len(nums1)+ len(nums2)) % 2:
                    return max(left1 , left2)
                else:
                   return (max(left1 , left2) + min(right1 , right2)) / 2.0


