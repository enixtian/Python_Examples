# coding: utf-8

'''
公共子序列问题(不连续）
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

双指针解法
'''
def isSubsequence(s, t)
    i,j = 0,0
    n,m = len(s), len(t)
    while i < n and j < m:
        if s[i] == t[j]:
            i+=1
        j+=1

    return i==n

  
 '''
 
