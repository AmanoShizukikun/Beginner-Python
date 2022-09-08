#猜數字遊戲
#1.數字範圍0~99
#2.每一次都會給大一點或小一點的提示
#3.猜錯三次就輸了
#4.要用到while迴圈

import random

secret_num = (random.randint(0,99))
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("請輸入數字: "))
        if guess > secret_num:
            print("小一點")
        elif guess < secret_num:
            print("大一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("你輸了")
else:
    print("你贏了")