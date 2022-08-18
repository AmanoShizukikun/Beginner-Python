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