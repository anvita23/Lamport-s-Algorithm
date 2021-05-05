i=j=count1=count2=0
m1=[] 
m2=[]
print("Enter event values for M1:")
for i in range(0,3):
    m1.append(input())
print("Enter event values for M2:")  
for i in range(0,3):
    m2.append(input())

for i in range(3):
    if(i==3 or j==3):
        break
    if(m1[i]<=m2[j]):
        count1=count1+1
        j=j+1

i=j=0

for i in range(3):
    if(i==3 or j==3):
        break
    if(m1[i]>=m2[j]):
        count2=count2+1
        j=j+1

if(count1==count2):
    print("M1 and M2 are concurrent events") 
elif(count1==3):
    print("M1 happened before M2") 
elif(count2==3):
    print("M2 happened before M1")  
else:
    print("M1 and M2 are concurrent events") 
