#類別class、物件object
class Phone: #class 類別名稱(字首大寫，不得使用空白或底線分隔單字)
    # 建構式                                               注意↓     ↓兩邊都是兩個底線 
    def __init__(self,os,number,is_waterproof): #函式 函式名稱(__init__) (傳入參數也是物件本身(self),定義的資料型態的資訊(os,number,is_waterproof))
        self.os = os #物件本身os屬性 = os
        self.number = number #物件本身number屬性 = number
        self.is_waterproof = is_waterproof #物件本身is_waterproof屬性 = is_waterproof

phone1 = Phone("ios",406,True)
print(phone1.os)
print(phone1.number)

phone2 = Phone("android",476,False)
print(phone2.os)
print(phone2.number)

print("_____________________________________________________________________") #分割線一
#物件函式
class Phone: 
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number 
        self.is_waterproof = is_waterproof 

    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False

    def add(self,num1,num2):
        return num1 + num2

phone1 = Phone("ios",406,True)
print(phone1.is_ios())
print(phone1.add(6,9))

phone2 = Phone("android",476,False)
print(phone2.is_ios())