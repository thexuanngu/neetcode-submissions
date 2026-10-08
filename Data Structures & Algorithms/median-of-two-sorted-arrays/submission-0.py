class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        if len(A) > len(B):
            A, B = B,A
        total = len(A) + len(B)
        half = total // 2

        l, r = 0, len(A) - 1

        while True:
            i = (r+l) // 2
            j = half - i - 2
            ALeft = A[i] if i >= 0 else float('-inf')
            ARight = A[i+1] if i < len(A)-1 else float('inf')
            BLeft = B[j] if j >= 0 else float('-inf')
            BRight = B[j+1] if j < len(B)-1 else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 0:
                    return (min(ARight, BRight) + max(ALeft, BLeft)) / 2;
                return min(ARight, BRight)

            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1