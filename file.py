# 檔案讀取、寫入

#open("檔案路徑" , mode = "開啟模式" , encoding = "編碼格式")

#檔案路徑分為:絕對路徑、相對路徑
#絕對路徑 檔案在電腦的固定位置 例如: D:/code-respository/Beginner-Python/file_readtest.txt
#相對路徑 以程式位置尋找文件位置 例如: file_readtest.txt

#開啟模式分為:讀取、覆寫、續寫
#讀取: r
#覆寫: w
#續寫: a

#編碼格式
#預設格式不支援中文，如果要用中文的話可以用 utf-8 格式

print("_____________________________________________________________________") #分割線一
#讀取並印出文件的全部內容
file = open("file_readtest.txt" , mode = "r")
print(file.read()) #將讀取到的文件的內容全部印出
file.close() #關閉檔案(避免佔用資源)

#讀取並印出文件的沒印出過的的第一行內容
file = open("file_readtest.txt" , mode = "r")
print(file.readline()) #將讀取到的文件印出沒印出過的的第一行內容
print(file.readline()) #將讀取到的文件印出沒印出過的的第一行內容
file.close() #關閉檔案(避免佔用資源)

#讀取並逐行印出文件的全部內容
file = open("file_readtest.txt" , mode = "r")
for line in file:
    print(line)
file.close() #關閉檔案(避免佔用資源)

#讀取並印出文件的沒印出過的的第一行內容
file = open("file_readtest.txt" , mode = "r")
print(file.readlines()) #將讀取到的所有文件內容放入列表並印出
file.close() #關閉檔案(避免佔用資源)

print("_____________________________________________________________________") #分割線二
#覆寫
file = open("file_writetest.txt" , mode = "w")
file.write("hello") #寫入內容
file.close() #關閉檔案(避免佔用資源)

#續寫
file = open("file_writetest.txt" , mode = "a" , encoding = "utf-8")
file.write("\n天野靜樹") #寫入內容
file.close() #關閉檔案(避免佔用資源)

print("_____________________________________________________________________") #分割線三
#延伸:自動關閉檔案
#每次都要關閉檔案會導致程式很亂，不然忘記關會占用資源
with open("file_writetest.txt" , mode = "a" , encoding = "utf-8") as file: #出了with就會自動close
    file.write("\n自動關閉真方便")