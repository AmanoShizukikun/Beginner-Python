#if判斷句
#第一種情況:如果A就a
#如果肚子餓就去吃飯
hungry = True
if hungry:
    print("吃飯")

#第二種情況:如果A就a，否則B就b
#如果肚子餓就去吃飯，否則就不吃
hungry = False
if hungry:
    print("吃飯")
else:
    print("不吃")

#第三種情況:如果A就a，或是如果B就b，否則C就c
#如果你考100分就給獎勵，或是如果你考60分以上就不懲罰，否則就懲罰
score = 90
if score == 100:
    print("給獎勵")
elif score >= 60:
    print("不懲罰")
else:
    print("懲罰")

#第四種情況:如果A「且」B就ab，否則C就c
#如果你考100分「且」我心情好就給獎勵，否則就懲罰
score = 90
happy = True
if score == 100 and happy:
    print("給獎勵")
else:
    print("懲罰")

#第五種情況:如果A「或」B就ab，否則C就c
#如果你考100分「或」我心情好就給獎勵，否則就懲罰
score = 90
happy = True
if score == 100 or happy:
    print("給獎勵")
else:
    print("懲罰")

#第六種情況:如果A「或沒有」B就ab，否則C就c
#如果你考100分「或沒有」生氣就給獎勵，否則就懲罰
score = 90
angry = True
if score == 100 or not angry:
    print("給獎勵")
else:
    print("懲罰")

#第七種情況:如果沒有A「或沒有」B就ab，否則C就c
#如果沒有考100分「或沒有」生氣就懲罰，否則就給獎勵
score = 90
angry = False
if score != 100 or not angry:
    print("懲罰")
else:
    print("給獎勵")

print("_____________________________________________________________________") #分割線一
#練習題一
#設一個函式max_num，輸入三個數字並回傳最大值(解法不只一種)

#解法一
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(2,4,6))

#解法二
def max_num(num1,num2,num3):
    max = [num1,num2,num3]
    max.sort()
    return(max[2])

print(max_num(5,9,7))
