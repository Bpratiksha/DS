#reverse array using bubble sort

def reverse(n):

    #loop for given list
    for i in range(len(n)-1,0,-1):
        for j in range(i):

            #if 2nd position is grater than 1st then swap values
            if n[j]<n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]


# list=[23,890,65,3,78,98,1]

#taking input from user
n=int(input("enter size of array: "))
list=[]
for i in range(n):
    list.append(int(input()))

reverse(list)
print(list)