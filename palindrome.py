#coding:utf-8

'''
回文字符串相关
'''


'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写,空字符串也定义为有效的回文串
'''
def isPalindrome(s):
    #过滤大小写敏感和非数字和字母的字符
    s = s.lower()
    p_s = ''
    for i in s:
        if i.isalnum():
            p_s = p_s + i
    #用倒序切片翻转字符串和原来的字符串进行比较
    if p_s == p_s[::-1]:
        return True
    else:
        return False
 

'''
给定一个字符串，判断该字符串中是否可以通过重新排列组合，形成一个回文字符串
'''
def canPermutePalindrome(s):
    flag = 0
    dic = {}
  #统计每个字符在字符串中出现的次数
    for i in s:
        dic[i] = s.count(i)
  #计算出现次数为奇数的字符个数
    for j in dic.values():
        if j%2 != 0:
            flag += 1
  #字符串如果可以形成回文，重复次数为奇数的字符不能超过2个
  #如果字符串的字符个数为奇数那么重复次数为奇数的字符只能有1个，如果字符串的字符个数为偶数，那么就不能有重复次数为奇数的字符，因此重复次数为奇数的字符要么为1，要么为0
    return flag < 2
      
      
'''
给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串的长度
'''
def longestPalindrome(s):
    dic = {}
    result = 0
    flag = False
    #统计每个字符在字符串中出现的次数
    for i in s:
        dic[i] = s.count(i)
    #将每个字符出现的次数累加起来，如果该字符出现偶数次，则直接累计，如果出现奇数次，则次数-1再累计。因为一个回文字符串最多只能有一个重复次数为奇数的字符
    for j in dic.values():
        if j%2 == 0:
            result += j
        else:
            result += j-1
            flag = True  #如果出现了重复次数为奇数的字符，则改变标识位
    #整个循环跑完后，每个字符出现的次数都会变成偶数，累加后的次数也是偶数，而如果求最长的回文字符串的话是可以再加一个字符的
    if flag:
        result += 1 
        
    return result
  
  
  '''
  给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。(不能改变字符的顺序)
  '''
def validPalindrome(self, s: str) -> bool:
    def checkPalindrome(low, high):
        #双指针的方式，一个头一个尾，如果相等头前进一个尾后退一个，如果不相等就返回False
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    low, high = 0, len(s) - 1
    while low < high:
        if s[low] == s[high]:
            low += 1
            high -= 1
        else:
            #如果low与high不相等时有两个分支：1.删除low的字符  2.删除high的字符  然后再判断剩下的字符串能否成为回文字符串
            return checkPalindrome(low+1, high) or checkPalindrome(low, high-1)
    return True
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
