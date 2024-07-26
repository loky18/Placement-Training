def ch(a,b):
    if(sorted(a)== sorted(b)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
x= input("Enter string1: ")
y= input("Enter string2: ")
ch(x,y)
