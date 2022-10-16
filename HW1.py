
# 請設計一個函數，輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形。
# 輸入: 6


def do(num):
 for i in range(1,num+1):

   if i==1:
        print("\n" +" "*(num)+"*")#第一個
   if i==num:
        print(("*"+" ")*i+"*") #最後一個
   else:
        print(" "*(num-i)+"*"+" "*(2*i-1)+"*") #其餘的排數

num = int(input('Input:')) 
do(int(num))