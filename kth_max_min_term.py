#find kth max term  term using bubble sort

def kth_Term(l,k):

    #firstly sort array in assending order
    for i in range(len(l)-1,0,-1):
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]

    #find kth term in sorted array
    max_kth_term=l[k-1]
    print(f"original sorted array: {l}")
    print(f"element present at kth position is: {max_kth_term}")

#user input
n=int(input("enter size of array: "))
list=[]
for p in range(n):
    list.append(int(input()))

k=int(input("enter kth term u want to access: \n"))
kth_Term(list,k)

#===============================================================================================
#find nth max term  term using selection sort

def nth_Term(li,n):

    #firstly sort array in decsending order using selection sort
    for i in range(len(li)):
        temp=i          
        for j in range(i+1,len(li)):
            if li[temp]<li[j]:
                temp=j
        
        li[temp],li[i]=li[i],li[temp]

    #find specific position from sorted array
    min_nth_term=li[n-1] 
    print(li)
    print(min_nth_term)

list=[23,90,-76,8,1,78]
k=int(input("enter position of element u wanna find: "))
nth_Term(list,k)