n=int(input("enter the number of candles"))
a=[]

for height in range(n):
    i=int(input("enter the height of the candle "))
    a.append(i)
print(a)
count=0
max=a[0]
count=0
for height in range(1,n):
    if(a[height]>max):
        max=a[height]

for height in range(0,n):
    if(a[height]==max):
        count+=1
print("no of candels she can blow is ",str(count))
