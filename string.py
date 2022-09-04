#字串
#1.換行 : \n
print("你好 \n天野靜月")

#2.在字串打引號(告訴Python\後的符號不是字串的範圍而是內容) : \
print("你好 \"天野靜月\"")

#3.兩個字串相連 : +
print("你好 " + "天野靜月")

#4.字串變數相連 : +
name = "天野靜月"
print("你好" + name)

print("_____________________________________________________________________") #分割線一
#字串常用函式(function)
#1.字串改小寫 : 字串.lower
phrase = "Hello AMSK"
print(phrase.lower())

#2.字串改大寫 : 字串.upper
phrase = "Hello AMSK"
print(phrase.upper())

#3.判斷字串內容是否全為大寫(小寫)，如果是回傳布林True反之則False : 字串.isupper (字串.islower)
phrase = "Hello AMSK"
print(phrase.isupper())
print(phrase.islower())

#4.字串函式疊加
phrase = "Hello AMSK"
print(phrase.lower().islower())

#5.指定輸出字串位置內容 : 字串[數字]
#Python第一位為0，且空格也會被算入字串
phrase = "Hello AMSK"
         #0123456789
print(phrase[0]) 
print(phrase[6]) 

#6.自字串裡尋找指定內容 : 字串.index("指定內容")
#只會找第一個相符的內容顯示數字
phrase = "Hello AMSK"
         #0123456789
print(phrase.index("H"))
print(phrase.index("l"))

#7.將字串內容A替換成B : 字串.replace("A","B")
#會將全部相符的內容替換
phrase = "Hello AMSK"
         #0123456789
print(phrase.replace("H","h"))
print(phrase.replace("l","L"))