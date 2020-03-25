n, m = map(int, input().split())
 
n1 = n - 1
m1 = m - 1
 
res = int((n * n1) / 2 + (m * m1) / 2)
 
print(res)