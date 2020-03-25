def palindrome(string): return 0 if string==string[::-1] else 1
 
s = input()
n = len(s)
 
kai1 = int((n - 1) / 2)
kai2 = int((n + 3) / 2)
 
first = s[0:kai1]
second = s[kai2-1:n]
if palindrome(s) == 0:
    if palindrome(first) == 0:
        if palindrome(second) == 0:
            print('Yes')
            exit()
 
print('No')
 