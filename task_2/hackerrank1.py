a=[]
alice=0
bob=0
print("Enter a triplet for alice")
for i in range(0,3):
    values_of_a=int(input())
    a.append(values_of_a)
b = []
print("Enter a triplet for bob")
for i in range(0, 3):
    values_of_b= int(input())
    b.append(values_of_b)



for i in range(0,3):

    if(a[i]>b[i]):
        alice+=1
    elif(a[i]<b[i]):
        bob+=1
    else:
        alice+=0
        bob+=0

print(alice,bob)

