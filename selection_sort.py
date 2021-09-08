#Selection sort in Python

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [5,3,8,6,7,2]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

# for i in range(len(data)):
    #     temp=i
    #     for j in range(i+1,len(data)):
    #         if data[j]<data[temp]:
    #             temp=j
        
    #     data[temp],data[i]=data[i],data[temp]