#for迴圈
#for 變數 in 字串或列表:
#   要重複執行的程式碼

for letter in "大家好我叫天野靜樹":
    print(letter)

for num in [2,4,6,8]:
    print(num)

print("_____________________________________________________________________") #分割線一
#range函式
for num in range(5): #從零重複5次 -> 0,1,2,3,4
    print(num)

for num in range(2,7): #從2印到6 -> 2,3,4,5,6
    print(num)

print("_____________________________________________________________________") #分割線二
#練習題一
#設一函式power用for迴圈做出和下列程式功能一樣的函式
print(pow(2,6)) #2的6次方

print("_____________________________________________________________________") #分割線三
#解答
def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num-1):
        result = result * base_num
    return result

print(power(2,6))
