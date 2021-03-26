# coding: utf-8

"""
!time: 2021-03-23 下午 08:01
!project: code
"""
for i in range(100, 1000):
    a = i % 10  # 取到个位数
    b = i // 10 % 10  # 取到十位数
    c = i // 100  # 取到百位
    if(a ** 3 + b ** 3 + c ** 3) == i:
        print(i)