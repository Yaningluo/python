# coding: utf-8 

"""
!project: code
!file: 三角形周长和面积.py
!time: 2021-03-22 下午 09:41
!product_name: PyCharm
"""

side_1 = float(input('输入第一条边：'))
side_2 = float(input('输入第二条边：'))
side_3 = float(input('输入第三条边：'))
if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
    s = (side_1 + side_2 + side_3) / 2
    print('oo')