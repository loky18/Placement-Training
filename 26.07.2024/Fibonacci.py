n = int(input("Enter the no.of terms: "))
x, y = 0, 1
co= 0
if n <= 0:
   print("enter a positive integer")
elif n == 1:
   print(f"Fibonacci sequence upto {n} is {x}")
else:
   print("Fibonacci sequence:")
   while co < n:
       print(x)
       t = x + y
       x = y
       y = t
       co+= 1
