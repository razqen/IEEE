s=input("Enter paragraph: ")
l=s.split()
print (l)
c=0
for i in l:
    if(i==i[::-1]):
        print(i)
        c+=1
if (c==0):print("0")