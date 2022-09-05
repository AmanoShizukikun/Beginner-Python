#問答程式
#請搭配QA_question一起看

from QA_question import Question #從QA_question.py只引入Question這個東西
import QA_question #引入QA_question.py的全部檔案

test = [
    "誰不是三合音的創始成員?\n(a) 勃起\n(b) 葳仔\n(c) 邱寬\n\n",
    "天野靜樹不會寫哪一種程式語言?\n(a) JavaScript\n(b) Python\n(c) C++\n\n",
    "哪首歌不是在天野しずき的頻道而是在T.I.M ACG發布的?\n(a) ラグトレイン\n(b) ヴァンパイア\n(c) 酔いどれ知ら\n\n"
]

#將問題存入列表，再變成QA_question自訂的資料型態Question(題目,答案)
questions = [
    Question(test[0],"c"),
    Question(test[1],"a"),
    Question(test[2],"b")
]

#運作函式
def run_test(questions):
    score = 0 #初始化分數
    for QA_question in questions: #for迴圈，將questions列表中的值一個一個傳到QA_question
        answer = input(QA_question.description) #從資料型態讀取並顯示題目，並將答案變數 = 輸入答案 
        if answer == QA_question.answer: #當答案變數 = 資料型態儲存的答案
            score += 1 #加分
    
    print("你得到" + str(score) + "分，共" + str(len(questions)) + "題")

#呼叫函式run_test(執行程式)
run_test(questions)