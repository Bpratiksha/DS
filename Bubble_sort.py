numb=[64, 34, 25, 12, 22, 11, 90]
def result(numb):
    n=len(numb)
    for i in range(n-1,0,-1):             #for passes ==>(n-1)
        swapped=False   
        for j in range(i):                 #for each element in array ==>(i)
            if numb[j]>numb[j+1]:           #condition for swapping
                numb[j],numb[j+1]=numb[j+1],numb[j]
                swapped=True
        if swapped==False:                  #to optimize the solution we raised this condition:
            break                                #if swapping is not happening means codes is already sorted one
        print(numb)     #checking formation

result(numb)
print(numb)