#字典
#字典以{}表示，是用來存放很多鍵跟值的配對，只能由鍵查值，不能用值查鍵

#  key   value
#  鍵      值
# 單字    注釋

dictionary = {"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
print(dictionary)

#查字典
dictionary = {"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
print(dictionary["蘋果"])

#鍵可以是數字
dictionary = {0:"apple",1:"banana",2:"cat",3:"dog"}
print(dictionary[3])

#值也可以是數字
dictionary = {0:9,1:8,2:7,3:6}
print(dictionary[1])
