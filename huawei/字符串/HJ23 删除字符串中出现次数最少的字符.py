"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
@Time        : 2022/3/24 21:35
@File        : HJ23 删除字符串中出现次数最少的字符.py
"""


def delString(str):
    """
    实现删除字符串中出现次数最少的字符，若出现次数最少的字符有多个，则把出现次数最少的字符都删除。输出删除这些单词后的字符串，字符串中其它字符保持原来的顺序。
    数据范围：输入的字符串长度满足 1 \le n \le 20 \1≤n≤20  ，保证输入的字符串中仅出现小写字母
    输入描述：
    字符串只包含小写英文字母, 不考虑非法输入，输入的字符串长度小于等于20个字节。

    输出描述：
    删除字符串中出现次数最少的字符后的字符串。
    :param str:
    :return:
    """
    record = {}
    for i in range(len(str)):
        s = str[i]
        if s not in record:
            record[s] = 1
        else:
            record[s] += 1
    min_val = min(record.values())

    new_str = ''
    for s in range(len(str)):
        if record[str[s]] != min_val:
            new_str +=  str[s]

    return new_str


print(delString('aabcdddc'))
