#函式
#函式的定義:函式是預先寫好的程式碼，當我們要使用他的時候才會被執行，函式幫我們做資料處理或運算然後回傳我們想要的資訊
#函式分為兩個部分，第一個是函式的定義，第二個是函式的呼叫
#必須先定義函式才能呼叫函式

def hello(): #def 函式名稱(命名規則和變數一樣請參考datatypes_and_variables.py)
    print("hello") #定義函式的內容:輸出hello

hello() #呼叫函式

def helloname(name):
    print("hello" + name)

helloname("靜樹")

def hellonameage(name,age):
    print("hello" + name + "你今年" + age + "歲")

hellonameage("靜樹","19") 
#注意數字無法和字串相加所以輸入必須是字串否則會報錯

#解決方法一
hellonameage("靜樹",str(19)) #從輸入解決

#解決方法二
def hellonameage(name,age):
    print("hello" + name + "你今年" + str(age) + "歲") #從函式解決

hellonameage("靜樹",19)

print("_____________________________________________________________________") #分割線一
#練習題一
#定義一個函式add，傳入兩個值並使其相加

def add(num1,num2):
    print(num1 + num2)

add(1,2)

# return 用法
#當函式碰到return，會將呼叫的值覆蓋成return的值
def add(num1,num2):
    return 10

add(1,2) #被return覆蓋變為10(不會印出)

#證明
print(add(1,2))#印出被return覆蓋變為10

#應用到練習題
def add(num1,num2):
    return num1 + num2

print(add(1,2))

#Q:為甚麼要用return? Ans:因為在寫程式的時候有時後回傳的值需要進一步的做處理，單純的print(印出)無法對值的內容進行下一步的更改

print("_____________________________________________________________________") #分割線二
#練習題二
#請回答下列程式輸出結果

def add(num1,num2):
    print(num1 + num2) #印出3+4所以解果為7
    return 5 #覆蓋add(3,4)改為5

value = add(3,4)
print(value)

#輸出結果
#7
#5

print("_____________________________________________________________________") #分割線二
#練習題二延伸
#請回答下列程式輸出結果

def add(num1,num2):
    print(num1 + num2) #印出3+4所以解果為7

value = add(3,4)
print(value)

#輸出結果
#7
#None

#Q:為甚麼是None? Ans:如果函式沒有return的話Python會自動將return設為None

print("_____________________________________________________________________") #分割線三
#當函式碰到return就會結束

def add(num1,num2):
    print(num1 + num2) #印出3+4所以解果為7
    return 5 #覆蓋add(3,4)改為5
    print("你好") #因為當函式碰到return就會結束所以不會輸出"你好"

value = add(3,4)
print(value)