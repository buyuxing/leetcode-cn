'''
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
3.无重复字符的最长子串
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
'''

def lengthOfLongestSubstring1(s):
    r = 0
    sub = ''
    for c in s:
        i = sub.find(c)
        if i == -1:
            sub = sub + c
        else:
            r = max(r, len(sub))
            sub = sub[i+1:]+c
    else:
        r = max(r, len(sub))
    return r

def lengthOfLongestSubstring2(s):
    r = 0
    hash = {}
    start = 0
    for (i,c) in enumerate(s):
        if c not in hash or hash[c] < start:
            pass
        else:
            r = max(r, i - start)
            start = hash[c] + 1
        hash[c] = i
    else:
        r = max(r, i - start + 1)
    return r

def main():
    s="abcabcbb"
    print(lengthOfLongestSubstring1(s))

if __name__ == '__main__':
    main()