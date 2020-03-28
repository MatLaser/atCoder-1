x = int(input())
res = 0
 
good1000 = x // 500
x500 = x % 500
 
good5 = x500 // 5
 
res = 1000 * good1000 + 5 * good5
print(res)