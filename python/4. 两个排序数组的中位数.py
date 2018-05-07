'''
https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
4. 两个排序数组的中位数

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2 。

请找出这两个有序数组的中位数。要求算法的时间复杂度为 O(log (m+n)) 。

示例 1:

nums1 = [1, 3]
nums2 = [2]

中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

中位数是 (2 + 3)/2 = 2.5

>>> nums1 = [1, 3]
>>> nums2 = [2]
>>> findMedianSortedArrays(nums1, nums2)
2

>>> nums1 = [1, 2]
>>> nums2 = [3, 4]
>>> findMedianSortedArrays(nums1, nums2)
2.5
'''

def findMedianSortedArrays1(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    l = m + n
    nums3 = []
    if m == 0 and n == 0:
        return None
    else:
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                nums3.append(nums1[i])
                i+=1
            else:
                nums3.append(nums2[j])
                j+=1
    nums3 += nums1[i:]
    nums3 += nums2[j:]
    if l % 2 == 0:
        return (nums3[l//2 - 1] + nums3[l//2])/2
    else:
        return nums3[l//2]
        

def findMedianSortedArrays(nums1, nums2):
    l = (nums1 + nums2).sort()
    count = len(l)
    if count % 2 == 0:
        return (l[count//2]+l[count//2-1])/2
    else:
        return l[count//2]

if __name__=='__main__':
    import doctest
    doctest.testmod()