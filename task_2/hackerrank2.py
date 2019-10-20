n=int(input("Enter size of the matrix"))
matrix=[]
print("enter "+str(n*n)+" elements")
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)

d1=0
d2=0
differenece=0
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            d1+=matrix[i][j]
        if(i==n-j-1):
            d2+=matrix[i][j]
print("the diagonal difference =",end=" ")
print(d1-d2)
