def sort(num):
    for i in range(1,len(num)):
        temp=num[i]          #1st element as temp or sorted array
        j=i-1                  #j is -1 for unsorted array
        while( j>=0 and temp<num[j]):   #j should be grater thn 0 and temp should be less thn num[j]
            num[j+1]=num[j]
            j=j-1
        
        num[j+1]=temp
        print(num)          #gives each pase

num=[4,7,2,98,67,1,6]
sort(num)
print(num)