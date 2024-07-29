def Leap(a):  
  if((a%400==0) or (a%100!=0) and (a%4==0)):   
    print("Given Year is a leap Year");   
  else:  
    print("Given Year is not a leap Year")   
y=int(input("Enter the number: "))   
Leap(y)  
