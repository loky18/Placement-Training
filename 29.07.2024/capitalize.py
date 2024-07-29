l=input("Enter the sentence : ")
m=l.split()
t=[]
for i in m:
        if i[0].islower():
            t.append(i[0].upper()+i[1:])
        else:
            t.append(i)
print(" ".join(t))
