#模組 module
#可以將.py檔引入當成一個模組使用

#tool裡的變數
#name = "靜月"
#age = 19

#tool裡的函式
#3個數取最大值函式
#def max_num(num1,num2,num3):
#    max = [num1,num2,num3]
#    max.sort()
#    return(max[2])


#引入模組 import .py檔
import tool 

#使用模組中的變數 : 模組.變數
print(tool.name) #印出tool模組中的name變數 tool模組 裡面的 name變數 = "靜月" 所以輸出為 靜月
print(tool.age) #印出tool模組中的age變數

#使用模組中的函式 : 模組.函式()
print(tool.max_num(2,4,6))

print("_____________________________________________________________________") #分割線一
#尋找內建模組的方法
import sys
print(sys.path)
#終端機中lib結尾的路徑就是內建模組的路徑

print("_____________________________________________________________________") #分割線二
#使用第三方模組
#假設要使用numpy步驟如下:
#1.Google收尋numpy
#2.點install
#3.按照步驟使用pip套件管理工具，在終端機輸入: pip install numpy


#模組改名 : import 模組 as 改名
#如果模組名稱不好記可以將模組改名 例如:
import tool as tl
#這樣想使用模組時就可以直接寫改名 如:
print(tl.name)