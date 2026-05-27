class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for num in range(0, n):
                nums1[num] = nums2[num]
            return
        if n == 0:
            return
        
        mp = m-1
        np = n-1

        for i in range(m+n-1, -1, -1):
            if mp == -1:
                nums1[i] = nums2[np]
                np -= 1
            elif np == -1:
                nums1[i] = nums1[mp]
                mp -= 1
            elif nums1[mp] >= nums2[np]:
                nums1[i] = nums1[mp]
                mp -= 1
            else:
                nums1[i] = nums2[np]
                np -= 1
        
