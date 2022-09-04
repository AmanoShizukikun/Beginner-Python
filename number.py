from math import *
import math
#數字
#1.基本數字
print(92)
print(-1.14)

#2.加減乘除
print(9+2)
print(1-14)
print(4*8)
print(6/9)

#3.除法只取整數
print(6//9)

#4.Python有先乘除後加減也可以用括號優先加減
print(4+8+6*9)
print(4+(8+6)*9)

#5.變數用法
number = 8
print(number*5)

#6.取餘數 : %
number = 8
print(number%5)

print("_____________________________________________________________________") #分割線一

#數字常用函式
#1.數字轉字串 : str(數字)
number = 8
print(str(number))
print("會印出數字" + str(number))

#2.取絕對值 : abs(數字)
number = 8
print(abs(number))
number = -8
print(abs(number))

#3.算次方 : pow(基數,次方)
print(pow(2,4))

#4.取最大值 : max(數字,數字...)
print(max(8,7,6,9))

#5.取最小值 : min(數字,數字...)
print(min(8,7,6,9))

#6.取四捨五入 : round
print(round(4.4))
print(round(4.6))

#7.無條件捨去 : floor
print(floor(6.9))

#8.無條件進位 : ceil
print(ceil(5.1))

#9.開根號 :sqrt
print(sqrt(9))