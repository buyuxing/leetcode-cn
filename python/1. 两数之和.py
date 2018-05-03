'''
https://leetcode-cn.com/problems/two-sum/description/
1. 两数之和
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

def twoSum(nums, target):
    hash = {}
    for (i, x) in enumerate(nums):
        y = target - x
        if(y in hash):
            return [hash[y], i]
        else:
            hash[x] = i
            
def main():
    print(twoSum([3,2,3], 6))

if __name__ == '__main__':
    main()