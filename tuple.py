#元組 
#元組跟列表很類似，元組是()，列表是[]

scores = (90,70,50,80,60)
print(scores[0]) #輸出為90
print(scores[0:2]) #輸出為90,70

#Q1:元組和列表的差別在哪裡呢? Ans:元組創建後就無法被修改
#錯誤示範

#scores = (90,70,50,80,60)
#scores[0] = 30
#print(scores)

#輸出結果type error

#Q2:為甚麼我們需要元組? Ans:防止資料被「意外」修改