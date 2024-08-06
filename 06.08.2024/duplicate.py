l=[1,2,3,3,4,3,5,6,7,5]
u=[]
for i in l:
  if i not in u:
    u.append(i)
print(f"The unique list is {u}")
