num_of_stairs=int(input("Enter number of steps"))
def stairs(a):
    n=num_of_stairs-1
    for i in range(0,num_of_stairs):
        print(" "*n,"#"*i)
        n-=1
    print("#"*num_of_stairs)
stairs(num_of_stairs)
