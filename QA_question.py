#請搭配QA_pratice一起看

class Question: #自訂資料型態Question
    def __init__(self,description,answer): #資料屬性(物件本身,題目,答案) → Question呼叫值(description,answer)
        self.description = description
        self.answer = answer