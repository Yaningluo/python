# coding: utf-8

"""
!time: 2021-03-23 下午 07:50
!project: code
"""
x = 1
y = 1
while x <= 9:
    y =1
    while y <= x:
        print(f"{y}*{x}={y*x}\t", end="")
        y +=1
    print()
    x += 1
#    print()
