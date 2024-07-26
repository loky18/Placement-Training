n = int(input("Enter a number: "))
temp = n
re = 0
while temp > 0:
    remainder = temp % 10
    re = (re * 10) + remainder
    temp = temp // 10
if n == re:
  print('Palindrome')
else:
  print("Not Palindrome")
