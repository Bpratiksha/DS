#find min and max element in array

def max_min(l):

    #sorted array using bubble sort (we can use any method)
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp

    #simply print last nd first element using index method
    print(f"sorted array : {l}")
    print(f"max element of array: {l[-1]}")
    print(f"max element of array: {l[0]}")

list=[20,679,-977,865,9,86,1]
max_min(list)

#==========================================================================================
# we have to find max and min term of a n array but without using any sorting method
#=======>we can use searchining methods......let's do  it

def search_max(li):
    maxnum,minnum=-1,1
    for i in range(len(li)):

        #compare two adjecent element and find max num and min
        if li[i]>maxnum:
            maxnum=li[i]    

        if li[i]<minnum:
            minnum=li[i]  
  
    print("the maximum element in the array: ",maxnum)
    print("the maximum element in the array: ",minnum)
       
n=int(input("enter size of array: "))     
list=[]
for i in range(n):
    list.append(int(input()))
print("original array: ",list)
search_max(list)
