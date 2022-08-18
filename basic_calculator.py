#基本計算機
name = input("請輸入你的名子: ")
age = input("請輸入你的年紀: ")
print("Hello" + name + "今年" + age +"歲")

#input 預設為字串，所以輸出為:"number1"+"number" -> "8"+"87"=887
number1 = input("第一個數: ")
number2 = input("第二個數: ")
print(number1 + number2)

#改為整數 int
number1 = input("第一個數: ")
number2 = input("第二個數: ")
print(int(number1) + int(number2))

#改為小數 float
number1 = input("第一個數: ")
number2 = input("第二個數: ")
print(float(number1) + float(number2))