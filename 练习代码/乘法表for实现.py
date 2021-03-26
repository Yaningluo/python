# coding: utf-8 

"""
!project: code
!file: 乘法表for实现.py
!time: 2021-03-23 下午 07:19
!product_name: PyCharm[
缺点：运行之后会有制表符，end=“”引号中间加空格会导致排版不好看
"""

for i in range(1, 10):
    for a in range(1, i+1):
        print(f"{a}*{i}={i*a}\t", end="")
    print()