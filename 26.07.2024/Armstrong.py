n= int(input("Enter a number: "))
s = 0
temp = n
while temp > 0:
   d = temp % 10
   s += d ** 3
   temp //= 10
if n == s:
   print(f"{n}is an Armstrong number")
else:
   print(f"{n}is not an Armstrong number")
