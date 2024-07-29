def calculate(x,y):   
    if x>y:  
        smaller=y  
    else:  
        smaller=x  
    for i in range(1,smaller+1):  
        if((x%i==0) and (y%i==0)):  
            hcf=i  
    return hcf   
n1=int(input("Enter first number: "))  
n2=int(input("Enter second number: "))  
print("The HCF of",n1,"and",n2,"is",calculate(n1,n2)) 
