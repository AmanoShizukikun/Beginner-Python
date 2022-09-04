#每次新增一個變數很麻煩
score1 = 90
score2 = 70
score3 = 50
score4 = 80
score5 = 60
print(str(score1) + str(score2) + str(score3) + str(score4) + str(score5))

#上面的變數可以透過列表簡化為下式
scores = [90,70,50,80,60]
print(scores)

#也可以存文字
friends = ["勃起","葳仔","邱寬"]
print(friends)

#也存放布林值
things = [True,False]
print(things)

#也可以混在一起
allthings = [90,"靜月",True]
print(allthings)

#輸出列表中的指定內容(-1代表倒數第一位 -> -x代表倒數第x位 )
scores = [90,70,50,80,60]
print(scores[0])
print(scores[-1])

#輸出列表中的x~y範圍內的內容(列表[x起始數字:y結尾數字(不包含y)])
scores = [90,70,50,80,60]
print(scores[0:2])
print(scores[1:4])

#輸出列表中的x範圍以後的內容(列表[x起始數字:])
scores = [90,70,50,80,60]
print(scores[1:])

#輸出列表中的y範圍以前的內容(列表[:y結尾數字(不包含y)])
scores = [90,70,50,80,60]
print(scores[:4])

#字串應用
phrase = "Hello Amano Shizuki"
print(phrase[6])
print(phrase[0:6])
print(phrase[6:])

#更改列表內容
scores = [90,70,50,80,60]
print(scores)
scores[0] = 30 
print(scores)

#延伸列表 : A列表.extend(B列表)
scores = [90,70,50,80,60]
friends = ["勃起","葳仔","邱寬"]
scores.extend(friends)
print(scores)

#延伸列表 : 列表.append(值)
scores = [90,70,50,80,60]
scores.append(30)
scores.append(True)
scores.append("右承")
print(scores)

#插入列表 : 列表.insert(插入位置,值)
scores = [90,70,50,80,60]
scores.insert(2,30) #將30插入第3位
print(scores)

#移除列表指定內容 : 列表.remove(值)
scores = [90,70,50,80,60]
scores.remove(50)
print(scores)

#清空列表 : 列表.clear()
scores = [90,70,50,80,60]
scores.clear()
print(scores)

#移除列表最後一位 : 列表.pop()
scores = [90,70,50,80,60]
scores.pop()
print(scores)

#小到大排列列表 : 列表.sort()
scores = [90,70,50,80,60]
scores.sort() #排列所以結果為[50, 60, 70, 80, 90]
print(scores)

#反轉列表 : 列表.reverse()
scores = [90,70,50,80,60]
scores.reverse() #反轉所以結果為[60, 80, 50, 70, 90]
print(scores)

#回傳指定內容在列表中的位置 : 列表.index(值)
scores = [90,70,50,80,60]
print(scores.index(50)) #50在第三位所以回傳2

#回傳列表中指定內容有機個 : 列表.count(值)
scores = [90,70,50,80,60]
print(scores.count(50)) #因為只有1個50所以回傳1
scores = [90,70,50,80,60,50,50]
print(scores.count(50)) #同上回傳3