
# 請設計一個函數，輸入為數字，輸出則為*符號為輸入數字邊長的空心正三角形。
# 輸入: 6


def do(num):
 for i in range(2,num+1):

   if i==2:
        print("\n" +" "*(num-1)+"*")
   if i==6:
        print((" "*(num-i)+"*"+" ")*i)
   else:
        print(" "*(num-i)+"*"+" "*(2*i-3)+"*")#其余行按照如下规律打印空格和*

num = int(input('Input:')) 
do(int(num))