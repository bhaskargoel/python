n= 9
a = 1
b = 1
for a in range(n+1):
    if a%2 != 0:
        val = (n - a) // 2
        print (" "*val + "*"*(a) + " "*val ,end = "\n")
for b in range(n-1,0,-1):
    if b%2 != 0:
        val2 = (n-b)//2
        print (" "*val2 + "*"*(b) + " "*val2 ,end = "\n")
print()
